import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_join_test import channel_join
from message_send_test import message_send
from message_remove_test import message_remove

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 is a normal user and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
'''

#Given a message, update it's text with new text
def message_edit(token, message_id, message):
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

channelDict1 = channels_create(user1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1,channel1)
channel_join(admin1,channel1)
channel_join(admin2,channel1)

##########################    END SETUP   ########################


#Testing editing a message sent from an admin
def test_message_edit_1():
	message_send(admin1, channel1, 'testing 123')	
	message_edit(admin1, 1, 'new message')

#Testing editing two message sent from the same admin
def test_message_edit_2():
	message_send(admin1, channel1, 'test message one')	
	message_send(admin1, channel1, 'test message two')	
	message_edit(admin1, 2, 'new test message 2')
	message_edit(admin1, 1, 'new test message 1')

#Testing user attempting to edit message
def test_message_edit_3():
	message_send(admin1, channel1, 'sorry guys only admins can edit messages')	
	message_send(user1, channel1, 'are you joking? let me test that')
	with pytest.raises(AccessError):
		message_edit(user1, 2, 'testing')

#Testing admin trying to edit another persons message (in this case an admins)
def test_message_edit_4():
	message_send(admin1, channel1, "hey admin 2, apparently we can't edit each others messages")	
	message_send(admin2, channel1, 'that sounds pretty standard to me')
	with pytest.raises(AccessError):
		message_edit(admin1, 2, 'admin1 is really cool')

#Testing admin trying to edit another persons message (in this case a users)
def test_message_edit_5():
	message_send(user1, channel1, "hey admin, did you hear you can't edit other people messages")	
	message_send(admin1, channel1, 'ridiculous, let me show you my admin rights')
	with pytest.raises(AccessError):
		message_edit(admin1, 1, 'imagine not being an admin')

#Testing editing a message that doesn't exist
def test_message_edit_6():
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	with pytest.raises(ValueError):
		message_edit(admin1, 1)

#Testing editing a message that has been removed
def test_message_edit_7():
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'testing')
	message_remove(admin1, 1)
	with pytest.raises(ValueError):
		message_edit(admin1, 1)

