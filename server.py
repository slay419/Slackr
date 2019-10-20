"""Flask server"""
import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request
import hashlib
import jwt
import re
import copy
<<<<<<< HEAD
import time

from backend.functions.data import *
from backend.functions.channels_create import channels_create
from backend.functions.channels_listall import channels_listall
from backend.functions.channels_list import channels_list
from backend.functions.channel_leave import channel_leave
=======
import sys

APP = Flask(__name__)
CORS(APP)

@APP.route('/auth/register', methods=['POST'])
def echo4():
    pass

#GLOBAL VARIABLES
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
SECRET = "daenerys"
data = {
    'users' : [], # should have a dictionary for each user
    'channels' : [] #shoudl have a dictionary for each channel

    # e.g. {email, password, name_first, name_last, u_id, permission_id, handle, token, profile, is_logged}

    #e.g {'channel_id' : 1234 , 'name' : channelname, 'owners' : [u_id1, u_id2...], members : [u_id, u_id2....], 'ispublic': True }
}
#GlOBAL VARIABLES

#check if email is valid
def valid_email(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

#abstraction for returning global data
def get_data():
    global data
    return data

#abstraction for returning json string
def send_sucess(data):
    return dumps(data)

def send_error(message):
    return dumps({
        '_error': message
    })

#encodes token given string and SECRET
def generate_token(string):
    global SECRET
    return jwt.encode({'string' : string}, SECRET, algorithm='HS256')

#decodes token given string and SECRET
def decode_token(token):
    global SECRET
    decoded = jwt.decode(token, SECRET, algorithm='HS256')
    return decoded['string']
>>>>>>> master

APP = Flask(__name__)

#########################   AUTH FUNCTIONS  ###########################

#REGISTER
@APP.route('/auth/register', methods = ['POST'])
def create():

    email = request.form.get('email') #get email
    password = request.form.get('password') # get password
    name_first = request.form.get('name_first') #get first name
    name_last = request.form.get('name_last') #get last name


    data = get_data()
    #check if email already exist
    if valid_email(email) == True:
        for user in data['users']:
            if email == user['email']:
                return send_error('already used email')
    else:
        return send_error('invalid email')

    if len(password) < 6: #rules for length of pasword
        return send_error('password too short')


    if len(name_first) < 1 or len(name_first) > 50 or len(name_last) < 1 or len(name_last) > 50: #rules for length of name (first and last)
        return send_error('names too long/short')

    handle = ''.join((name_last, name_last))
    for user in data['users']:
        if handle == user['handle']:
            handle += str(1 + len(data['users']))

    hashedPassword = hash_password(password)
    u_id = 101 + len(data['users'])
    token = generate_token(u_id)

    if len(data['users']) == 0:
        permission_id = 1
    else:
        permission_id = 3


    #append all relevant information to users dictionary
    data['users'].append({
        'email' : email,
        'password' : hashedPassword,
        'name_first' : name_first,
        'name_last' : name_last,
        'u_id': u_id,
        'permission_id' : permission_id,
        'handle' : handle,
        'tokens'  : [],
        'profile' : None
    })
    return send_sucess({
        'u_id': u_id,
        'token' : token
    })

#LOGIN
@APP.route('/auth/login', methods = ['PUT'])
def connect():

    email = request.form.get('email') #get email
    password = request.form.get('password') #get password

    data = get_data()
    if valid_email(email) == False: #check valid email
        return send_error('invalid email')

    #check if email exists and if so check if password matches
    for user in data['users']:
        if user['email'] == email and user['password'] == hash_password(password):
            u_id = user['u_id']
            token = generate_token(u_id)
            user['tokens'].append(token)
            return send_sucess({
                'u_id' : u_id,
                'token': token
            })

    return send_error('email does not exist or password is incorrect')


#INVITE
@APP.route('/channel/invite', methods = ['POST'])
def invite():

    token = request.form.get('token') #get token
    channel_id = request.form.get('channel_id') #get channel_id
    u_id = request.form.get('u_id') #get u_id

    inv_u_id = decode_token(token)

    if u_id == inv_u_id:
        return send_error('cannot invite self')

    channel = channel_dict(channel_id)
    if channel == None:
        return send_error('channel id does not exist')

    for user in channel['members']:
        if u_id == user:
            return send_error('user already part of channel')
    channel['members'].append(u_id)
    return send_sucess({})



#JOIN
@APP.route('/channel/join', methods = ['POST'])
def join():

    token = request.form.get('token') #get token
    channel_id = request.form.get('channel_id') #get channel_id

    u_id = decode_token(token)

    channel = channel_dict(channel_id)
    user = user_dict(u_id)
    if user == None or channel == None:
        return send_error('channel id/ user id does not exist')

    if user['permission_id'] != 3:
        channel['members'].append(u_id)
    elif user['permission_id'] == 3 and channel['is_public'] == True:
        channel['members'].append(u_id)
    else:
        return send_error('user does not have rightts')

    return send_sucess({})

@APP.route('/auth/logout', methods = ['PUT'])
def logout():

    token = request.form.get('token') #get token
    u_id = decode_token(token)
    user = user_dict(u_id)
    user['tokens'].remove(token)

    return send_sucess({})

#########################   CHANNEL FUNCTIONS  ###########################

@APP.route('/channels/create', methods = ['POST'])
def channel_create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    if not is_logged_in(token):
        return send_error("User not logged in")
    return send_sucess(channels_create(token, name, is_public))


@APP.route('/channels/listall', methods = ['GET'])
def listall():
    token = request.args.get('token')
    if not is_logged_in(token):
        return send_error("User is not logged in")
    return send_sucess(channels_listall(token))


@APP.route('/channels/list', methods = ['GET'])
def list():
    token = request.args.get('token')
    if not is_logged_in(token):
        return send_error("User is not logged in")
    return send_sucess(channels_list(token))

@APP.route('/channel/leave', methods = ['POST'])
def leave():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    if not is_logged_in(token):
        return send_error("User is not logged in")
    if not is_joined(token, channel_id):
        return send_error("User has not joined this channel yet")
    if not is_valid_channel(channel_id):
        return send_error("Channel ID is invalid")
    return send_sucess(channel_leave(token, channel_id))

if __name__ == "__main__":
<<<<<<< HEAD
    APP.run()
=======
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))
>>>>>>> master
