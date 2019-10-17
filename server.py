from json import dumps
from flask import Flask, request
import hashlib
import jwt
import re
import copy

APP = Flask(__name__)

#GLOBAL VARIABLES
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
SECRET = "daenerys"
data = {
    'users' : [], # should have a dictionary for each user
    'channels' : [] #shoudl have a dictionary for each channel

    #e.g {'channel_id' : 1234 , 'name' : channelname, 'owners' : [u_id1, u_id2...], members : [u_id, u_id2....], 'ispublic': True }
}
#GlOBAL VARIABLES

#########################   AUTH FUNCTIONS  ###########################

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

#generates hash for string
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#REGISTER
@APP.route('/auth/register', methods = ['POST'])
def create():
    data = get_data()
    email = request.form.get('email') #get email

    #check if email already exist
    if valid_email(email) == True:
        for user in data['users']:
            if email == user['email']:
                return send_error('already used email')
    else:
        return send_error('invalid email')

    password = request.form.get('password') # get password

    if len(password) < 6: #rules for length of pasword
        return send_error('password too short')


    name_first = request.form.get('name_first') #get first name
    name_last = request.form.get('name_last') #get last name

    if len(name_first) < 1 or len(name_first) > 50 or len(name_last) < 1 or len(name_last) > 50: #rules for length of name (first and last)
        return send_error('names too long/short')



    handle = "handle"

    hashedPassword = hash_password(password)


    #append all relevant information to users dictionary
    data['users'].append({
        'email' : email,
        'password' : hashedPassword,
        'name_first' : name_first,
        'name_last' : name_last,
        'u_id': 101 + len(data['users']),
        'permission_id' : 3,
        'handle' : handle,
        'profile' : None
        'token': generate_token
    })
    print(data)
    return send_sucess({ #return
        'u_id': 101 + len(data['users']),
        'token' : generate_token(email)
    })

#LOGIN
@APP.route('/login', methods = ['PUT'])
def connect():
    data = get_data()
    email = request.form.get('email') #get email
    password = request.form.get('password') #get password

    if valid_email(email) == False: #check valid email
        return send_error('invalid email')

    #check if email exists and if so check if password matches
    for user in data['users']:
        if user['email'] == email and hash_password(user['password']) == hash_password(password):
            return send_sucess({
                'u_id' : user['u_id'],
                'token': generate_token('u_id')
            })

    return send_error('email does not exist or password is incorrect')


#INVITE
@APP.route('/channel/invite', methods = ['POST'])
def invite():
    data = get_data()

    token = request.form.get('token') #get token
    channel_id = request.form.get('channel_id') #get channel_id
    u_id = request.form.get('u_id') #get u_id

    inv_u_id = decode_token(token)

    if u_id == inv_u_id:
        return send_error('cannot invite self')

    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if inv_u_id not in channel['owners']:
                return send_error('invalid user id (not owner)')
            for user in channel['members']:
                if u_id == user:
                    return send_error('user already part of channel')
            channel['members'].append(u_id)
            return send_sucess({})
    return send_error({'channel id does not exist'})

#########################   CHANNEL FUNCTIONS  ###########################

@APP.route('/channels/create', methods = ['POST'])
def channel_create():
    data = get_data()
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    #if not is_logged_in(token):
    #    send_error("User not logged in")
    if len(name) > 20:
        return send_error("Name of channel is longer than 20 characters.")

    owner_id = decode_token(token)

    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    new_channel_id = len(data['channels']) + 1

    # Create a dictionary with all the relevant info and append to data
    dict = {
        'channel_id': new_channel_id, 'name': name, 'owners': [owner_id],
        'members': [], 'is_public': is_public
    }
    data['channels'].append(dict)
    print(data['channels'])
    return send_sucess({
        'channel_id': new_channel_id
    })

@APP.route('/channels/listall', methods = ['GET'])
def listall():
    token = request.form.get('token')
    data = get_data()

    channels_list = []
    for channels in data['channels']:
        dict = {}
        dict.update('channel_id': channels['channel_id'], 'name': channels['name'])
        channels_list.append(dict)



    channels = data['channels']
    channels_list = copy.deepcopy(channels)
    for dict in channels_list:
        del dict['is_public']

    print channels_list
    print data
    return send_sucess(channels_list)




if __name__ == "__main__":
    APP.run(port = 2000)
