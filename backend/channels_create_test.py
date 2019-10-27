from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
The name of a channel should be at least one character long - you can't name a channel nothing?
The channel ID will increase in number if created late
e.g. channel_id1 created first will be lower than the channel_id2 created last
'''

######################## GLOBAL VARIABLES SETUP ######################
reset_data()
ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownerDict['token']
owner_id = ownerDict['u_id']

##########################    END SETUP   ########################

# Testing channel name that is exactly 21 characters long and is public
def test_channels_create_1():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "nameOfChannelIs21Long", True)

# Testing channel name that is exactly 21 characters long and isprivate
def test_channels_create_2():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "nameOfChannelIs21Long", False)

# Testing channel name that is significantly longer than 20 and public
def test_channels_create_3():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "nameOfChannelThatIsDefinitelyTooLong", True)

# Testing channel name that is significantly longer than 20 and private
def test_channels_create_4():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "nameOfChannelThatIsDefinitelyTooLong", False)

# Testing channel name that is exactly 20 characters long and Public
def test_channels_create_5():
    reset_channels()
    new_channel = channels_create(owner_token, "nameOfChannelIs20xxx", True)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "nameOfChannelIs20xxx",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': True,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing channel name that is exactly 20 characters long and Private
def test_channels_create_6():
    reset_channels()
    new_channel = channels_create(owner_token, "nameOfChannelIs20xxx", False)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "nameOfChannelIs20xxx",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': False,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing channel name that is exactly 19 characters long and Public
def test_channels_create_7():
    reset_channels()
    new_channel = channels_create(owner_token, "nameOfChannelIs19xx", True)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "nameOfChannelIs19xx",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': True,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing channel name that is exactly 19 characters long and Private
def test_channels_create_8():
    reset_channels()
    new_channel = channels_create(owner_token, "nameOfChannelIs19xx", False)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "nameOfChannelIs19xx",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': False,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing numbers count as a character
def test_channels_create_8():
    reset_channels()
    new_channel = channels_create(owner_token, "123456789", True)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "123456789",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': True,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing too many numbers will raise an error
def test_channels_create_9():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "1234567890123456789012345", True)

#T Testing symbols will count as a character
def test_channels_create_10():
    reset_channels()
    new_channel = channels_create(owner_token, "~!@#$%^&*()_-+=", False)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "~!@#$%^&*()_-+=",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': False,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

def test_channels_create_11():
    reset_channels()
    new_channel = channels_create(owner_token, "[]{}\|;:',./<>?", False)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "[]{}\|;:',./<>?",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': False,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing space bar counts as a character
def test_channels_create_12():
    reset_channels()
    new_channel = channels_create(owner_token, "        ", True)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "        ",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': True,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing too many symbols will create an error
def test_channels_create_13():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", False)

# Testing a mix of letters and symbols
def test_channels_create_14():
    reset_channels()
    new_channel = channels_create(owner_token, "name123!@#", True)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "name123!@#",
        'owner_members': [{
            'u_id': decode_token(owner_token),
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'all_members': [{
            'u_id': owner_id,
            'name_first': "owner",
            'name_last': "privileges"
        }],
        'is_public': True,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing a long string of letters and symbols
def test_channels_create_15():
    reset_channels()
    with pytest.raises(ValueError):
        new_channel = channels_create(owner_token, "VeryLongName123456!@#$%^@!#", True)

# Testing expected previous behaviour with a different token
def test_channels_create_16():
    reset_channels()
    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    different_token = userDict['token']
    new_channel = channels_create(different_token, "Name123!@#", False)
    channel_id = new_channel['channel_id']
    channel = channel_dict(channel_id)
    assert(new_channel == {
        'channel_id': channel_id
    })
    assert(channel == {
        'channel_id': channel_id,
        'name': "Name123!@#",
        'owner_members': [{
            'u_id': userDict['u_id'],
            'name_first': "person",
            'name_last': "one"
        }],
        'all_members': [{
            'u_id': userDict['u_id'],
            'name_first': "person",
            'name_last': "one"
        }],
        'is_public': False,
        'messages': [],
        'standup_queue': [],
        'standup_active': False
    })

# Testing long name with a different token
def test_channels_create_17():
    reset_channels()
    userDict = auth_register("person2@gmail.com", "password", "person", "one")
    different_token = userDict['token']
    with pytest.raises(ValueError):
        new_channel = channels_create(different_token, "VeryLongName123456!@#$^$", False)

# Testing creating multiple public channels - channel_id should be increasing order
def test_channels_create_18():
    reset_channels()
    new_channel1 = channels_create(owner_token, "Channel 1", True)
    new_channel2 = channels_create(owner_token, "Channel 2", True)
    new_channel3 = channels_create(owner_token, "Channel 3", True)
    assert(new_channel1 == {
        'channel_id': 1
    })
    assert(new_channel2 == {
        'channel_id': 2
    })
    assert(new_channel3 == {
        'channel_id': 3
    })

# Testing creating multiple private channels - channel_id should be increasing order
def test_channels_create_19():
    reset_channels()
    new_channel1 = channels_create(owner_token, "Channel 1", False)
    new_channel2 = channels_create(owner_token, "Channel 2", False)
    new_channel3 = channels_create(owner_token, "Channel 3", False)
    assert(new_channel1 == {
        'channel_id': 1
    })
    assert(new_channel2 == {
        'channel_id': 2
    })
    assert(new_channel3 == {
        'channel_id': 3
    })

# Testing creating multiple public & private channels - channel_id should be increasing order
def test_channels_create_20():
    reset_channels()
    new_channel1 = channels_create(owner_token, "Channel 1", True)
    new_channel2 = channels_create(owner_token, "Channel 2", False)
    new_channel3 = channels_create(owner_token, "Channel 3", True)
    new_channel4 = channels_create(owner_token, "Channel 4", False)
    assert(new_channel1 == {
        'channel_id': 1
    })
    assert(new_channel2 == {
        'channel_id': 2
    })
    assert(new_channel3 == {
        'channel_id': 3
    })
    assert(new_channel4 == {
        'channel_id': 4
    })
