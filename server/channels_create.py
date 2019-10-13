import config
'''
Very basic start to creating channels
'''



def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError("Name of channel is longer than 20 characters.")

    # Give the channel an ID which corresponds to the number created e.g. 1st channel is ID1 ...
    channel_id = len(config.GLOBAL_CHANNELS) + 1
    channel_dict = {'id': channel_id}
    # Create a new dict with name field to append to global variable
    new_dict = channel_dict
    new_dict.update({'name': name})
    # append dictionary to a global variable
    config.GLOBAL_CHANNELS.append(new_dict)

    return channel_dict
'''
print(config.GLOBAL_CHANNELS)
test_dict = channels_create(1, "Testing Name", True)
print(config.GLOBAL_CHANNELS)
test_dict = channels_create(1, "Testing Name2", True)
print(config.GLOBAL_CHANNELS)
'''
