import pytest

'''
####################### ASSUMPTIONS #####################
Assume the order of the list of dictionaries is in ascending order of channel_id
'''

# Provide a list of all channels (and their associated details)
def channels_listall(token):
    pass # return {channels}  # list of dictionary with {id: ' ', name: ' '}

######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register("person1@gmail.com", "password", "person", "one")
token = userDict1['token']

##########################    END SETUP   ########################

# Empty list of channels if none have been created yet
def test_channels_listall_1():
    assert(channels_listall(token) == [{}])

# List with one dictionary only if only one channel has been created
def test_channels_listall_2():
    channel_id1 = channels_create(token, "Name", True)
    assert(channels_listall(token) == [{'id': channel_id1, 'name': "Name"}])

# List of dictionaries with 3 channels created assuming order of channel_id
def test_channels_listall_3():
    channel_id1 = channels_create(token, "Name1", True)
    channel_id2 = channels_create(token, "Name2", True)
    channel_id3 = channels_create(token, "Name3", True)
    assert(channels_listall(token) == [{'id': channel_id1, 'name': "Name1"},
                                       {'id': channel_id2, 'name': "Name2"},
                                       {'id': channel_id3, 'name': "Name3"}
                                      ])

# List of dictionaries with 2 channels, ensuring ascending order of channel_id
def test_channels_listall_4():
    bigger_id = channels_create(token, "Name1", True)
    smaller_id = channels_create(token "Name2", True)
    assert(channels_listall(token) == [{'id': smaller_id, 'name': "Name2"},
                                       {'id': bigger_id, 'name': "Name1"}
                                       ])
