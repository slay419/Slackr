from .data import *
from datetime import datetime
from datetime import timezone

#########################   MESSAGE FUNCTIONS  ###########################
def message_sendlater(token, channel_id, message, time_sent):
    data = get_data()

    #The message_id will be 1 + length of messages in a specific channel
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
    channel = channel_dict(channel_id)
    channel['messages'].insert(0, message_dict)
    data['messages'].append(message_dict)
    return {'message_id': message_id}

#input: token,channelid,message
def message_send(token, channel_id, message):
    #Initialising all data from input
    data = get_data()

    #The message_id will be 1 + length of messages in a specific channel
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
    message_dict = {
        'message_id': message_id,
        'u_id': u_id,
        'message': message,
        'time_created': timestamp,
        'is_unread': True,
        'reacts': [],
        'is_pinned': False,
    }
    channel = channel_dict(channel_id)
    channel['messages'].insert(0, message_dict)
    data['messages'].append(message_dict)
    return {'message_id': message_id}

def message_remove(token, message_id):
    data = get_data()
    u_id = decode_token(token)
    userdict = user_dict(u_id)
    #remove message from global dict
    if not is_valid_message(message_id):
        raise ValueError('Message (based on ID) no longer exists')
    message = message_dict(message_id)
    if message['u_id'] == u_id or userdict['permission_id'] != 3:
        data['messages'].remove(message)
    else:
        raise AccessError('user is removing a message not of own')
    #Searching for correct messagedict in the channels list
    channels = data['channels']
    for channeldict in channels:
        messagelist = channeldict['messages']
        for messagedict in messagelist:
            if messagedict['message_id'] == message_id:
                messagelist.remove(messagedict)
    return {}

def message_edit(token, message_id, message):
    data = get_data()
    u_id = decode_token(token)
    userdict = user_dict(u_id)
    #u_id is used to find corresponding message
    if(len(message) > 1000):
        raise ValueError('message is more than 1000 characters')
    if not is_valid_message(message_id):
        raise ValueError('Message (based on ID) no longer exists')
    #accesserror when nonadmin/owner attempts to edit someone elses message
    editmessage = message_dict(message_id)
    if editmessage['u_id'] == u_id or userdict['permission_id'] != 3:
        editmessage['message'] = message
    else:
        raise AccessError('user is editing a message not of own')
    #detect if no message was found
    return {}

def message_react(token, message_id, react_id):
    data = get_data()
    #check valid react_id
    u_id = decode_token(token)
    if not is_valid_message(message_id):
        raise ValueError('message_id is not a valid message within a channel that the authorised user has joined')
    if react_id != 1:
        raise ValueError('react_id is not a valid React ID.')
    #First set is_this_user_reacted to false if not contained in u_id
    for message in data['messages']:
        for react in message['reacts']:
            if u_id not in react['u_ids']:
                react['is_this_user_reacted'] = False
            else:
               react['is_this_user_reacted'] = True
    #Check if the message has react_dict already
    for message in data['messages']:
        if message['message_id'] == message_id:
            #if react_id dict doesn't already exist for specific message
            if not any(d['react_id'] == react_id for d in message['reacts']):
                dict = {
                    'react_id': react_id,
                    'u_ids': [u_id],
                    'is_this_user_reacted': True
                }
                message['reacts'].append(dict)
            #if the dict does already exist, append the u_id to it
            else:
                for react_dict in message['reacts']:
                    if react_dict['react_id'] == react_id:
                        if u_id not in react_dict['u_ids']:
                            react_dict['u_ids'].append(u_id)
                            react_dict['is_this_user_reacted'] = True
                        else:
                            raise ValueError('user has already reacted to this message')
    for message in data['messages']:
        if message['message_id'] == message_id:
            print(message['reacts'])
    return {}

def message_unreact(token, message_id, react_id):
    data = get_data()
    u_id = decode_token(token)
    if not is_valid_message(message_id):
        raise ValueError('message_id is not a valid message within a channel that the authorised user has joined')
    if react_id != 1:
        raise ValueError('react_id is not a valid React ID.')
    #Check if the message has react_dict already
    for message in data['messages']:
        if message['message_id'] == message_id:
            #if react_id dict doesn't already exist for specific message
            if not any(d['react_id'] == react_id for d in message['reacts']):
                raise ValueError('message does not have this react_id')
            #if the dict does already exist, append the u_id to it
            else:
                for react_dict in message['reacts']:
                    if react_dict['react_id'] == react_id:
                        react_dict['u_ids'].remove(u_id)
                        react_dict['is_this_user_reacted'] = False
    for message in data['messages']:
        if message['message_id'] == message_id:
            print(message['reacts'])
    return {}

def message_pin(token, message_id):
    data = get_data()
    #check valid message
    if not is_valid_message(message_id):
        raise ValueError("Message ID is invalid")
    #checking if user is an admin
    u_id = decode_token(token)
    user =  user_dict(u_id)
    #get channel_id
    channels = data['channels']
    for channeldict in channels:
        messagelist = channeldict['messages']
        for messagedict in messagelist:
            if messagedict['message_id'] == message_id:
                channel_id = channeldict['channel_id']
    if user['permission_id'] != 1:
        raise ValueError('user is not an admin')
    #Cycle through message list until id match and check wether it is already
    #pinned, if not pin it
    message = message_dict(message_id)
    if(is_member(u_id, channel_id) == False):
        raise AccessError('Authorised user has not joined the channel they are trying to pin to')
    if message['is_pinned'] == False:
        message['is_pinned'] = True
    else:
        raise ValueError('message is already pinned')
    return {}

def message_unpin(token, message_id):
    data = get_data()
    #check valid message
    if not is_valid_message(message_id):
        raise ValueError("Message ID is invalid")
    #checking if user is an admin
    u_id = decode_token(token)
    user =  user_dict(u_id)
    #get channel_id
    channels = data['channels']
    for channeldict in channels:
        messagelist = channeldict['messages']
        for messagedict in messagelist:
            if messagedict['message_id'] == message_id:
                channel_id = channeldict['channel_id']
    if user['permission_id'] != 1:
        raise ValueError('user is not an admin')
    #Cycle through message list until id match and check wether it is
    #pinned, if it is unpin it
    message = messagedict(message_id)
    if(is_member(u_id, channel_id) == False):
        raise AccessError('Authorised user has not joined the channel they are trying to pin to')
    if message['is_pinned'] == True:
        message['is_pinned'] = False
    else:
        raise ValueError("message isn't currently pinned")
    return {}
