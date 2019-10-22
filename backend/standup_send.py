import pytest
from auth_login_test import auth_login
from channels_create_test import channels_create
from channel_join_test import channel_join
from standup_start_test	import standup_start

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


## This function does:
## Sending a message to get buffered in the standup queue, 
## assuming a standup is currently active

## Function will fail if:
## 1. Channel (based on ID) does not exist
## 2. Message is more than 1000 characters
## 3. The authorised user is not a member of the channel that the message is within
## 4. If the standup time has stopped

def standup_send(token, channel_id, message):

	if in_channel(channel_id) is 0:
		raise ValueError("Channel does not exist")
	if len(message) > 1000:
		raise ValueError ("Message more than 1000 characters")
	if len(message) < 1:
		raise ValueError ("Message empty")			
	if if_in_channel(token ,channel_id) is 0:
		raise AttributeError("Authorised User is not a member of the channel")
	if time_left(channel_id) is 0:
		raise AttributeError("The standup time has stopped")
		
'''
If the channel is valid return 1
If the channel is invalid, return 0
'''
def is_channel(channel_id):
	pass

'''
If the user is a member of the channel, return 1
If the user is not a member of the channel, return 0
'''
def if_in_channel(token ,channel_id):
	pass

'''
This function retrieves inforatiom from standup_start
If there is still time left, return 1
If there is no more time left, or no standup called, return 0
'''
def time_left(channel_id)):
	pass

######################## GLOBAL VARIABLES SETUP ######################
# First user
userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']

# Second user
userDict2 = auth_login("person2@gmail.com", "password123")
u_token2 = userDict2['token']

valid_channel_id = channels_create(u_token,'SERVER1', is_public)
no_time_channel_id = channels_create(u_token,'SERVER3', is_public)

invalid_channel_id = channels_create(u_token2,'SERVER2', is_public)

no_channel_id = 123123

no_standup_running_channel_id = 123123123

##########################    END SETUP   ########################

# Test for a channel that does not exist
def test_standup_send_1():
	
	with pytest.raises(ValueError):
		standup_send(u_token, no_channel_id, "Hey Lets start the standup")

# Test for a message with 1001 characters
def test_standup_send_2():

	with pytest.raises(ValueError):
		standup_send(u_token, valid_channel_id, 1001*"A")		

# Test for a message with 1000 characters
def test_standup_send_3():
	standup_send(u_token, valid_channel_id, 1000*"A")

# Test for a message with 999 characters
def test_standup_send_4():
	standup_send(u_token, valid_channel_id, 999*"A")

# Test for an empty message
def test_standup_send_5():
	standup_send(u_token, valid_channel_id, "")

# Test for starting a standup on a channel the user is not part of
def test_standup_send_6():
	
	with pytest.raises(AttributeError):
		standup_send(u_token, invalid_channel_id, "Hey Lets start the standup")	

# Test for starting a standup on a channel the user is not part of
def test_standup_send_7():
	
	with pytest.raises(AttributeError):
		standup_send(u_token2, valid_channel_id, "Hey Lets start the standup")	


# Test for sending a message when the standup has ended
def test_standup_send_8():

	with pytest.raises(AttributeError):
		standup_send(u_token, no_time_channel_id, "Hey Lets start the standup")

# Test for sending a message when there is no standup
def test_standup_send_9():

	with pytest.raises(AttributeError):
		standup_send(u_token, no_standup_running_channel_id, "Hey Lets start the standup")
		
# Test for a normal message
def test_standup_send_10():
	standup_send(u_token, valid_channel_id, "Hey Lets start the standup"		