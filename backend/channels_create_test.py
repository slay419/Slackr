from auth_register_test     import auth_register
from channels_create        import channels_create
import pytest

'''
####################### ASSUMPTIONS #####################
The name of a channel should be at least one character long - you can't name a channel nothing?
The channel ID will increase in number if created late
e.g. channel_id1 created first will be lower than the channel_id2 created last
'''

######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['u_id']

##########################    END SETUP   ########################

# Testing channel name that is exactly 21 characters long and is public
def test_channels_create_1():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "nameOfChannelIs21Long", True)

# Testing channel name that is exactly 21 characters long and isprivate
def test_channels_create_2():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "nameOfChannelIs21Long", False)

# Testing channel name that is significantly longer than 20 and public
def test_channels_create_3():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "nameOfChannelThatIsDefinitelyTooLong", True)

# Testing channel name that is significantly longer than 20 and private
def test_channels_create_4():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "nameOfChannelThatIsDefinitelyTooLong", False)

# Testing channel name that is exactly 20 characters long and Public
def test_channels_create_5():
    channel_id = channels_create(owner_token, "nameOfChannelIs20xxx", True)

# Testing channel name that is exactly 20 characters long and Private
def test_channels_create_6():
    channel_id = channels_create(owner_token, "nameOfChannelIs20xxx", False)

# Testing channel name that is exactly 19 characters long and Public
def test_channels_create_7():
    channel_id = channels_create(owner_token, "nameOfChannelIs19xx", True)

# Testing channel name that is exactly 19 characters long and Private
def test_channels_create_8():
    channel_id = channels_create(owner_token, "nameOfChannelIs19xx", False)

# Testing numbers count as a character
def test_channels_create_8():
    channel_id = channels_create(owner_token, "123456789", True)

# Testing too many numbers will raise an error
def test_channels_create_9():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "1234567890123456789012345", True)

#T Testing symbols will count as a character
def test_channels_create_10():
    channel_id = channels_create(owner_token, "~!@#$%^&*()_-+=", False)

def test_channels_create_11():
    channel_id = channels_create(owner_token, "[]{}\|;:',./<>?", False)

# Testing space bar counts as a character
def test_channels_create_12():
    channel_id = channels_create(owner_token, "        ", True)

# Testing too many symbols will create an error
def test_channels_create_13():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", False)

# Testing a mix of letters and symbols
def test_channels_create_14():
    channel_id = channels_create(owner_token, "name123!@#", True)

# Testing a long string of letters and symbols
def test_channels_create_15():
    with pytest.raises(ValueError):
        channel_id = channels_create(owner_token, "VeryLongName123456!@#$%^@!#", True)

# Testing expected previous behaviour with a different token
def test_channels_create_16():
    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    different_token = userDict1['token']
    channel_id = channels_create(different_token, "Name123!@#", False)

# Testing long name with a different token
def test_channels_create_17():
    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    different_token = userDict1['token']
    with pytest.raises(ValueError):
        channel_id = channels_create(different_token, "VeryLongName123456!@#$^$", False)
