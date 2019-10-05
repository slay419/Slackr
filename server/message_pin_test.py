
import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_join_test import channel_join
from message_send_test import message_sendge

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 and user2 are normal users
It is assumed that messages sent must be atleast one character long
'''

#Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
def message_pin(token, message_id):
	pass


######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
admin1 = adminDict1['token']
admin_id1 = adminDict1['u_id']

channelDict1 = channels_create(user1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1, channel1)
channel_join(admin1, channel1)

##########################    END SETUP   ########################

#Testing admin pinning own message
def test_message_pin_1():
	message_send(admin1, channel1, 'testing 123')	
	message_pin(admin1, 1)

#Testing admin pinning another persons message (a users)
def test_message_pin_2():
	message_send(user1, channel1, 'could an admin pin this message, it is very important')	
	message_pin(admin1, 1)

#Testing user pinning another persons message (an admins)
def test_message_pin_3():
	message_send(admin1, channel1, 'could a user pin this message for test purposes')	
	with raises.pytest(ValueError)
		message_pin(user1, 1)

#Testing admin pinning an already pinned message
def test_message_pin_4():
	message_send(admin1, channel1, 'I wonder what happens if I pin my own message twice')
	message_pin(admin1, 1)
	with raises.pytest(ValueError)
		message_pin(admin1, 1)

#Testing admin pinning message that doesn't exist
def test_message_pin_5():
	with raises.pytest(ValueError)
		message_pin(admin1, 1)