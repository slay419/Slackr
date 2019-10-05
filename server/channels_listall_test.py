from auth_register_test         import auth_register
from channels_create_test       import channels_create
from channels_join_test         import channels_join

import pytest

'''
####################### ASSUMPTIONS #####################
Assume the order of the list of dictionaries is in ascending order of channel_id
i.e. order of channel_id created
'''

# Provide a list of all channels (and their associated details)
def channels_listall(token):
    pass # return {channels}  # list of dictionary with {id: ' ', name: ' '}

######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['u_id']

ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
owner_token2 = ownderDict['token']
owner_id2 = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['u_id']

##########################    END SETUP   ########################

# Empty list of channels if none have been created yet
def test_channels_listall_1():
    assert(channels_listall(u_token) == [{}])

# List with one dictionary only if only one channel has been created
def test_channels_listall_2():
    channel1 = channels_create(owner_token, "Name", True)
    channel_id1 = channel1['channel_id']
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name"}])

# List of dictionaries with 2 channels created assuming order of channel_id
def test_channels_listall_2():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                         {'id': channel_id2, 'name': "Name2"}])

# List of dictionaries with 3 channels created assuming order of channel_id
def test_channels_listall_3():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                         {'id': channel_id2, 'name': "Name2"},
                                         {'id': channel_id3, 'name': "Name3"}])

# Testing the owner of the channel should also have the same list_all output as
# a member
def test_channels_listall_4():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    assert(channels_listall(owner_token) == [{'id': channel_id1, 'name': "Name1"},
                                             {'id': channel_id2, 'name': "Name2"},
                                             {'id': channel_id3, 'name': "Name3"}])

# Testing list should still be the same after joining a few
def test_channels_listall5():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                         {'id': channel_id2, 'name': "Name2"},
                                         {'id': channel_id3, 'name': "Name3"}])

# Testing function lists all the channels created by different owners and are
# the same for different users
def test_channels_listall_6():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token2, "Name3", True)
    channel4 = channels_create(owner_token2, "Name4", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_id4 = channel4['channel_id']
    assert(channels_listall(owner_token) == [{'id': channel_id1, 'name': "Name1"},
                                             {'id': channel_id2, 'name': "Name2"},
                                             {'id': channel_id3, 'name': "Name3"}
                                             {'id': channel_id4, 'name': "Name4"}])
    assert(channels_listall(owner_token) == channels_listall(owner_token2))
    assert(channels_listall(owner_token) == channels_listall(u_token))
