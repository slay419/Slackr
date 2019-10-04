import pytest

def message_unpin(token, message_id):
	pass

#Value error on: message_id not valid message
#user isn't an admin
#message is already unpinned

#Access error on: user is not member of channel message is in

#For tests 1-3, it is assumed that the user/admin is a member of the channel
#the message is in.
def test_message_unpin_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'testing 123')	
	message_pin(admin1, 1)
	mesage_unpin(admin1,1)

def test_message_unpin_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, 'could an admin pin this message, it is very important')	
	message_pin(admin1, 1)
	message_unpin(admin1,1)

def test_message_unpin_3():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	adminDict2 = auth_register('adminsteven2@gmail.com','admin2hello123','admin2Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	admin2 = adminDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'apparently we can unpin each others messages')	
	message_send(admin2, channel1, 'let me try that')	
	message_pin(admin1, 1)
	message_unpin(admin2,1)

def test_message_unpin_4():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'could a user try unpinning this message for test purposes')
	message_pin(admin1,1)
	with raises.pytest(ValueError)
		message_unpin(user1, 1)

def test_message_unpin_5():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'I wonder what happens if I unpin my own message twice')
	message_pin(admin1, 1)
	message_unpin(admin1,1)
	with raises.pytest(ValueError)
		message_unpin(admin1, 1)

def test_message_unpin_6():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	with raises.pytest(ValueError)
		message_unpin(admin1, 1)