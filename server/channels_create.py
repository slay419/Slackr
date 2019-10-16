from data import get_users, get_channels
'''
Very basic start to creating channels
'''



def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError("Name of channel is longer than 20 characters.")

    users = get_users()

    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    channel_list = get_channels()
    channel_id = len(channel_list) + 1
    # Create a new dictionary with the channel info and append to global variable
    dict = {'channel_id': channel_id, 'name': name, 'is_public': is_public}
    channel_list.append(dict)

    return {'channel_id': channel_id}


'''

print(get_channels())
test_dict = channels_create(1, "ONE", True)
print(get_channels())
test_dict2 = channels_create(1, "TWO", False)
print(get_channels())
test_dict3 = channels_create(1, "THREE", False)

print(get_channels())
'''
'''

print(data.CHANNELS_INFO)

def is_public(channel_id):
    for dict in data.CHANNELS_INFO:
        if dict.get('id') == channel_id:
            return dict.get('is_public')

    return False

print(is_public(test_dict['id']))
'''
