
import pytest
from auth_register_test import auth_register
from auth_login_test import auth_login
from channels_create_test import channels_create
from channel_join_test import channel_join

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 is a normal user and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
'''

#Given a message_id for a message, this message is removed from the channel
def message_remove(token, message_id):
	pass


######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
admin1 = adminDict1['token']
admin_id1 = adminDict1['u_id']

adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
admin2 = adminDict2['token']
admin_id2 = adminDict2['u_id']

auth_login('steven@gmail.com', 'hello123')
auth_login('adminsteven@gmail.com', 'adminhello123')
auth_login('admin2steven@gmail.com', 'adminhello123')

channelDict1 = channels_create(user1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1,channel1)
channel_join(admin1,channel1)
channel_join(admin2,channel1)

##########################    END SETUP   ########################



#All test assume that nothing (users/channels/reacts/messages) exist prior to testing

	
#Testing removing a message sent by an admin in a joined channel
def test_message_remove_1():
	message_send(admin1, channel1, 'testing 123')	
	message_remove(admin1, 1)

#Testing removing messages of messages with different ID's
def test_message_remove_2():
	message_send(admin1, channel1, 'test message one')	
	message_send(admin1, channel1, 'test message two')	
	message_remove(admin1, 1)
	message_remove(admin1, 2)

#Testing user removing a message
def test_message_remove_3():
	message_send(admin1, channel1, 'sorry guys only admins can remove messages')	
	message_send(user1, channel1, 'are you joking? let me test that')
	with pytest.raises(AccessError):
		message_remove(user1, 2)

#Testing admin trying to remove another persons message (in this case another admin)
def test_message_remove_4():
	message_send(admin1, channel1, "hey admin 2, apparently we can't remove each others messages")	
	message_send(admin2, channel1, 'that sounds pretty fair to me')
	with pytest.raises(AccessError):
		message_remove(admin1, 2)

#Testing admin trying to remove another persons message (in this case a users)
def test_message_remove_5():
	message_send(user1, channel1, "hey admin, did you hear you can't remove other people messages")	
	message_send(admin1, channel1, 'ridiculous, let me show you my admin rights')
	with pytest.raises(AccessError):
		message_remove(admin1, 1)

#Testing an admin removing a message that was previously removed
def test_message_remove_6():
	message_send(admin1, channel1, 'Hello world!')
	message_remove(admin1, 1)
	with pytest.raises(ValueError):
		message_remove(admin1, 1)
		
#Testing an admin removing a message that doesn't exist
def test_message_remove_7():
	with pytest.raises(ValueError):
		message_remove(admin1, 1)
