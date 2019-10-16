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
    'users' : [],
    'channels' : ['''' {'channel_id' : channel_id , 'owners' : [u_id1, u_id2...]members : [u_id, u_id2....], }, {} ...''']
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
        for user in dict['users']:
            if email == user['email']
                return send_error('already used email')
    else:
        return send_error('invalid email')

    password = request.form.get('password') # get password

    if len(password < 6): #rules for length of pasword
        return send_error('password too short')

    name_first = request.form.get('name_first') #get first name
    name_last = request.form.get('name_last') #get last name

    if len(name_first) < 1 or len(name_first) > 50 or len(name_last) < 1 or len(name_last) > 50 { #rules for length of name (first and last)
        return send_error('names too long/short')
    }

    hashedPassword = hash_password(password)

    #append all relevant information to users dictionary
    data['users'].append({
        'email' : email,
        'password' : hashedPassword,
        'name_first' : name_first,
        'name_last' : name_last
        'u_id': len(101 + len(data['users']))
    })
    return send_sucess({ #return
        'u_id': len(101 + len(data['users']))
        'token' : generate_token(email)
        })

#LOGIN 
@APP.route('/login', methods = ['PUT'])
def connect():
    data = get_data()
    email = request.form.get('email') #get email
    password = request.form.get('password') #get password

    if (valid_email(email) == False) { #check valid email
        return send_error('invalid email')
    }

    #check if email exists and if so check if password matches
    for user in data['users']:
        if user['email'] == email and hash_password(user['password']) == hash_password(password):
            return send_sucess({
                'u_id' : user['u_id']
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

    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            if (inv_u_id not in channel['owners']) {
                return send_error('invalid user id (not owner)')
            }
            for user in channel['members']:
                if u_id = user:
                    return send_error('user already exists')
            channel['members'].append(u_id)
            return send_sucess({})
    return send_error({'channel id does not exist'})




if __name__ == "__main__":
    APP.run(port = 2000)