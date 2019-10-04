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
owner_id = ownerDict['id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['id']

##########################    END SETUP   ########################

# Empty list of channels if none have been created yet
def test_channels_listall_1():
    assert(channels_listall(u_token) == [{}])

# List with one dictionary only if only one channel has been created
def test_channels_listall_2():
    channel_id1 = channels_create(owner_token, "Name", True)
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name"}])

# List of dictionaries with 2 channels created assuming order of channel_id
def test_channels_listall_2():
    channel_id1 = channels_create(owner_token, "Name1", True)
    channel_id2 = channels_create(owner_token, "Name2", True)
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                       {'id': channel_id2, 'name': "Name2"}])

# List of dictionaries with 3 channels created assuming order of channel_id
def test_channels_listall_3():
    channel_id1 = channels_create(owner_token, "Name1", True)
    channel_id2 = channels_create(owner_token, "Name2", True)
    channel_id3 = channels_create(owner_token, "Name3", True)
    assert(channels_listall(u_token) == [{'id': channel_id1, 'name': "Name1"},
                                       {'id': channel_id2, 'name': "Name2"},
                                       {'id': channel_id3, 'name': "Name3"}])
