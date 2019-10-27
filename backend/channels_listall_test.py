from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_listall

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
Assume the order of the list of dictionaries is in ascending order of channel_id
i.e. order of channel_id created
'''



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

# Empty list of channels if none have been created yet
def test_channels_listall_1():
    reset_channels()
    assert(channels_listall(u_token) == {
        'channels': []
    })

# List with one dictionary only if only one channel has been created
def test_channels_listall_2():
    reset_channels()
    channel1 = channels_create(owner_token, "Name", True)
    channel_id1 = channel1['channel_id']
    assert(channels_listall(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name"}
        ]
    })

# List of dictionaries with 2 channels created assuming order of channel id
def test_channels_listall_3():
    reset_channels()
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    assert(channels_listall(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"}
        ]
    })

# List of dictionaries with 3 channels created assuming order of channel id
def test_channels_listall_4():
    reset_channels()
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    assert(channels_listall(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"},
            {'channel_id': channel_id3, 'name': "Name3"}
        ]
    })

# Testing the owner of the channel should also have the same list_all output as
# a member
def test_channels_listall_5():
    reset_channels()
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    assert(channels_listall(owner_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"},
            {'channel_id': channel_id3, 'name': "Name3"}
        ]
    })

# Testing list should still be the same after joining a few
def test_channels_listall_6():
    reset_channels()
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_listall(u_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"},
            {'channel_id': channel_id3, 'name': "Name3"}
        ]
    })


# Testing function lists all the channels created by different owners and are
# the same for different users
def test_channels_listall_7():
    reset_channels()
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token2, "Name3", True)
    channel4 = channels_create(owner_token2, "Name4", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_id4 = channel4['channel_id']
    assert(channels_listall(owner_token) == {
        'channels': [
            {'channel_id': channel_id1, 'name': "Name1"},
            {'channel_id': channel_id2, 'name': "Name2"},
            {'channel_id': channel_id3, 'name': "Name3"},
            {'channel_id': channel_id4, 'name': "Name4"}
        ]
    })
    assert(channels_listall(owner_token) == channels_listall(owner_token2))
    assert(channels_listall(owner_token) == channels_listall(u_token))
