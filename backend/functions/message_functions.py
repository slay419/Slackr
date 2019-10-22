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
    if(u_id not in newchannel['members'] and u_id not in newchannel['owners']):
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
    message_id = 1 + len(newchannel['messages'])
    if(len(message) > 1000):
        return send_error('message is more than 1000 characters')
    #Obtaining u_id from token
    u_id = decode_token(token)
    #if user hasn't joined the channel they are sending a message in):
    if(u_id not in newchannel['members'] and u_id not in newchannel['owners']):
        return send_error('user is not in correct channel')
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
    return {'message_id': message_id}
