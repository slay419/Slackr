#pylint: disable=missing-docstring
#pylint: disable=unused-variable
import pytest

from functions.auth_functions import auth_register
from functions.channel_functions import channels_create
from functions.misc_functions import standup_send, standup_start

from functions.data import reset_data

from functions.exceptions import ValueError, AccessError


'''
####################### ASSUMPTIONS ######################
Assume the time is returned as a 'datetime' object
Assume creating a channel immediatly causes the creator to join
Assume there is no permission required to start a standup
Assume you cannot have two standups running at the same time on the same channel

Assume standup_start will have been successfully called
Assume the message is not empty and will return a ValueError
Assume "time_left" can retrieve the date_time object from standup_start
'''

######################## GLOBAL VARIABLES SETUP ######################
def setup():
    reset_data()
    # First user
    owner_dict1 = auth_register("person1@gmail.com", "password", "firstname", "lastname")
    owner_token = owner_dict1['token']

    # Second user
    user_dict1 = auth_register("person2@gmail.com", "password123", "firstname", "lastname")
    u_token = user_dict1['token']

    return owner_token, u_token
##########################    END SETUP   ########################

# Test for a channel that does not exist
def test_standup_send_1():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    with pytest.raises(ValueError):
        standup_send(owner_token, channel_id1 + 1, "Hey Lets start the standup")

# Test for a message with 1001 characters
def test_standup_send_2():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    with pytest.raises(ValueError):
        standup_send(owner_token, channel_id1, 1001*"A")

# Test for a message with 1000 characters
def test_standup_send_3():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    standup_send(owner_token, channel_id1, 1000*"A")

# Test for a message with 999 characters
def test_standup_send_4():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    standup_send(owner_token, channel_id1, 999*"A")

# Test for an empty message
def test_standup_send_5():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    with pytest.raises(ValueError):
        standup_send(owner_token, channel_id1, "")

# Test for starting a standup on a channel the user is not part of
def test_standup_send_6():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    with pytest.raises(AccessError):
        standup_send(u_token, channel_id1, "Hey Lets start the standup")

# Test for starting a standup on a channel the user is not part of
def test_standup_send_7():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    with pytest.raises(AccessError):
        standup_send(u_token, channel_id1, "Hey Lets start the standup")


# Test for sending a message when the standup has ended
def test_standup_send_8():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    with pytest.raises(ValueError):
        standup_send(owner_token, channel_id1, "Hey Lets start the standup")

# Test for sending a message when there is no standup
def test_standup_send_9():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    with pytest.raises(ValueError):
        standup_send(owner_token, channel_id1, "Hey Lets start the standup")

# Test for a normal message
def test_standup_send_10():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    standup_send(owner_token, channel_id1, "Hey Lets start the standup")
