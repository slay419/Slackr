from .data import *



def channels_create(token, name, is_public):
    if len(name) > 20:
        return send_error("Name of channel is longer than 20 characters.")

    owner_id = decode_token(token)
    print(owner_id)
    get_user_name(owner_id)
    print(f"owner's name is: {get_user_name(owner_id)}")
    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    new_channel_id = len(data['channels']) + 1

    # Create a dictionary with all the relevant info and append to data
    dict = {
        'channel_id': new_channel_id, 'name': name, 'owners': [owner_id],
        'members': [], 'is_public': is_public
    }
    data['channels'].append(dict)
    print(data['channels'])
    return {
        'channel_id': new_channel_id
    }


def get_user_name(u_id):
    data = get_data()
    for user in data['users']:
        if u_id == user['u_id']:
            return {user['name_first'], user['name_last']}
    return None
