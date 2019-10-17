from json import dumps
from flask import Flask, request
import hashlib
import jwt
import re

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
def send_sucess(input):
    return dumps(input)

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
        'token'  : token,
        'profile' : None,
        'is_logged' : False
    })
    return send_sucess({ #return
        'u_id': u_id,
        'token' : token
        })

#LOGIN 
@APP.route('/login', methods = ['PUT'])
def connect():

    email = request.form.get('email') #get email
    password = request.form.get('password') #get password

    data = get_data()
    if valid_email(email) == False: #check valid email
        return send_error('invalid email')

    #check if email exists and if so check if password matches
    for user in data['users']:
        if user['email'] == email and hash_password(user['password']) == hash_password(password):
            user['is_logged'] = True
            return send_sucess({
                'u_id' : user['u_id'],
                'token': generate_token(user['u_id'])
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
            for user in channel['members']:
                if u_id == user:
                    return send_error('user already part of channel')
            channel['members'].append(u_id)
            return send_sucess({})
    return send_error({'channel id does not exist'})

#JOIN
@APP.route('/channel/join', methods = ['POST'])
def join():
    data = get_data()

    token = request.form.get('token') #get token
    channel_id = request.form.get('channel_id') #get channel_id

    u_id = decode_token(token)

    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            for user in data['users']:
                if u_id == user['u_id'] and user['permission_id'] != 3:
                    channel['members'].append(u_id)
                elif u_id == user['u_id'] and user['permission_id'] == 3 and channel['is_public'] == True:
                    channel['members'].append(u_id)
                else:
                    return send_error('user does not have rightts')
            return send_sucess({})
    return send_error({'channel id does not exist'})

if __name__ == "__main__":
    APP.run(port = 2000)

