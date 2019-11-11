"""Flask server"""
import sys
from flask_cors import CORS
from flask_mail import Mail, Message
from random import randint
from json import dumps
from flask import Flask, request

import hashlib
import jwt
import re
import copy
import time

from backend.functions.exceptions import *
from backend.functions.data import *
from backend.functions.auth_functions import *
from backend.functions.channel_functions import *
from backend.functions.message_functions import *
from backend.functions.profile_functions import *
from backend.functions.misc_functions import *

APP = Flask(__name__)
APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
CORS(APP)

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'masterbranch101@gmail.com',
    MAIL_PASSWORD = "comp1531"
)


#########################   AUTH FUNCTIONS  ###########################

#REGISTER
@APP.route('/auth/register', methods = ['POST'])
def create():
    email = request.form.get('email') #get email
    password = request.form.get('password') # get password
    name_first = request.form.get('name_first') #get first name
    name_last = request.form.get('name_last') #get last name

    return send(auth_register(email, password, name_first, name_last))

#LOGIN
@APP.route('/auth/login', methods = ['POST'])
def connect():
    email = request.form.get('email') #get email
    password = request.form.get('password') #get password

    return send(auth_login(email, password))

#INVITE
@APP.route('/channel/invite', methods = ['POST'])
def invite():
    token = request.form.get('token') #get token
    channel_id = int(request.form.get('channel_id')) #get channel_id
    u_id = int(request.form.get('u_id')) #get u_id

    return send(channel_invite(token, channel_id, u_id))

#JOIN
@APP.route('/channel/join', methods = ['POST'])
def join():
    token = request.form.get('token') #get token
    channel_id = int(request.form.get('channel_id')) #get channel_id

    return send(channel_join(token, channel_id))

@APP.route('/auth/logout', methods = ['POST'])
def logout():
    token = request.form.get('token') #get token

    return send(auth_logout(token))

#PASSWORD RESET REQ
@APP.route('/auth/passwordreset/request', methods = ['POST'])
def reset_request():
    email = request.form.get('email')
    mail = Mail(APP)
    u_id = get_u_id(email)
    if u_id == None:
        raise ValueError(f"Email: {email} not registered")
    user = user_dict(u_id)

    try:
        msg = Message("Reset Code",
            sender="masterbranch101@gmail.com",
            recipients=[email])
        reset_code = str(u_id) + str(randint(100,999))
        user['reset_code'] = reset_code
        msg.body = f"Your reset code is {reset_code}"
        mail.send(msg)
        return {}
    except Exception as e:
        return (str(e))


#PASSWORD RESET RESET
@APP.route('/auth/passwordreset/reset', methods = ['POST'])
def reset_restore():
    reset_code = request.form.get('reset_code')
    new_password = request.form.get('new_password')
    return send(auth_passwordreset_reset(reset_code, new_password))

#########################   CHANNEL FUNCTIONS  ###########################

@APP.route('/channels/create', methods = ['POST'])
def channel_create():
    token = request.form.get('token')
    name = request.form.get('name')
    is_public = bool(request.form.get('is_public'))

    return send(channels_create(token, name, is_public))


@APP.route('/channels/listall', methods = ['GET'])
def listall():
    token = request.args.get('token')
    return send(channels_listall(token))


@APP.route('/channels/list', methods = ['GET'])
def list():
    token = request.args.get('token')
    return send(channels_list(token))

@APP.route('/channel/leave', methods = ['POST'])
def leave():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))

    return send(channel_leave(token, channel_id))

@APP.route('/channel/addowner', methods = ['POST'])
def addowner():
    token = request.form.get('token')   # person doing promoting
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))     # person being promoted

    return send(channel_addowner(token, channel_id, u_id))

@APP.route('/channel/removeowner', methods = ['POST'])
def removeowner():
    token = request.form.get('token')   # person doing demoting
    channel_id = int(request.form.get('channel_id'))
    u_id = int(request.form.get('u_id'))     # person being demoted

    return send(channel_removeowner(token, channel_id, u_id))

@APP.route('/channel/details', methods = ['GET'])
def details():
    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))

    return send(channel_details(token, channel_id))

@APP.route('/channel/messages', methods = ['GET'])
def listmessages():
    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id')) #must be valid channel
    start = int(request.args.get('start')) #cannot be >= no. of messages in channel

    return send(channel_messages(token, channel_id, start))

#########################   MESSAGE FUNCTIONS  ###########################
@APP.route('/message/sendlater', methods = ['POST'])
def sendlatermessages():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    message = request.form.get('message')
    time_sent = int(request.form.get('time_sent'))

    return send(message_sendlater(token, channel_id, message, time_sent))

