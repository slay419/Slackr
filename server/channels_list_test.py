from auth_register_test         import auth_register
from auth_login_test            import auth_login
from channels_create_test       import channels_create
from channels_join_test         import channels_join

import pytest

'''
####################### ASSUMPTIONS #####################
Assume the order of the list of dictionaries is in ascending order of channel_id
NOT the order joined

Assume the person creating the channel is already an owner and joined the channel
'''

# Provide a list of all channels (and their associated details) that the authorised user is part of
def channels_list(token):
    pass # return {channels} # list of dictionary with {id: ' ', name: ' '}


######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
ownerLogin = auth_login("owner@gmail.com", "password")
owner_token = ownderDict['token']
owner_id = ownerDict['u_id']

ownerDict2 = auth_register("owner2@gmail.com", "password", "owner2", "privileges")
ownerLogin2 = auth_login("owner2@gmail.com", "password")
owner_token2 = ownderDict['token']
owner_id2 = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
userLogin = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']
u_id = userDict1['u_id']

##########################    END SETUP   ########################


# Testing function returns empty list of channels if none have been created yet
def test_channels_list_1():
    assert(channels_list(u_token) == [{}])

# Empty list of channels if some have been created but not joined yet
def test_channels_list_2():
    channel1 = channels_create(owner_token, "Name", True)
    assert(channels_list(u_token) == [{}])

# Testing function still returns empty list of channels if multiple channels created
# but not joined
def test_channels_list_3():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    assert(channels_list(u_token) == [{}])


# Testing single list of channels if one has been created and joined
def test_channel_list_4():
    channel1 = channels_create(owner_token, "Name", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name"}])

# Expecting single list of channels if multiple have been created, but joined only one
def test_channel_list_5():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_join(u_token, channel_id1)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name1"}])

# Expecting only a few list of channels to be returned if not all have been joined
def test_channel_list_6():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                      {'id': channel_id2, 'name': "Name2"}])

# Expecting all channels to be returned if all have been created and joined
def test_channel_list_7():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                      {'id': channel_id2, 'name': "Name2"},
                                      {'id': channel_id3, 'name': "Name3"}])


# Expecting the list of channels to be in order of channel_id, ignoring the order
# it was joined in
def test_channel_list_8():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner_token, "Name2", True)
    channel3 = channels_create(owner_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id3)
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                      {'id': channel_id2, 'name': "Name2"},
                                      {'id': channel_id3, 'name': "Name3"}])

# Testing joining channels created by multiple owners
def test_channel_list_9():
    channel1 = channels_create(owner_token, "Name1", True)
    channel2 = channels_create(owner2_token, "Name2", True)
    channel3 = channels_create(owner2_token, "Name3", True)
    channel_id1 = channel1['channel_id']
    channel_id2 = channel2['channel_id']
    channel_id3 = channel3['channel_id']
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                      {'id': channel_id2, 'name': "Name2"}])
