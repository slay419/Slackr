from .data import *

# Return a list of channels the user has already joined or is a owner of
def channels_list(token):
    u_id = decode_token(token)
    channels_list = []
    for channels in data['channels']:
        if u_id in channels['members'] or u_id in channels['owners']:
            channels_list.append({
                'channel_id': channels['channel_id'],
                'name': channels['name']
            })
    return channels_list
