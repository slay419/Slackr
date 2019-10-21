from .data import *

'''
####################### ASSUMPTIONS ######################
Assume you need to have joined the channel first before leaving
Assume "Channel does not exist" means channels you have not joined yet OR
channel_id hasn't been created yet
'''

def channel_leave(token, channel_id):
    channel = channel_dict(channel_id)
    u_id = decode_token(token)
    # loop through owners
    for user in channel['owners']:
        if user == u_id:
            channel['owners'].remove(u_id)
    # loop through members
    for user in channel['members']:
        if user == u_id:
            channel['members'].remove(u_id)
    return {}
