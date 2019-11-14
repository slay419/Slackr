from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change, standup_send, standup_start, standup_active
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail

from functions.data import *

from datetime import datetime, timedelta, timezone
import pytest

'''
####################### ASSUMPTIONS ######################
Assume the function can either have two states, active or deactive
'''

######################## GLOBAL VARIABLES SETUP ######################
def setup():
	reset_data()
	# First user
	ownerDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	owner_token = ownerDict['token']

	# Second user
	userDict = auth_register("person2@gmail.com", "password123", "firstname", "lastname")
	u_token = userDict['token']

	return owner_token, u_token
##########################    END SETUP   ########################


# Testing a invalid channel_id
def test_standup_active_1():
	owner_token, u_token = setup()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	with pytest.raises(ValueError):
		standup_active(owner_token, channel_id1 + 1)

# Testing a channel id that the user is not part
def test_standup_active_2():
	owner_token, u_token = setup()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	with pytest.raises(AccessError):
		standup_active(u_token, channel_id1)

# Testing starting a standup that is already running
def test_standup_active_3():
	owner_token, u_token = setup()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	standup_start(owner_token, channel_id1, 10)
	assert(standup_active(owner_token,channel_id1)['is_active'] == True)

# Testing starting a standup that is not running
def test_standup_active_4():
	owner_token, u_token = setup()
	channel1 = channels_create(owner_token, 'SERVER1', True)
	channel_id1 = channel1['channel_id']
	assert(standup_active(owner_token,channel_id1)['is_active'] == False)


