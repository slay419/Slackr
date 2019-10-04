import pytest

def message_send(token, channel_id, message):
	pass

	#possible errors:
	#Value error when:message to large
	#To test message_send, we need user token from auth register
	#auth_register(email,password,name_first,name_last) returns dict containing u_id, token
	#and a channel_id from channels_create
	#channels_create(token,name,is_public) returns dict containing id,name

	#All test assume that nothing (users/channels/reacts/messages) exist prior to testing
def test_message_send_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, 'hello')	

def test_message_send_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, 'HElL014%@#!9xCSzsafqw9-#*')	

def test_message_send_3():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, '1001')	

def test_message_send_4():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel2, '')

def test_message_send_5():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	#assuming '999characterstring' is taken literally
	message_send(user1, channel2, '999characterstring')	#not legal

def test_message_send_6():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	#assuming '1000characterstring' is taken literally
	message_send(user1, channel1, '1000characterstring')

def test_message_send_7():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	#assuming '1001characterstring' is taken literally
	with pytest.raises(ValueError):
		message_send(user1, channel1, '1001characterstring')

def test_message_send_8():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1,'chat1',True)
	channelDict2 = channels_create(user1,'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	#assuming '5000characterstring' is taken literally
	with pytest.raises(ValueError):
		message_send(user1, channel1, '5000characterstring')