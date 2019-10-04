import pytest

def message_react(token,message_id,react_id):
	pass

#Value error when: message_id is not a valid message in the current channel
#react_id doesn't belong to a valid id
#message with message_id already has a react_id (no react dupes)

#All test assume that nothing (users/channels/reacts/messages) exist prior to testing
#All test assume that reacts exist from react_id 0 -> react_id 50
def test_message_react_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'Hey guys they just released reacts on slackr')
	message_react(user1,1,1)

def test_message_react_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'so apparently they have 50 reacts out right now')
	message_react(user1,1,50)

def test_message_react_3():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'I wonder what happens if I react with react 51')
	with pytest.raises(ValueError):
		message_react(user1,1,51)

def test_message_react_4():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	with pytest.raises(ValueError):
		message_react(user1,1,1)

def test_message_react_5():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	user2 = userDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'hey try reacting to my message after I do')
	message_send(user2,channel1,'alright let me try it now')
	message_react(user1,1,32)
	message_react(user2,1,26)

def test_message_react_6():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	user2 = userDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'okay try using the same react as me')
	message_send(user2,channel1,'okay here I go again')
	message_react(user1,1,12)
	with pytest.raises(ValueError):
		message_react(user2,1,12)