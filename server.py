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
from backend.functions.auth_functions import *
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
    
    return send(auth_register(email, password, name_first, name_last));

#LOGIN
@APP.route('/auth/login', methods = ['PUT'])
def connect():

    email = request.form.get('email') #get email
    password = request.form.get('password') #get password


    return send(channel_invite(email, password))


#INVITE
@APP.route('/channel/invite', methods = ['POST'])
def invite():

    token = request.form.get('token') #get token
    channel_id = request.form.get('channel_id') #get channel_id
    u_id = request.form.get('u_id') #get u_id

    
    return send(channel_invite(token, channel_id, u_id))



#JOIN
@APP.route('/channel/join', methods = ['POST'])
def join():

    token = request.form.get('token') #get token
    channel_id = request.form.get('channel_id') #get channel_id


    return send(channel_join(token, channel_id))

@APP.route('/auth/logout', methods = ['PUT'])
def logout():

    token = request.form.get('token') #get token


    return send(auth_logout(token))

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

