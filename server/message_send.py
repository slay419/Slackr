
import pytest
from auth_register_test import auth_register
from auth_login_test import auth_login
from channels_create_test import channels_create
from channel_join_test import channel_join

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
It is assumed that messages sent must be atleast one character long
'''

#Send a message from authorised_user to the channel specified by channel_id
def message_send(token, channel_id, message):
	pass 
	
######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

auth_login('steven@gmail.com','hello123')

channelDict1 = channels_create(user1,'chat1',True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1,'chat2',True)
channel2 = channelDict2['channel_id']

channel_join(user1,channel1)

##########################    END SETUP   ########################


#possible errors:
#Value error when:message to large
#To test message_send, we need user token from auth register
#auth_register(email,password,name_first,name_last) returns dict containing u_id, token
#and a channel_id from channels_create
#channels_create(token,name,is_public) returns dict containing id,name

#Testing string 'hello'
def test_message_send_1():
	message_send(user1, channel1, 'hello')

#Testing special characters
def test_message_send_2():
	message_send(user1, channel1, '!@#$%^&*()_+=')	

#Testing numbers
def test_message_send_3():
	message_send(user1, channel1, '1234567890')

#Testing sending messages to other channels (should function, not stated in spec)
def test_message_send_4():
	message_send(user1, channel2, 'hello')

#Testing mixture of characters,numbers,special characters
def test_message_send_5():
	message_send(user1, channel2, 'HeLlo123!@#%')

#Testing 999 character string
def test_message_send_6():
	message_send(user1, channel2, 999*'a')

#Testing 1000 character string
def test_message_send_7():
	message_send(user1, channel1, 1000*'a')

#Testing string 1001 character string
def test_message_send_8():
	with pytest.raises(ValueError):
		message_send(user1, channel1, 1001*'a')

#Testing string definitely > 1000 characters
def test_message_send_9():
	with pytest.raises(ValueError):
		message_send(user1, channel1, 5000*'a')
