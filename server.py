"""Flask server"""
import sys
from flask_cors import CORS
from json import dumps
from flask import Flask, request
import hashlib
import jwt
import re

APP = Flask(__name__)
CORS(APP)

@APP.route('/auth/register', methods=['POST'])
def echo4():
    pass

#GLOBAL VARIABLES
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
SECRET = "daenerys"
data = {
    'users' : []
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

@APP.route('/auth/register', methods = ['POST'])
def create():
    data = get_data()
    email = request.form.get('email')
    if valid_email(email) == True:
        for user in dict['users']:
            if email == user['email']
                return send_error('already used email')
    else:
        return send_error('invalid email')

    password = request.form.get('password')

    if len(password < 6):
        return send_error('password too short')

    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')

    #exception conditions
    if len(name_first) < 1 or len(name_first) > 50 or len(name_last) < 1 or len(name_last) > 50 {
        return send_error('names too long/short')
    }

    hashedPassword = hash_password(password)
    data['users'].append({
        'email' : email,
        'password' : hashedPassword,
        'name_first' : name_first,
        'name_last' : name_last
        'u_id': len(101 + len(data['users']))
    })
    return send_sucess({
        'u_id': len(101 + len(data['users']))
        'token' : generate_token(email)
        })

@APP.route('/login', methods = ['PUT'])
def connect():
    data = get_data()
    email = request.form.get('email')
    password = request.form.get('password')

    if (valid_email(email) == False) {
        return send_error('invalid email')
    }
    for user in data['users']:
        if user['email'] == email and hash_password(user['password']) == hash_password(password):
            return send_sucess({
                'u_id' : user['u_id']
                'token': generate_token(email)
            })
    return send_error('email does not exist or password is incorrect')




if __name__ == '__main__':
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000))
