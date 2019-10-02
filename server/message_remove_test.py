import pytest

def message_remove(token, message_id):
	if message_id == null
		raise ValueError("Message no longer exists") 
	pass

	#possible errors:
	#value error
	#1. message at id doesn't exist
	#access error
	#2. message wasn't sent by the user using message_remove
	#3. message not sent by an owner of the channel (admin i guess? i'm not sure)
	#4. message wasn't sent by an admin or owner of the slack

def test_message_remove_1():
	#To test message_send, we need user token from auth register
	#auth_register(email,password,name_first,name_last) returns dict containing u_id, token
	#and a channel_id from channels_create
	#channels_create(token,name,is_public) returns dict containing id,name
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']

	#assuming no messages have been sent yet
	with pytest.raises(ValueError):
		message_remove(user1, 1)	#not legal

def test_message_remove_2():
	#To test message_send, we need user token from auth register
	#auth_register(email,password,name_first,name_last) returns dict containing u_id, token
	#and a channel_id from channels_create
	#channels_create(token,name,is_public) returns dict containing id,name
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1, "hello")
	message_remove(user1, 1)	#removes message id 1 assuming "hello" is contained in message_id 1		
	with pytest.raises(ValueError):
		message_remove(user1, 1)	#not legal (no more message in message_id 1)

def test_message_remove_3():