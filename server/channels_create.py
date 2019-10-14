import data
'''
Very basic start to creating channels
'''



def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError("Name of channel is longer than 20 characters.")

    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    channel_id = len(data.CHANNELS_INFO) + 1

    # Create a new dictionary with the channel information and append to global variabe
    new_channel_dict = {'id': channel_id, 'name': name, 'is_public': is_public}
    data.CHANNELS_INFO.append(new_channel_dict)

    # return a dictionary of channel id
    return {'id': channel_id}

'''
test_dict = channels_create(1, "ONE", True)
test_dict2 = channels_create(1, "TWO", False)
test_dict3 = channels_create(1, "THREE", False)

print(data.CHANNELS_INFO)

def is_public(channel_id):
    for dict in data.CHANNELS_INFO:
        if dict.get('id') == channel_id:
            return dict.get('is_public')

    return False

print(is_public(test_dict['id']))
'''
