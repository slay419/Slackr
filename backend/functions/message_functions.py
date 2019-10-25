from .data import *
from datetime import datetime
from datetime import timezone

#########################   MESSAGE FUNCTIONS  ###########################
def message_sendlater(token, channel_id, message, time_sent):
    data = get_data()
    
    #The message_id will be 1 + length of messages in a specific channel
    newchannel = {}
    for channel in data['channels']:
        if(channel['channel_id'] == channel_id):
            newchannel.update(channel)
    message_id = 1 + len(data['messages'])
    if not is_valid_channel(channel_id):
        raise ValueError('Channel ID is not a valid channel')
    if(len(message) > 1000):
        raise ValueError('Message is more than 1000 characters')
    #Obtaining u_id from token
    u_id = decode_token(token)
    #if user hasn't joined the channel they are sending a message in):
    if(is_member(u_id, channel_id) == False):
        raise AccessError('Authorised user has not joined the channel they are trying to post to')
    dt = datetime.now()
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    if time_sent < timestamp:
        raise ValueError('Time sent is a time in the past')
    message_dict = {
        'message_id': message_id,
        'u_id': u_id,
        'message': message,
        'time_created': time_sent,
        'is_unread': True,
        'reacts': [],
        'is_pinned': False,
    }
    for channel in data['channels']:
        if(channel['channel_id'] == channel_id):
            channel['messages'].insert(0, message_dict)
            data['messages'].append(message_dict)
            print('return 3')
    return {'message_id': message_id}
    
#input: token,channelid,message
def message_send(token, channel_id, message):
    #Initialising all data from input
    data = get_data()
    
    #The message_id will be 1 + length of messages in a specific channel
    newchannel = {}
    for channel in data['channels']:
        if(channel['channel_id'] == channel_id):
            newchannel.update(channel)
    message_id = 1 + len(data['messages'])
    if(len(message) > 1000):
        print('return 1')
        return send('message is more than 1000 characters')
    #Obtaining u_id from token
    u_id = decode_token(token)
    #if user hasn't joined the channel they are sending a message in):
    if(is_member(u_id, channel_id) == False):
        print('return 2')
        return send('user is not in correct channel')
    dt = datetime.now()
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    message_dict = {
        'message_id': message_id,
        'u_id': u_id,
        'message': message,
        'time_created': timestamp,
        'is_unread': True,
        'reacts': [],
        'is_pinned': False,
    }
    for channel in data['channels']:
        if(channel['channel_id'] == channel_id):
            channel['messages'].insert(0, message_dict)
            data['messages'].append(message_dict)

    print(message_dict)
    return {'message_id': message_id}

def message_remove(token, message_id):
    data = get_data()
    #remove message from global dict
    for message in data['messages']:
        if message['message_id'] == message_id:
            print("we found a match")
            data['messages'].remove(message)
    #Searching for correct messagedict in the channels list
    channels = data['channels']
    for channeldict in channels:
        messagelist = channeldict['messages']
        for messagedict in messagelist:
            if messagedict['message_id'] == message_id:
                messagelist.remove(messagedict) 
    print (data['messages'])
    return {}
    
def message_edit(token, message_id, message):
    data = get_data()
    u_id = decode_token(token)
    userdict = user_dict(u_id)
    #u_id is used to find corresponding message
    if(len(message) > 1000):
        return send('message is more than 1000 characters')
    #accesserror when nonadmin/owner attempts to edit someone elses message
    for editmessage in data['messages']:
        print(editmessage['message_id'])
        print(message_id)
        if editmessage['message_id'] == int(message_id):
            if editmessage['u_id'] == u_id or userdict['permission_id'] == 3:
                editmessage['message'] = message
                print('message was edited')
            else:
                return send('user is editing a message not of own')
    #detect if no message was found
    return {}
    
def message_react(token, message_id, react_id):
    data = get_data()
    #check valid react_id
    for message in data['messages']:
        if message['message_id'] == int(message_id):
            if react_id not in message['reacts']:
                message['reacts'].append(react_id)
                print(message['reacts'])
            else:
                return send('message already has this react_id')
    print(message)
    return {}

def message_unreact(token, message_id, react_id):
    data = get_data()
    for message in data['messages']:
        if message['message_id'] == int(message_id):
            if react_id in message['reacts']:
                message['reacts'].remove(react_id)
                print(message['reacts'])
            else:
                return send('message does not have this react_id')
    print(message)
    return {}
    
def message_pin(token, message_id):
    data = get_data()
    #check valid message
    if not is_valid_message(message_id):
        return send("Message ID is invalid")
    #checking if user is an admin
    u_id = decode_token(token)
    user =  user_dict(u_id)
    if user['permission_id'] != 1:
        return send('user is not an admin')
    #Cycle through message list until id match and check wether it is already
    #pinned, if not pin it
    for message in data['messages']:
        if message['message_id'] == int(message_id):
            if message['is_pinned'] == False:
                message['is_pinned'] = True
            else:
                return send('message is already pinned')
    print(message)
    return {}

def message_unpin(token, message_id):
    data = get_data()
    #check valid message
    if not is_valid_message(message_id):
        return send("Message ID is invalid")
    #checking if user is an admin
    u_id = decode_token(token)
    user =  user_dict(u_id)
    if user['permission_id'] != 1:
        return send('user is not an admin')
    #Cycle through message list until id match and check wether it is
    #pinned, if it is unpin it
    for message in data['messages']:
        if message['message_id'] == int(message_id):
            if message['is_pinned'] == True:
                message['is_pinned'] = False
            else:
                return send("message isn't currently pinned")
    print(message)
    return {}
