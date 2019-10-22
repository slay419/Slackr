
import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_join_test import channel_join
from message_send_test import message_send
from message_pin_test import message_pin
'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 is a normal user and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
'''

#Given a message within a channel, remove it's mark as unpinned
def message_unpin(token, message_id):
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


#Testing admin unpinning own pinned message
def test_message_unpin_1():
	message_send(admin1, channel1, 'testing 123')	
	message_pin(admin1, 1)
	mesage_unpin(admin1, 1)

#Testing admin pinning and unpinning message for a user
def test_message_unpin_2():
	message_send(user1, channel1, 'could an admin pin and unpin this message, it is very important')	
	message_pin(admin1, 1)
	message_unpin(admin1, 1)

#Testing admin2 unpinning a message that admin1 pinned
def test_message_unpin_3():
	message_send(admin1, channel1, 'apparently we can unpin each others messages')	
	message_send(admin2, channel1, 'let me try that')	
	message_pin(admin1, 1)
	message_unpin(admin2, 1)

#Testing user unpinning a pinned message
def test_message_unpin_4():
	message_send(admin1, channel1, 'could a user try unpinning this message for test purposes')
	message_pin(admin1, 1)
	with raises.pytest(ValueError):
		message_unpin(user1, 1)

#Testing admin unpinning an unpinned message (unpinning twice)
def test_message_unpin_5():
	message_send(admin1, channel1, 'I wonder what happens if I unpin my own message twice')
	message_pin(admin1, 1)
	message_unpin(admin1, 1)
	with raises.pytest(ValueError):
		message_unpin(admin1, 1)

#Testing admin pinning an unpinned message
def test_message_unpin_6():
    message_send(admin1, channel1, 'I wonder what happens if I unpin my own message twice')
    message_pin(admin1, 1)
    message_unpin(admin1, 1)
    message_pin(admin1, 1)

#Testing unpinning message that doesn't exist
def test_message_unpin_7():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	with raises.pytest(ValueError):
		message_unpin(admin1, 1)
