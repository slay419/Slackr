from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
Assume the order of the list of dictionaries is in ascending order of channel_id
NOT the order joined

Assume the person creating the channel is already an owner and joined the channel
'''


# Testing function returns empty list of channels if none have been created yet
def test_channels_list_1():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    assert(channels_list(u_token) == {
        'channels': []
    })

# Empty list of channels if some have been created but not joined yet
def test_channels_list_2():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name", True)
    assert(channels_list(u_token) == {
        'channels': []
    })

# Testing function still returns empty list of channels if multiple channels created
# but not joined
def test_channels_list_3():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    assert(channels_list(u_token) == {
        'channels': []
    })


# Testing single list of channels if one has been created and joined
def test_channel_list_4():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name"}
        ]
    })

# Expecting single list of channels if multiple have been created, but joined only one
def test_channel_list_5():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"}
        ]
    })

# Expecting only a few list of channels to be returned if not all have been joined
def test_channel_list_6():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"}
        ]
    })

# Expecting all channels to be returned if all have been created and joined
def test_channel_list_7():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"},
            {'channel_id': channel_id3, 'name': "Name3"}
        ]
    })


# Expecting the list of channels to be in order of channel_id, ignoring the order
# it was joined in
def test_channel_list_8():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id3)
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"},
            {'channel_id': channel_id3, 'name': "Name3"}
        ]
    })

# Testing joining channels created by multiple owners
def test_channel_list_9():
    ######################## GLOBAL VARIABLES SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
    owner_token2 = ownerDict['token']
    owner_id2 = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']
    ##########################    END SETUP   ########################

    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token2, "Name2", True)
    channel3 = channels_create(owner_token2, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"}
        ]
    })
