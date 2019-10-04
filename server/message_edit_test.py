import pytest

#Given a message, update it's text with new text
def message_edit(token, message_id, message):
	pass

#For tests, we need a token and message_id of previous message
#All tests assume no messages have been written previously

#Value error when attempting to edit a message not sent by yourself (someone elses message)
#Attempting to edit an edited message that you didn't create
#Editing a message that wasn't sent by channel owner
#Editing a message that wasn't sent by slack owner/ an admin
#As such only admin can edit his/hers own messages

#All test assume that nothing (users/channels/reacts/messages) exist prior to testing
#All test assume that user1 is a normal user and admin1 and admin2 are admins and owner1 is an owner of the channel	

def test_message_edit_1():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'testing 123')	
	message_edit(admin1, 1, 'new message')

def test_message_edit_2():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'test message one')	
	message_send(admin1, channel1, 'test message two')	
	message_edit(admin1, 2, 'new test message 2')
	message_remove(admin1, 1, 'new test message 1')

def test_message_edit_3():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'sorry guys only admins can edit messages')	
	message_send(user1, channel1, 'are you joking? let me test that')
	with pytest.raises(AccessError):
		message_edit(user1, 2, 'testing')
	message_edit(admin1, 1, 'admins are cool')

def test_message_edit_4():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	adminDict2 = auth_register('adminsteven2@gmail.com','admin2hello123','admin2Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	admin2 = adminDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, "hey admin 2, apparently we can't edit each others messages")	
	message_send(admin2, channel1, 'that sounds pretty standard to me')
	with pytest.raises(AccessError):
		message_edit(admin1, 2, 'admin1 is really cool')
	with pytest.raises(AccessError):
		message_edit(admin2, 1, 'edit test')

def test_message_edit_5():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	userDict1 = auth_register('steven2@gmail.com','2hello123','2Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, "hey admin, did you hear you can't edit other people messages")	
	message_send(admin1, channel1, 'ridiculous, let me show you my admin rights')
	with pytest.raises(AccessError):
		message_edit(admin1, 1, 'imagine not being an admin')
	message_remove(admin1, 2, 'testing 1 2 3')

def test_message_edit_6():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	with pytest.raises(ValueError):
		message_edit(admin1, 1)