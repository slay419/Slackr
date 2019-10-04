import pytest
from auth_login_test import auth_login
from standup_start import standup_start
import requests

## This function does:
## Sending a message to get buffered in the standup queue, 
## assuming a standup is currently active

## Function will fail if:
## 1. Channel (based on ID) does not exist
## 2. Message is more than 1000 characters
## 3. The authorised user is not a member of the channel that the message is within
## 4. If the standup time has stopped

def standup_send(token, channel_id, message)

	 

	if channel_id < 0:
		raise ValueError("Channel does not exist")
	if len(message) > 1000
		raise ValueError ("Message more than 1000 characters")		
	if '500' is not in token
		raise AccessError("Authorised User is not a member of the channel")
	
	time_left = standup_start(token, channel_id)
	
	if time_left is 0
		raise AccessError("The standup time has stopped")
		

def test_invalid_channel
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(ValueError):
		standup_send(intendedUser, '-50', "Hey Lets start the standup")
def test_long_message
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(ValueError):
		standup_send(intendedUser, '50', 500*"Hey Lets start the standup")		

def test_no_perms
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(AccessError):
		standup_send(intendedUser, '50', "Hey Lets start the standup")	
		
def test_invalid_timer
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(AccessError):
		standup_send('500', '50', "Hey Lets start the standup")		