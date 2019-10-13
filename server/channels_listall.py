import config
from channels_create import channels_create

# Provide a list of all channels (and their associated details)
def channels_listall(token):
    return config.GLOBAL_CHANNELS


     # return {channels}  # list of dictionary with {id: ' ', name: ' '}

'''
print(channels_listall(2))
owner_token = 1



channel1 = channels_create(owner_token, "Name1", True)
channel2 = channels_create(owner_token, "Name2", True)
channel3 = channels_create(owner_token, "Name3", True)
channel_id1 = channel1['id']
channel_id2 = channel2['id']
channel_id3 = channel3['id']

print(channels_listall(owner_token))
'''
