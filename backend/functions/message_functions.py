from .data import *
from datetime import datetime

#input: token, channelid, start
#user must be a member of the channel
def channel_messages(token, channel_id, start):
    data = get_data()
    end = start + 50
    messages = []
    #Checking channel_id is valid
    newchannel = {}
    for channel in data['channels']:
        if(channel['channel_id'] == channel_id):
            newchannel.update(channel)
    if not newchannel:
        return send_error('Invalid channel_id')
    #Checking length of messages
    if(start > len(newchannel['messages'])):
        return send_error('Start index is > then amount of messages')
    u_id = decode_token(token)
    #Checking if user is authorised in correct channel
    if(is_member(u_id, channel_id) == False):
        return send_error('user is not in correct channel')
    index = start
    print("Index: " + str(index))
    print("Length of messages: " + str(len(newchannel['messages'])+1))
    print(newchannel['messages'])
    for i in range(index,len(newchannel['messages'])):
        messages.append(newchannel['messages'][i])
    if end > len(newchannel['messages']):
        end = -1
    return {'messages': messages, 'start': start, 'end': end,}

    #given start return end which is start + 50 or -1 if theres no more messages
            
#########################   MESSAGE FUNCTIONS  ###########################
#check valid channel aswell

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
    message_dict = {
        'message_id': message_id,
        'u_id': u_id,
        'message': message,
        'time_created': datetime.now(),
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
    return {}
