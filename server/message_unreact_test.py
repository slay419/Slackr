import pytest

def message_unreact(token, message_id, react_id):
	pass
#Value error when message_id is not valid message in currently joined channel
#react id doesn't exist
#message with id doesn't contain react with react_id

#All test assume that nothing (users/channels/reacts/messages) exist prior to testing
#All test assume that reacts exist from react_id 0 -> react_id 50
def test_message_unreact_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'Testing ureacts on slackr')
	message_react(user1,1,1)
	message_unreact(user1,1,1)

def test_message_unreact_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'Testing unreacts2 on slackr')
	message_react(user1,1,32)
	message_react(user1,1,32)

def test_message_unreact_3():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'Unreacting with reacts that do not exist')
	message_react(user1,1,50)
	with pytest.raises(ValueError):
		message_unreact(user1,1,51)

def test_message_unreact_4():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	with pytest.raises(ValueError):
		message_unreact(user1,1,1)

def test_message_unreact_5():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	user2 = userDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'so apparently you can remove other peoples reacts')
	message_send(user2,channel1,'really? let me try it now')
	message_react(user1,1,32)
	message_unreact(user2,1,32)

def test_message_unreact_6():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	user2 = userDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(user1,channel1,'how about if you do not have a react')
	message_send(user2,channel1,'let me try again')
	with pytest.raises(ValueError):
		message_react(user2,1,12)