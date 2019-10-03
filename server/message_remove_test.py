import pytest

def message_remove(token, message_id):
	pass

	#possible errors:
	#value error
	#1. message at id doesn't exist
	#access error
	#2. message wasn't sent by the user using message_remove (removing someone elses message)
	#3. message not sent by an owner of the channel (error when removing a message not sent by the owner)
	#4. message wasn't sent by an admin or owner of the slack (error when removing a message not sent by admin)
	
	#Only admin can remove messages (his own messages)

	#All test assume that nothing (users/channels/reacts/messages) exist prior to testing
	#All test assume that user1 is a normal user and admin1 and admin2 are admins and owner1 is an owner of the channel
def test_message_remove_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	ownerDict1 = auth_register('ownersteven@gmail.com','ownerhello123','ownerSteven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	owner1 = ownerDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'testing 123')	
	message_remove(admin1, 1)

def test_message_remove_2():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	ownerDict1 = auth_register('ownersteven@gmail.com','ownerhello123','ownerSteven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	owner1 = ownerDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'test message one')	
	message_send(admin1, channel1, 'test message two')	
	message_remove(admin1, 1)
	message_remove(admin1, 2)

def test_message_remove_3():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	ownerDict1 = auth_register('ownersteven@gmail.com','ownerhello123','ownerSteven','Lay')
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	user1 = userDict1['token']
	owner1 = ownerDict1['token']
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, 'sorry guys only admins can remove messages')	
	message_send(user1, channel1, 'are you joking? let me test that')
	with pytest.raises(AccessError):
		message_remove(user1, 2)
	message_remove(admin1, 1)

def test_message_remove_4():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	adminDict2 = auth_register('adminsteven2@gmail.com','admin2hello123','admin2Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	admin2 = adminDict2['token']
	channel1 = channelDict1['channel_id']
	message_send(admin1, channel1, "hey admin 2, apparently we can't remove each others messages")	
	message_send(admin2, channel1, 'that sounds pretty fair to me')
	with pytest.raises(AccessError):
		message_remove(admin1, 2)
	with pytest.raises(AccessError):
		message_remove(admin2, 1)

def test_message_remove_5():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	userDict1 = auth_register('steven2@gmail.com','2hello123','2Steven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	user1 = userDict1['token']
	channel1 = channelDict1['channel_id']
	message_send(user1, channel1, "hey admin, did you hear you can't remove other people messages")	
	message_send(admin1, channel1, 'ridiculous, let me show you my admin rights')
	with pytest.raises(AccessError):
		message_remove(admin1, 1)
	message_remove(admin1, 2)

def test_message_remove_6():
	adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
	channelDict1 = channels_create(user1, 'chat1',True)
	admin1 = adminDict1['token']
	channel1 = channelDict1['channel_id']
	with pytest.raises(ValueError):
		message_remove(admin1, 1)