import pytest

def message_pin(token, message_id):
	pass

#Value error on: message_id not valid message
#user isn't an admin
#message is already pinned

#Access error on: user is not member of channel message is in

#For tests 1-3, it is assumed that the user/admin is a member of the channel
#the message is in.
def test_message_pin_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'testing 123')	
	message_pin(admin1, 1)

def test_message_pin_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, 'could an admin pin this message, it is very important')	
	message_pin(admin1, 1)

def test_message_pin_3():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'could a user pin this message for test purposes')	
	with raises.pytest(ValueError)
		message_pin(user1, 1)

def test_message_pin_4():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'I wonder what happens if I pin my own message twice')
	message_pin(admin1, 1)
	with raises.pytest(ValueError)
		message_pin(admin1, 1)

def test_message_pin_5():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	with raises.pytest(ValueError)
		message_pin(admin1, 1)