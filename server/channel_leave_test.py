
import pytest

'''
####################### ASSUMPTIONS ######################
Assume you need to have joined the channel first before leaving
'''

def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError("Name of channel is longer than 20 characters.")
    return channel_id

'''
ValueError when:
    Channel (based on ID) does not exist
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


###########################     TESTS     #####################################


# Leaving a channel that has not been created yet
def test_channel_leave_1():
    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    token = userDict1['token']
    with pytest.raises(ValueError):
        channel_leave(token, 1234)


#######################     BEGIN SETUP     #########################

userDict1 = auth_register("person1@gmail.com", "password", "person", "one")
token1 = userDict1['token']
channel_id1 = channels_create(token1, "Channel Name", True)

userDict2 = auth_register("person2@gmail.com", "password", "person", "two")
token2 = userDict2['token']
channel_id2 = channels_create(token2, "Second Channel", True)

userDict3 = auth_register("person2@gmail.com", "password", "person", "three")
token3 = userDict2['token']
channel_id3 = channels_create(token3, "Third Channel", True)

#######################     END SETUP     #########################

# Leaving a channel different to one that has already been created
def test_channel_leave_2():
    invalid_channel_id = channel_id1 + channel_id2 + channel_id3
    with pytest.raises(ValueError):
        channel_leave(token, different_channel_id)




    ###     TEST USING CHANNELS_LIST ASSERT












#
