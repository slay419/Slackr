from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.message_functions import message_send
from functions.misc_functions import admin_userpermission_change, standup_send, standup_start, search
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail

from functions.data import *
import math
from datetime import datetime, timedelta, timezone

import pytest
'''
####################### ASSUMPTIONS ######################
Assume entering an empty search	message is not possible as there is
no way to prevent this at the moment
Assume searching will be 'find-in-word'. i.e searching for 'a' will result in 'example'
because the letter a is present
Assume the search message is not case sensetive because it is not possible at the moment
'''

######################## BEGIN SETUP ######################
def setup_users():
	reset_data()
	ownerDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	owner_token = ownerDict['token']
	owner_id = ownerDict['u_id']

	# Second user
	userDict = auth_register("person2@gmail.com", "password123", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']

	# Create channel for messages to send to
	channel = channels_create(owner_token, "channel name", True)
	channel_id = channel['channel_id']

	# Create channel for messages to send to
	second_channel = channels_create(u_token, "second channel", True)
	channel_id2 = second_channel['channel_id']

	return owner_token, owner_id, u_token, u_id, channel_id, channel_id2

def setup_messages():
	owner_token, owner_id, u_token, u_id, channel_id, channel_id2 = setup_users()
	message1 = message_send(owner_token, channel_id, "message1")
	message2 = message_send(owner_token, channel_id, "message12")
	message3 = message_send(owner_token, channel_id, "message3")
	message4 = message_send(owner_token, channel_id, "message4")
	message5 = message_send(u_token, channel_id2, "message32")
	floor_all_message_times()

	return message1, message2, message3, message4, message5

def floor_message_time(message_id):
	message = message_dict(message_id)
	message['time_created'] = math.floor(message['time_created'])

def floor_all_message_times():
	for message_dict in get_data()['messages']:
		floor_message_time(message_dict['message_id'])
		
##########################    END SETUP   ########################

#Testing for exact match
def test_search_1():
	owner_token, owner_id, u_token, u_id, channel_id, channel_id2 = setup_users()
	message1, message2, message3, message4, message5 = setup_messages()
	message_time = math.floor(datetime.now().replace().timestamp())
	message_id2 = message2['message_id']
	assert (search(owner_token, "message12") ==  {
		'messages': [
			{
				'message_id': message_id2,
		        'u_id': owner_id,
		        'message': "message12",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			}
		]
	})

#Test find-in-word search and also across other channels
def test_search_2():
	owner_token, owner_id, u_token, u_id, channel_id, channel_id2 = setup_users()
	message1, message2, message3, message4, message5 = setup_messages()
	message_time = math.floor(datetime.now().replace().timestamp())
	message_id1 = message1['message_id']
	message_id2 = message2['message_id']
	message_id3 = message3['message_id']
	message_id4 = message4['message_id']
	message_id5 = message5['message_id']
	assert (search(owner_token, "message") ==  {
		'messages': [
			{
				'message_id': message_id1,
		        'u_id': owner_id,
		        'message': "message1",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id2,
		        'u_id': owner_id,
		        'message': "message12",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id3,
		        'u_id': owner_id,
		        'message': "message3",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id4,
		        'u_id': owner_id,
		        'message': "message4",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id5,
		        'u_id': u_id,
		        'message': "message32",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			}
		]
	})

#Test find-in-word search
def test_search_3():
	owner_token, owner_id, u_token, u_id, channel_id, channel_id2 = setup_users()
	message1, message2, message3, message4, message5 = setup_messages()
	message_time = math.floor(datetime.now().replace().timestamp())
	message_id1 = message1['message_id']
	message_id2 = message2['message_id']
	assert (search(owner_token, "message1") ==  {
		'messages': [
			{
				'message_id': message_id1,
				'u_id': owner_id,
				'message': "message1",
				'time_created': message_time,
				'is_unread': True,
				'reacts': [],
				'is_pinned': False,
			},
			{
				'message_id': message_id2,
				'u_id': owner_id,
				'message': "message12",
				'time_created': message_time,
				'is_unread': True,
				'reacts': [],
				'is_pinned': False,
			}
		]
	})

#Test no match
def test_search_4():
	owner_token, owner_id, u_token, u_id, channel_id, channel_id2 = setup_users()
	message1, message2, message3, message4, message5 = setup_messages()
	message_time = math.floor(datetime.now().replace().timestamp())
	assert (search(owner_token,"no match") ==  {
		'messages': []
	})

# Testing for empty string returns everything
def test_search_5():
	owner_token, owner_id, u_token, u_id, channel_id, channel_id2 = setup_users()
	message1, message2, message3, message4, message5 = setup_messages()
	message_time = math.floor(datetime.now().replace().timestamp())
	message_id1 = message1['message_id']
	message_id2 = message2['message_id']
	message_id3 = message3['message_id']
	message_id4 = message4['message_id']
	message_id5 = message5['message_id']
	assert (search(owner_token,"") ==  {
		'messages': [
			{
				'message_id': message_id1,
		        'u_id': owner_id,
		        'message': "message1",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id2,
		        'u_id': owner_id,
		        'message': "message12",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id3,
		        'u_id': owner_id,
		        'message': "message3",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id4,
		        'u_id': owner_id,
		        'message': "message4",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			},
			{
				'message_id': message_id5,
		        'u_id': u_id,
		        'message': "message32",
		        'time_created': message_time,
		        'is_unread': True,
		        'reacts': [],
		        'is_pinned': False,
			}
		]
	})
