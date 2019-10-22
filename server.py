"""Flask server"""
import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request
import hashlib
import jwt
import re
import copy
import time

from backend.functions.data import *
from backend.functions.channel_functions import *

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
    return send_success({
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
            return send_success({
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
    return send_success({})



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

    return send_success({})

@APP.route('/auth/logout', methods = ['PUT'])
def logout():

    token = request.form.get('token') #get token
    u_id = decode_token(token)
    user = user_dict(u_id)
    user['tokens'].remove(token)

    return send_success({})

#########################   CHANNEL FUNCTIONS  ###########################

@APP.route('/channels/create', methods = ['POST'])
def channel_create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    if not is_logged_in(token):
        return send_error(f"User: {decode_token(token)} not logged in")
    return send_success(channels_create(token, name, is_public))


@APP.route('/channels/listall', methods = ['GET'])
def listall():
    token = request.args.get('token')
    if not is_logged_in(token):
        return send_error(f"User: {decode_token(token)} is not logged in")
    return send_success(channels_listall(token))


@APP.route('/channels/list', methods = ['GET'])
def list():
    token = request.args.get('token')
    if not is_logged_in(token):
        return send_error(f"User: {decode_token(token)} is not logged in")
    return send_success(channels_list(token))

@APP.route('/channel/leave', methods = ['POST'])
def leave():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    if not is_logged_in(token):
        return send_error(f"User: {decode_token(token)} is not logged in")
    if not is_joined(token, channel_id):
        return send_error(f"User: {decode_token(token)} has not joined channel: {channel_id} yet")
    if not is_valid_channel(channel_id):
        return send_error(f"Channel ID: {channel_id} is invalid")
    return send_success(channel_leave(token, channel_id))

@APP.route('/channel/addowner', methods = ['POST'])
def addowner():
    token = request.form.get('token')   # person doing promoting
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))     # person being promoted
    if not is_logged_in(token):
        return send_error(f"User: {decode_token(token)} is not logged in")
    #if not is_logged_in(generate_token(u_id)):
    #    return send_error(f"User: {u_id} is not logged in")
    if not is_valid_channel(channel_id):
        return send_error(f"Channel ID: {channel_id} is invalid")
    if is_owner(u_id, channel_id):
        return send_error(f"User: {u_id} is already an owner")
    if not is_owner(decode_token(token), channel_id):
        return send_error(f"User: {decode_token(token)} does not have privileges to promote others")

    return send_success(channel_addowner(token, channel_id, u_id))

@APP.route('/channel/removeowner', methods = ['POST'])
def removeowner():
    token = request.form.get('token')   # person doing demoting
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))     # person being demoted
    if not is_logged_in(token):
        return send_error(f"User: {decode_token(token)} is not logged in")
    #if not is_logged_in(generate_token(u_id)):
    #    return send_error(f"User: {u_id} is not logged in")
    if not is_valid_channel(channel_id):
        return send_error(f"Channel ID: {channel_id} is invalid")
    if not is_owner(u_id, channel_id):
        return send_error(f"User: {u_id} is not an owner")
    if not is_owner(decode_token(token), channel_id):
        return send_error(f"User: {decode_token(token)} does not have privileges to demote others")

    return send_success(channel_removeowner(token, channel_id, u_id))


if __name__ == "__main__":
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))
