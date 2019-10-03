import pytest

'''
####################### ASSUMPTIONS ######################
Assume you need to need to create a channel first before joining
Also you cannot join a channel you are already in
Assume "Channel does not exist" means channels you have already joined OR
channel_id hasn't been created yet
'''


def channel_join(token, channel_id):
    if is_valid_channel(channel_id):
        pass
    else:
        raise ValueError("Channel ID does NOT Exist")
    pass


######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register("person1@gmail.com", "password", "person", "one")
token = userDict1['token']

##########################    END SETUP   ########################

# Testing joining a channel that hasn't been created yet
def test_channel_join_1():
    with pytest.raises(ValueError):
        channel_join(token, 1234)

# Testing joining a channel with a different id to one that has been created
def test_channel_join_2():
    channel_id = channels_create(token, "Name" True)
    invalid_channel_id = channel_id + 1
    with pytest.raises(ValueError):
        channel_join(token, invalid_channel_id)

# Testing joining a channel you have already joined
def test_channel_join_3():
    channel_id = channels_create(token, "Name" True)
    channel_join(token, channel_id)
    with pytest.raises(ValueError):
        channel_join(token, channel_id)

# Testing joining a different channel id to a list of already created channels
def test_channel_join_4():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    invalid_channel_id = channel_id1 + channel_id2 + channel_id3
    with pytest.raises(ValueError):
        channel_join(channels_create(token, invalid_channel_id)

# Testing joining a channel already joined in a list of channels
def test_channel_join_5():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_join(token, channel_id1)
    channel_join(token, channel_id2)
    channel_join(token, channel_id3)
    with pytest.raises(ValueError):
        channel_join(token, channel_id2)

# Testing joining a single channel already created
def test_channel_join_6():
    channel_id1 = channels_create(token, "Name" True)
    channel_join(token, channel_id)
    assert(channels_list(token) == [{'id': channel_id1, 'name': "Name"}])

# Testing joining only one channel out of a list of channels
def test_channel_join_7():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_join(token, channel_id2)
    assert(channels_list(token) == [{'id': channel_id2, 'name': "Second Channel"}])


# Testing joining multiple channels
def test_channel_join_8():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_join(token, channel_id2)
    channel_join(token, channel_id3)
    assert(channels_list(token) == [{'id': channel_id2, 'name': "Second Channel"},
                                     'id': channel_id3, 'name': "Third Channel"}])

# Testing joining all available channels
def test_channel_join_9():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_join(token, channel_id1)
    channel_join(token, channel_id2)
    channel_join(token, channel_id3)
    assert(channels_listall(token) == [{'id': channel_id1, 'name': "Channel Name"},
                                       {'id': channel_id2, 'name': "Second Channel"},
                                       {'id': channel_id3, 'name': "Third Channel"}])
