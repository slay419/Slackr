from .data import *

# Provide a list of all channels (and their associated details)
def channels_listall(token):
    channels_list = []
    for channels in data['channels']:
        dict = {}
        dict.update({
            'channel_id': channels['channel_id'], 'name': channels['name']
        })
        channels_list.append(dict)
        print(channels_list)
        print(data)
        return channels_list