@APP.route('/message/send', methods = ['POST'])
def sendmessages():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    message = request.form.get('message')

    return send(message_send(token, channel_id, message))

@APP.route('/message/remove', methods = ['DELETE'])
def removemessages():
    token = request.form.get('token')
    message_id = int(request.form.get('message_id'))

    return send(message_remove(token, message_id))

@APP.route('/message/edit', methods = ['PUT'])
def editmessages():
    token = request.form.get('token')
    message_id = int(request.form.get('message_id'))
    message = request.form.get('message')

    return send(message_edit(token, message_id, message))

@APP.route('/message/react', methods = ['POST'])
def reactmessages():
    token = request.form.get('token')
    message_id = int(request.form.get('message_id'))
    react_id = int(request.form.get('react_id'))

    return send(message_react(token, message_id, react_id))

@APP.route('/message/unreact', methods = ['POST'])
def unreactmessages():
    token = request.form.get('token')
    message_id = int(request.form.get('message_id'))
    react_id = int(request.form.get('react_id'))

    return send(message_unreact(token, message_id, react_id))

@APP.route('/message/pin', methods = ['POST'])
def pinmessages():
    token = request.form.get('token')
    message_id = int(request.form.get('message_id'))

    return send(message_pin(token, message_id))

@APP.route('/message/unpin', methods = ['POST'])
def unpinmessages():
    token = request.form.get('token')
    message_id = int(request.form.get('message_id'))

    return send(message_unpin(token, message_id))

#########################  USER PROFILE FUNCTIONS  ###########################
# SET USER EMAIL
@APP.route('/user/profile/setemail', methods = ['PUT'])
def setemail():
    token = request.form.get('token')
    email = request.form.get('email')

    return send(user_profile_setemail(token, email))

# SET USER HANDLE
@APP.route('/user/profile/sethandle', methods = ['PUT'])
def sethandle():
    token = request.form.get('token')
    handle_str = request.form.get('handle_str')

    return send(user_profile_sethandle(token, handle_str))

# SET USER NAMES
@APP.route('/user/profile/setname', methods = ['PUT'])
def setnames():
    token = request.form.get('token')
    name_first = request.form.get('name_first')
    name_last = request.form.get('name_last')

    return send(user_profile_setname(token, name_first,name_last))

# RETRIEVE USER PROFILE
@APP.route('/user/profile', methods = ['GET'])
def retrieveProf():
    token = request.args.get('token')
    u_id = int(request.args.get('u_id'))

    return send(user_profile(token, u_id))

@APP.route('/user/profiles/uploadphoto', methods = ['POST'])
def uploadPhoto():
    token = request.form.get('token')
    img_url = str(request.form.get('img_url'))
    x_start = int(request.form.get('x_start'))
    y_start = int(request.form.get('y_start'))
    x_end = int(request.form.get('x_end'))
    y_end = int(request.form.get('y_end'))

    return send(user_profile_uploadphoto(token, img_url, x_start, y_start, x_end, y_end))

@APP.route('/users/all', methods = ['GET'])
def users_all():
    token = request.args.get('token')
    return send(users_listall(token))
#########################  MISC. FUNCTIONS  ###########################

# STANDUP START
@APP.route('/standup/start', methods = ['POST'])
def standupStart():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    length = int(request.form.get('length'))

    return send(standup_start(token, channel_id, length))

# STANDUP SEND
@APP.route('/standup/send', methods = ['POST'])
def standupSend():
    token = request.form.get('token')
    channel_id = int(request.form.get('channel_id'))
    message = request.form.get('message')

    return send(standup_send(token, channel_id, message))

# STANDUP ACTIVE
@APP.route('/standup/active', methods = ['GET'])
def standupActive():
    token = request.args.get('token')
    channel_id = int(request.args.get('channel_id'))

    return send(standup_active(token,channel_id))

# SEARCH
@APP.route('/search', methods = ['GET'])
def searchWrapper():
    token = request.args.get('token')
    query_str = request.args.get('query_str')

    return send(search(token, query_str))

# ADMIN PERM CHANGE
@APP.route('/admin/userpermission/change', methods = ['POST'])
def userPermChange():
    token = request.form.get('token')
    u_id = int(request.form.get('u_id'))
    permission_id = int(request.form.get('permission_id'))

    return send(admin_userpermission_change(token, u_id, permission_id))



if __name__ == "__main__":
    APP.run(port=(sys.argv[1] if len(sys.argv) > 1 else 5000), debug=True)
