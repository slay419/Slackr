from .data import *


def channels_create(token, name, is_public):
    if len(name) > 20:
        return send_error("Name of channel is longer than 20 characters.")
    data = get_data()
    owner_id = decode_token(token)
    print(owner_id)
    get_user_name(owner_id)
    print(f"owner's name is: {get_user_name(owner_id)}")

    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    new_channel_id = len(data['channels']) + 1
    # Create a dictionary with all the relevant info and append to data
    dict = {
        'channel_id': new_channel_id,
        'name': name,
        'owners': [owner_id],
        'members': [],
        'is_public': is_public,
        'messages': []
    }
    data['channels'].append(dict)
    print(data['channels'])
    return {
        'channel_id': new_channel_id
    }

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

# Return a list of channels the user has already joined or is a owner of
def channels_list(token):
    data = get_data()
    u_id = decode_token(token)
    channels_list = []
    for channels in data['channels']:
        if u_id in channels['members'] or u_id in channels['owners']:
            channels_list.append({
                'channel_id': channels['channel_id'],
                'name': channels['name']
            })
    return channels_list


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

def channel_addowner(token, channel_id, u_id):
    channel = channel_dict(channel_id)
    print(f"channel owners are: {channel['owners']}")
    # append user to list of owners
    channel['owners'].append(u_id)
    print(f"channel owners are: {channel['owners']} after appending")
    return {}


def channel_removeowner(token, channel_id, u_id):
    channel = channel_dict(channel_id)
    print(f"channel owners are: {channel['owners']}")
    # remove user from list of owners
    channel['owners'].remove(u_id)
    print(f"channel owners are: {channel['owners']} after removing")
    return {}






def get_user_name(u_id):
    data = get_data()
    for user in data['users']:
        if u_id == user['u_id']:
            return {user['name_first'], user['name_last']}
    return None
