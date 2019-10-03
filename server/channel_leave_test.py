
import pytest

'''
####################### ASSUMPTIONS ######################
Assume you need to have joined the channel first before leaving
Assume "Channel does not exist" means channels you have not joined yet
'''

def channel_leave(token, channel_id):
    if is_valid_channel(channel_id):
        pass
    elif:
        raise ValueError("Channel ID does NOT Exist")
    pass

# Returns 1 if the channel id exists and is valid
# Returns 0 if the channel id does not exist and is invalid
def is_valid_channel(channel_id):
    pass:


######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register("person1@gmail.com", "password", "person", "one")
token = userDict1['token']

##########################    END SETUP   ########################


# Leaving a channel that has not been created yet
def test_channel_leave_1():
    with pytest.raises(ValueError):
        channel_leave(token, 1234)

# Leaving a channel that has been created but not joined
def test_channel_leave_2():
    channel_id1 = channels_create(token1, "Channel Name", True)
    with pytest.raises(ValueError):
        channel_leave(token, channel_id1)

# Leaving a non-matching channel that been created and joined
def test_channel_leave_3():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_join(token, channel_id1)
    invalid_channel_id = channel_id1 + 1
    with pytest.raises(ValueError):
        channel_leave(token, invalid_channel_id)

# Leaving a channel that hasn't been joined
def test_channel_leave_4():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_join(token, channel_id1)
    channel_join(token, channel_id2)
    with pytest.raises(ValueError):
        channel_leave(token, channel_id3)


# Leaving an invalid channel not matching any from a list of joined channels
def test_channel_list_5():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_join(token, channel_id1)
    channel_join(token, channel_id2)
    channel_join(token, channel_id3)
    invalid_channel_id = channel_id1 + channel_id2 + channel_id3
    with pytest.raises(ValueError):
        channel_leave(token, invalid_channel_id)

# Leaving the only channel they have joined would return empty list
def test_channel_leave_6():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_join(token, channel_id1)
    channel_leave(token, channel_id1)
    assert(channels_list(token) == [{}])

# Leaving a channel out of 2 already joined
def test_channel_leave_7():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_join(token, channel_id1)
    channel_join(token, channel_id2)
    channel_leave(token, channel_id1)
    assert(channels_list(token) == [{'id': channel_id2, 'name': "Second Channel"}])

# Leaving a channel out of 4 already joined
def test_channel_leave_8():
    channel_id1 = channels_create(token1, "Channel Name", True)
    channel_id2 = channels_create(token2, "Second Channel", True)
    channel_id3 = channels_create(token3, "Third Channel", True)
    channel_id4 = channels_create(token3, "Fourth Channel", True)
    channel_join(token, channel_id1)
    channel_join(token, channel_id2)
    channel_join(token, channel_id3)
    channel_join(token, channel_id4)
    channel_leave(token, channel_id3)
    assert(channels_list(token) == [{'id': channel_id1, 'name': "Channel Name"},
                                     'id': channel_id2, 'name': "Second Channel"},
                                     'id': channel_id4, 'name': "Fourth Channel"}])
