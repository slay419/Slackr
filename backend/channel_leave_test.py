from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list, channel_leave
from functions.misc_functions import admin_userpermission_change

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS ######################
Assume you need to have joined the channel first before leaving
Assume "Channel does not exist" means channels you have not joined yet OR
channel_id hasn't been created yet
'''


######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownerDict['token']
owner_id = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict['token']
u_id = userDict['u_id']

# Assume no channels have been created yet

##########################    END SETUP   ########################


# Leaving a channel that has not been created yet
def test_channel_leave_1():
    reset_channels()
    with pytest.raises(ValueError):
        channel_leave(u_token, 1234)

# Leaving a channel that has been created but not joined
def test_channel_leave_2():
    reset_channels()
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    with pytest.raises(ValueError):
        channel_leave(u_token, channel_id)

# Leaving a non-matching channel that been created and joined
def test_channel_leave_3():
    reset_channels()
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    invalid_channel_id = channel_id1 + 1
    with pytest.raises(ValueError):
        channel_leave(u_token, invalid_channel_id)

# Leaving a channel that hasn't been joined
def test_channel_leave_4():
    reset_channels()
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel2 = channels_create(owner_token, "Second Channel", True)
    channel3 = channels_create(owner_token, "Third Channel", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    with pytest.raises(ValueError):
        channel_leave(u_token, channel_id3)


# Leaving an invalid channel not matching any from a list of joined channels
def test_channel_list_5():
    reset_channels()
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
    reset_channels()
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    channel_leave(u_token, channel_id1)
    assert(channels_list(u_token) == {
        'channels': []
    })

# Leaving a channel out of 2 already joined
def test_channel_leave_7():
    reset_channels()
    channel1 = channels_create(owner_token, "Channel Name", True)
    channel2 = channels_create(owner_token, "Second Channel", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_leave(u_token, channel_id1)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id2, 'name': "Second Channel"}
        ]
    })

# Leaving a channel out of 4 already joined
def test_channel_leave_8():
    reset_channels()
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
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Channel Name"},
            {'channel_id': channel_id2, 'name': "Second Channel"},
            {'channel_id': channel_id4, 'name': "Fourth Channel"}
        ]
    })  
