
import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_join_test import channel_join
from message_send_test import message_send
from message_react_test import message_react

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 and user2 are normal users
It is assumed that messages sent must be atleast one character long
All test assume that reacts exist from react_id 0 -> react_id 50
'''

#Given a message within a channel the authorised user is part of, remove a "react" to that particular message
def message_unreact(token, message_id, react_id):
	pass
	
	
######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
user2 = userDict2['token']
user_id2 = userDict2['u_id']

channelDict1 = channels_create(user1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1,channel1)
channel_join(user2,channel1)

##########################    END SETUP   ########################

#Testing user unreacting to a message he reacted to with same react_id (1,1)
def test_message_unreact_1():
	message_send(user1,channel1,'Testing ureacts on slackr')
	message_react(user1,1,1)
	message_unreact(user1,1,1)

#Testing user unreacting to a message he reacted to with same react_id (31,31)
def test_message_unreact_2():
	message_send(user1,channel1,'Testing unreacts2 on slackr')
	message_react(user1,1,32)
	message_react(user1,1,32)

#Testing user unreacting to a message with invalid react_id (50,51)
def test_message_unreact_3():
	message_send(user1,channel1,'Unreacting with reacts that do not exist')
	message_react(user1,1,50)
	with pytest.raises(ValueError):
		message_unreact(user1,1,51)

#Testing user unreacting to message that doesn't exist
def test_message_unreact_4():
	with pytest.raises(ValueError):
		message_unreact(user1,1,1)

#Testing two users, one reacting to a message and the other unreacting with same
#react_id (32,32)
def test_message_unreact_5():
	message_send(user1,channel1,'so apparently you can remove other peoples reacts')
	message_send(user2,channel1,'really? let me try it now')
	message_react(user1,1,32)
	message_unreact(user2,1,32)

#Testing user2 unreacting message from user1 that doesn't contain a react
def test_message_unreact_6():
	message_send(user1,channel1,'how about if you do not have a react')
	message_send(user2,channel1,'let me try again')
	with pytest.raises(ValueError):
		message_react(user2,1,12)
