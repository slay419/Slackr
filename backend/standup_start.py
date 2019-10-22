import pytest
from auth_login_test import auth_login
from channels_create_test               import channels_create
from channel_join_test                  import channel_join


'''
####################### ASSUMPTIONS ######################
Assume the time is returned as a 'datetime' object
Assume creating a channel immediatly causes the creator to join
Assume there is no permission required to start a standup
Assume you cannot have two standups running at the same time on the same channel
'''


## This function does:
## For a given channel, start the standup period whereby for the next 15 minutes 
## if someone calls "standup_send" with a message, 
## it is buffered during the 15 minute window then at the end of the 15 minute window 
## a message will be added to the message queue in the channel from the user who started the standup.

## Function will fail if:
## 1. Channel (based on ID) does not exist
## 2. The authorised user is not a member of the channel that the message is within

def standup_start(token, channel_id):

	if in_channel(channel_id) is 0:
		raise ValueError("Channel does not exist")
	if if_in_channel(token ,channel_id) is 0:
		raise AttributeError("Authorised User is not a member of the channel")
	return time_finish
	
'''
If the channel is valid return 1
If the channel is invalid, return 0
'''
def in_channel(channel_id):
	pass

'''
If the user is a member of the channel, return 1
If the user is not a member of the channel, return 0
'''
def if_in_channel(token ,channel_id):
	pass

######################## GLOBAL VARIABLES SETUP ######################
# First user
userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']

# Second user
userDict2 = auth_login("person2@gmail.com", "password123")
u_token2 = userDict2['token']


valid_channel_id = channels_create(u_token,'SERVER1', is_public)

invalid_channel_id = channels_create(u_token2,'SERVER2', is_public)

no_channel_id = 123123

##########################    END SETUP   ########################

	
# Testing a invalid channel_id 
def test_standup_start_1():
	with pytest.raises(ValueError):
		standup_start(u_token, no_channel_id)

# Testing a channel id that the user is not part
def test_standup_start_2():
	with pytest.raises(AttributeError):
		standup_start(u_token, invalid_channel_id)

# Testing a channel id that the user is not part
def test_standup_start_3():
	with pytest.raises(AttributeError):
		standup_start(u_token2, valid_channel_id)

# Testing a channel id that the user is part of
def time_standup_start_4():
	assert(standup_start(u_token, valid_channel_id) == time_finish)