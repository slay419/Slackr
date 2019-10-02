import pytest

def auth_register(email, password, name_first, name_last):
	dummyDict = {u_id:1,token:123456}
	return dummyDict

def channels_create(token, name, is_public):
	dummyDict = {channel_id:1}
	return dummyDict

def message_send(token, channel_id, message):
	if len(message) > 1000:
		raise ValueError("Message is more than 1000 characters")
	pass

	#possible errors:
	#1.message to large

	#To test message_send, we need user token from auth register
	#auth_register(email,password,name_first,name_last) returns dict containing u_id, token
	#and a channel_id from channels_create
	#channels_create(token,name,is_public) returns dict containing id,name
def test_message_send_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	channelDict2 = channels_create(user1, 'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	#testing string > 1000
	with pytest.raises(ValueError):
		message_send(user1, channel1, 1001*'a')	#not legal

def test_message_send_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	channelDict2 = channels_create(user1, 'chat2',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	#testing string > 1001
	assert
		message_send(user1, channel1, 1001*'a')	#not legal