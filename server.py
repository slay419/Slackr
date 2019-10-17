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
    'users' : [],
    'channels' : []
}
#GlOBAL VARIABLES
def valid_email(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

def get_data():
    global data
    return data

def send_sucess(data):
    return dumps(data)

def send_error(message):
    return dumps({
        '_error': message
    })

def generate_token(string):
    global SECRET
    return jwt.encode({'string' : string}, SECRET, algorithm='HS256')

def decode_token(token):
    global SECRET
    decoded = jwt.decode(token, SECRET, algorithm='HS256')
    return decoded['string']

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#########################   AUTH FUNCTIONS  ###########################

@APP.route('/auth/register', methods = ['POST'])
def create():
    data = get_data()
    email = request.form.get('email')
    if valid_email(email) == True:
        for user in data['users']:
            if email == user['email']:
                return send_error('already used email')
    else:
        return send_error('invalid email')

    password = request.form.get('password')

    if len(password) < 6:
        return send_error('password too short')

    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')

    #exception conditions
    if len(name_first) < 1 or len(name_first) > 50 or len(name_last) < 1 or len(name_last) > 50:
        return send_error('names too long/short')


    hashedPassword = hash_password(password)
    data['users'].append({
        'email' : email,
        'password' : hashedPassword,
        'name_first' : name_first,
        'name_last' : name_last,
        'u_id': 101 + len(data['users'])
    })
    return send_sucess({
        'u_id': 101 + len(data['users']),
        'token': generate_token(email)
    })

@APP.route('/auth/login', methods = ['PUT'])
def connect():
    data = get_data()
    email = request.form.get('email')
    password = request.form.get('password')

    if (valid_email(email) == False):
        return send_error('invalid email')

    for user in data['users']:
        if user['email'] == email and hash_password(user['password']) == hash_password(password):
            return send_sucess({
                'u_id' : user['u_id'],
                'token': generate_token(email)
            })
    return send_error('email does not exist or password is incorrect')

#########################   CHANNEL FUNCTIONS  ###########################

@APP.route('/channels/create', methods = ['POST'])
def channel_create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = request.form.get('is_public')
    if len(name) > 20:
        return send_error("Name of channel is longer than 20 characters.")

    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    data = get_data()
    channels_list = data['channels']
    new_channel_id = len(channels_list) + 1
    # Store global variables
    data['channels'].append({
        'channel_id': new_channel_id, 'name': name, 'is_public': is_public
    })
    print(data['channels'])
    return send_sucess({
        'channel_id': new_channel_id
    })

@APP.route('/channels/listall', methods = ['GET'])
def listall():
    token = request.form.get('token')
    data = get_data()
    channels = data['channels']
    channels_list = copy.deepcopy(channels)
    for dict in channels_list:
        del dict['is_public']

    print channels_list
    print data
    return send_sucess(channels_list)




if __name__ == "__main__":
    APP.run(port = 2000)
