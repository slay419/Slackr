from auth_register_test         import auth_register
from channels_create_test       import channels_create
from channels_join_test         import channels_join
from channels_list_test         import channels_list

import pytest

'''
####################### ASSUMPTIONS ######################
Assume you need to have joined the channel first before leaving
Assume "Channel does not exist" means channels you have not joined yet OR
channel_id hasn't been created yet
'''

def channel_leave(token, channel_id):
    if is_valid_channel(channel_id):
        pass
    else:
        raise ValueError("Channel ID does NOT Exist")
    pass

'''
Returns 1 if the channel id exists and is valid
Returns 0 if the channel id does not exist and is invalid
'''
def is_valid_channel(channel_id):
    pass


######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['u_id']

# Assume no channels have been created yet

##########################    END SETUP   ########################


# Leaving a channel that has not been created yet
def test_channel_leave_1():
    with pytest.raises(ValueError):
        channel_leave(u_token, 1234)

# Leaving a channel that has been created but not joined
def test_channel_leave_2():
    channel1 = channels_create(owner_token, "Channel Name", True)
    with pytest.raises(ValueError):
        channel_leave(u_token, channel_id1)

# Leaving a non-matching channel that been created and joined
def test_channel_leave_3():
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    invalid_channel_id = channel_id1 + 1
    with pytest.raises(ValueError):
        channel_leave(u_token, invalid_channel_id)

# Leaving a channel that hasn't been joined
def test_channel_leave_4():
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel2 = channels_create(owner_token, "Second Channel", True)
    channel3 = channels_create(owner_token, "Third Channel", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    with pytest.raises(ValueError):
        channel_leave(u_token, channel_id3)


# Leaving an invalid channel not matching any from a list of joined channels
def test_channel_list_5():
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel2 = channels_create(owner_token, "Second Channel", True)
    channel3 = channels_create(owner_token, "Third Channel", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    invalid_channel_id = channel_id1 + channel_id2 + channel_id3
    with pytest.raises(ValueError):
        channel_leave(u_token, invalid_channel_id)

# Leaving the only channel they have joined would return empty list
def test_channel_leave_6():
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    channel_leave(u_token, channel_id1)
    assert(channels_list(u_token) == [{}])

# Leaving a channel out of 2 already joined
def test_channel_leave_7():
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel2 = channels_create(owner_token, "Second Channel", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_leave(u_token, channel_id1)
    assert(channels_list(u_token) == [{'id': channel_id2, 'name': "Second Channel"}])

# Leaving a channel out of 4 already joined
def test_channel_leave_8():
    channel1= channels_create(owner_token, "Channel Name", True)
    channel2 = channels_create(owner_token, "Second Channel", True)
    channel3 = channels_create(owner_token, "Third Channel", True)
    channel4 = channels_create(owner_token, "Fourth Channel", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_id4 = channel4['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    channel_join(u_token, channel_id4)
    channel_leave(u_token, channel_id3)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Channel Name"},
                                      {'id': channel_id2, 'name': "Second Channel"},
                                      {'id': channel_id4, 'name': "Fourth Channel"}])
