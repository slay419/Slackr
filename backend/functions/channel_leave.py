from .data import *

'''
####################### ASSUMPTIONS ######################
Assume you need to have joined the channel first before leaving
Assume "Channel does not exist" means channels you have not joined yet OR
channel_id hasn't been created yet
'''

def channel_leave(token, channel_id):
    
    pass



def is_joined(token, channel_id):
    data = get_data()
    u_id = decode_token(token)
    for channel_dict in data['channels']:
        if u_id in channel_dict['members'] or u_id in channel_dict['owners']:
            return True
    return False

# Returns true if the channel has been created already, false if no channel exists
def is_valid_channel(channel_id):
    data = get_data()
    channel_list = data['channels']
    for channels_dict in channel_list:
        if channels_dict['channel_id'] == channel_id:
            return True
    return False
