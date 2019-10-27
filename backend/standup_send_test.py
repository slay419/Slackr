from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change, standup_send, standup_start
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail

from functions.data import *

import pytest

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
reset_data()
# First user
ownerDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
owner_token = ownerDict['token']

# Second user
userDict = auth_register("person2@gmail.com", "password123", "firstname", "lastname")
u_token = userDict['token']

##########################    END SETUP   ########################

# Test for a channel that does not exist
def test_standup_send_1():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	with pytest.raises(ValueError):
		standup_send(owner_token, channel_id1 + 1, "Hey Lets start the standup")

# Test for a message with 1001 characters
def test_standup_send_2():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	with pytest.raises(ValueError):
		standup_send(owner_token, channel_id1, 1001*"A")

# Test for a message with 1000 characters
def test_standup_send_3():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	standup_send(owner_token, channel_id1, 1000*"A")

# Test for a message with 999 characters
def test_standup_send_4():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	standup_send(owner_token, channel_id1, 999*"A")

# Test for an empty message
def test_standup_send_5():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	with pytest.raises(ValueError):
		standup_send(owner_token, channel_id1, "")

# Test for starting a standup on a channel the user is not part of
def test_standup_send_6():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	with pytest.raises(AccessError):
		standup_send(u_token, channel_id1, "Hey Lets start the standup")

# Test for starting a standup on a channel the user is not part of
def test_standup_send_7():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	with pytest.raises(AccessError):
		standup_send(u_token, channel_id1, "Hey Lets start the standup")


# Test for sending a message when the standup has ended
def test_standup_send_8():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	with pytest.raises(ValueError):
		standup_send(owner_token, channel_id1, "Hey Lets start the standup")

# Test for sending a message when there is no standup
def test_standup_send_9():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	with pytest.raises(ValueError):
		standup_send(owner_token, channel_id1, "Hey Lets start the standup")

# Test for a normal message
def test_standup_send_10():
	reset_channels()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1)
	standup_send(owner_token, channel_id1, "Hey Lets start the standup")
