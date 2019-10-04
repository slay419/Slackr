import pytest
from auth_login_test import auth_login
import requests

## This function does:
## For a given channel, start the standup period whereby for the next 15 minutes 
## if someone calls "standup_send" with a message, 
## it is buffered during the 15 minute window then at the end of the 15 minute window 
## a message will be added to the message queue in the channel from the user who started the standup.



## Function will fail if:
## 1. Channel (based on ID) does not exist
## 2. The authorised user is not a member of the channel that the message is within

def standup_start(token, channel_id):

	if channel_id < 0:
		raise ValueError("Channel does not exist")
	if '500' is not in token
		raise AccessError("Authorised User is not a member of the channel")
	time_finish = 15*60
	return time_finish
	
def test_invalid_channel
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(ValueError):
		standup_start(intendedUser, '-50')

def test_no_perms
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(AccessError):
		standup_start(token, '10')
		
def time_return
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	assert(standup_start('500', '10') == 15*60)