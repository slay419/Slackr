from .data import *

# Provide a list of all channels (and their associated details)
def channels_listall(token):
    data = get_data()
    channels_list = []
    for channels in data['channels']:
        dict = {}
        dict.update({
            'channel_id': channels['channel_id'], 'name': channels['name']
        })
        channels_list.append(dict)
        return channels_list
