from .data import *


def channels_create(token, name, is_public):
    #if not is_logged_in(token):
    #    return f"User: {decode_token(token)} not logged in"
    if len(name) > 20:
        return "Name of channel is longer than 20 characters"
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
        'owners': [{
            'u_id': owner_id,
            'name_first': get_first_name(owner_id),
            'name_last': get_last_name(owner_id)
        }],
        'members': [{
            'u_id': owner_id,
            'name_first': get_first_name(owner_id),
            'name_last': get_last_name(owner_id)
        }],
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
    #if not is_logged_in(token):
    #    return f"User: {decode_token(token)} is not logged in"
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
    #if not is_logged_in(token):
    #    return f"User: {decode_token(token)} is not logged in"

    data = get_data()
    u_id = decode_token(token)
    channels_list = []
    for channels in data['channels']:
        if is_member(u_id, channels['channel_id']) or is_owner(u_id, channels['channel_id']):
            channels_list.append({
                'channel_id': channels['channel_id'],
                'name': channels['name']
            })
    return channels_list


def channel_leave(token, channel_id):
    if not is_logged_in(token):
        return f"User: {decode_token(token)} is not logged in"
    if not is_joined(token, channel_id):
        return f"User: {decode_token(token)} has not joined channel: {channel_id} yet"
    if not is_valid_channel(channel_id):
        return f"Channel ID: {channel_id} is invalid"

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
    if not is_logged_in(token):
        return f"User: {decode_token(token)} is not logged in"
    #if not is_logged_in(generate_token(u_id)):
    #    return ff"User: {u_id} is not logged in"
    if not is_valid_channel(channel_id):
        return f"Channel ID: {channel_id} is invalid"
    if is_owner(u_id, channel_id):
        return f"User: {u_id} is already an owner"
    if not is_owner(decode_token(token), channel_id):
        return f"User: {decode_token(token)} does not have privileges to promote others"

    channel = channel_dict(channel_id)
    print(f"channel owners are: {channel['owners']}")
    # append user to list of owners
    channel['owners'].append(u_id)
    print(f"channel owners are: {channel['owners']} after appending")
    return {}


def channel_removeowner(token, channel_id, u_id):
    if not is_logged_in(token):
        return f"User: {decode_token(token)} is not logged in"
    #if not is_logged_in(generate_token(u_id)):
    #    return ff"User: {u_id} is not logged in"
    if not is_valid_channel(channel_id):
        return f"Channel ID: {channel_id} is invalid"
    if not is_owner(u_id, channel_id):
        return f"User: {u_id} is not an owner"
    if not is_owner(decode_token(token), channel_id):
        return f"User: {decode_token(token)} does not have privileges to demote others"

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
