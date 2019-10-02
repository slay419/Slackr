import pytest

'''
-----------------ASSUMPTIONS--------------------
The name of a channel should be at least one character long - you can't name a channel nothing?
'''



'''
auth_register(email, password, name_first, name_last)
'''

def channels_create(token, name, is_public):
    if len(name) > 20:
        raise ValueError("Name of channel is longer than 20 characters.")
    return channel_id


# BEGIN SETUP

userDict1 = auth_register("person1@gmail.com", "password", "person", "one")
token = userDict1['token']

userDict2 = auth_register("person2@gmail.com", "password", "person", "two")
differentToken = userDict2['token']


# END SETUP


'''
 Testing exception cases with names greater than 20 characters
'''

# Testing channel name that is exactly 21 characters long and is public
def test_channels_create_1(token):
    with pytest.raises(ValueError):
        channels_create(token, "nameOfChannelIs21Long", True)

# Testing channel name that is exactly 21 characters long and isprivate
def test_channels_create_2(token):
    with pytest.raises(ValueError):
        channels_create(token, "nameOfChannelIs21Long", False)

# Testing channel name that is significantly longer than 20 and public
def test_channels_create_3(token):
    with pytest.raises(ValueError):
        channels_create(token, "nameOfChannelThatIsDefinitelyTooLong", True)

# Testing channel name that is significantly longer than 20 and private
def test_channels_create_4(token):
    with pytest.raises(ValueError):
        channels_create(token, "nameOfChannelThatIsDefinitelyTooLong", False)

'''
####################################################################
NEED TO DOUBLE CHECK THIS PART BECAUSE THEY DO NOT RAISE ANY ERRORS
###################################################################
'''
# Testing channel name that is exactly 20 characters long and Public
def test_channels_create_5(token):
    channels_create(token, "nameOfChannelIs20xxx", True)

# Testing channel name that is exactly 20 characters long and Private
def test_channels_create_6(token):
    channels_create(token, "nameOfChannelIs20xxx", False)

'''
Testing channel names that are random symbols/numbers - not just characters
'''
# Testing numbers count as a character
def test_channels_create_7(token):
    channels_create(token, "123456789", True)

# Testing too many numbers will raise an error
def test_channels_create_8(token):
    with pytest.raises(ValueError):
        channels_create(token, "1234567890123456789012345", True)

#T Testing symbols will count as a character
def test_channels_create_9(token):
    channels_create(token, "~!@#$%^&*()_-+=", False)

def test_channels_create_10(token):
    channels_create(token, "[]{}\|;:',./<>?", False)

# Testing space bar counts as a character
def test_channels_create_11(token):
    channels_create(tokenm "        ", True)

# Testing too many symbols will create an error
def test_channels_create_12(token):
    with pytest.raises(ValueError):
        channels_create(token, "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", False)

# Testing a mix of letters and symbols
def test_channels_create_13(token):
    channels_create(token, "name123!@#", True)

# Testing a long string of letters and symbols
def test_channels_create_14(token):
    with pytest.raises(ValueError):
        channels_create(token, "VeryLongName123456!@#$%^@!#", True)

# Testing expected previous behaviour with a different token
def test_channels_create_15(differentToken):
    channels_create(differentToken, "Name123!@#", False)

# Testing long name with a different token
def test_channels_create_16(differentToken):
    with pytest.raises(ValueError):
        channels_create(differentToken, "VeryLongName123456!@#$^$", False)
