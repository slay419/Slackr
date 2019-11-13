from json import dumps
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from werkzeug.exceptions import HTTPException
from random import randint
import hashlib
import jwt
import re
import copy
import time
import urllib.request
from PIL import Image
from .exceptions import *
#GLOBAL VARIABLES
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
SECRET = "daenerys"
data = {
    'users' : [],
    'channels' : [],
    'messages' : []
}

########################    HELPER FUNCTIONS    #########################

# Check if email is valid
def valid_email(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

# Abstraction for returning global data
def get_data():
    global data
    return data

# Abstraction for returning json string
def send(data):
    return dumps(data)

# Encodes token given string and SECRET
def generate_token(string):
    global SECRET
    return jwt.encode({'string' : string, 'time' : time.time()}, SECRET, algorithm='HS256').decode('utf-8')

# Decodes token given string and SECRET
def decode_token(token):
    global SECRET
    decoded = jwt.decode(token.encode('utf-8'), SECRET, algorithms=['HS256'])
    return decoded['string']

# Generates hash for string
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Return Bool value if user is logged in based on token
def is_logged_in(token):
    u_id = decode_token(token)
    user = user_dict(u_id)
    if user == None:
        return False
    if token in user['tokens']:
        return True
    else:
        return False

# Return a dictionary with the user's authentication data
def user_dict(u_id):
    data = get_data()
    for user in data['users']:
        if u_id == user['u_id']:
            return user
    return None

# Return a dictionary with the channel's data
def channel_dict(channel_id):
    data = get_data()
    for channel in data['channels']:
        if channel_id == channel['channel_id']:
            return channel
    return None

# Return a dictionary with the message's data
def message_dict(message_id):
    data = get_data()
    for messages in data['messages']:
        if message_id == messages['message_id']:
            return messages
    return None

# Returns true if the channel has been created already, false if no channel exists
def is_valid_channel(channel_id):
    data = get_data()
    channel_list = data['channels']
    for channels_dict in channel_list:
        if channels_dict['channel_id'] == channel_id:
            return True
    return False

# Returns true if the message has been created already, false if no message exists
def is_valid_message(message_id):
    data = get_data()
    message_list = data['messages']
    for messages_dict in message_list:
        if messages_dict['message_id'] == int(message_id):
            return True
    return False

# Returns True if the user is an owner in the given channel ID, false otherwise
def is_owner(u_id, channel_id):
    channel = channel_dict(channel_id)
    # loop through channel to check if owner
    for dict in channel['owner_members']:
        if u_id == dict['u_id']:
            return True
    return False

# Returns True if the user is a member in the given channel ID, false otherwise
def is_member(u_id, channel_id):
    channel = channel_dict(channel_id)
    if channel == None:
        return False
    # loop through channel to check if member
    for dict in channel['all_members']:
        if u_id == dict['u_id']:
            return True
    return False

# Returns a dictionary with the user's first and last name
def get_user_name(u_id):
    data = get_data()
    for user in data['users']:
        if u_id == user['u_id']:
            return {user['name_first'], user['name_last']}
    return None

# Returns a string of the user's first name
def get_first_name(u_id):
    user = user_dict(u_id)
    for user in data['users']:
        if u_id == user['u_id']:
            return user['name_first']
    return None

# Returns a string of the user's last name
def get_last_name(u_id):
    data = get_data()
    for user in data['users']:
        if u_id == user['u_id']:
            return user['name_last']
    return None

# Returns a user's ID from their given email
def get_u_id(email):
    data = get_data()
    for user in data['users']:
        if email == user['email']:
            return user['u_id']
    return None

# Returns the user's permission ID - 1: Owner, 2: Admin, 3: Member
def get_permission_id(u_id):
    user = user_dict(u_id)
    return user['permission_id']

# Returns the user's reset code sent after using the password reset feature
def get_reset_code(u_id):
    user = user_dict(u_id)
    return user['reset_code']

###################     PYTEST HELPER FUNCTIONS     ###################

# Clears all data from the database
def reset_data():
    global data
    reset_users()
    reset_channels()
    reset_messages()

# Clears all users from the database
def reset_users():
    global data
    users = data['users']
    users.clear()

# Clears all channels from the database
def reset_channels():
    global data
    channels = data['channels']
    channels.clear()

# Clears all messages from the database
def reset_messages():
    global data
    messages = data['messages']
    messages.clear()
    channels = data['channels']
    for channeldict in channels:
        messagelist = channeldict['messages']
        messagelist.clear()
