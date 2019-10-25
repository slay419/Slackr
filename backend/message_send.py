from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join
from functions.message_functions import message_send
from functions.data import *

import pytest
'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
It is assumed that messages sent must be atleast one character long
'''

#Send a message from authorised_user to the channel specified by channel_id
	
######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

channelDict1 = channels_create(user1,'chat1',True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1,'chat2',True)
channel2 = channelDict2['channel_id']

messagelist = data['messages']
##########################    END SETUP   ########################


#Testing string 'hello'
def test_message_send_1():
    reset_messages()
    assert message_send(user1, channel1, 'hello') == {'message_id': messagelist[0]['message_id']}

#Testing special characters
def test_message_send_2():
    reset_messages()
    assert message_send(user1, channel1, '!@#$%^&*()_+=') == {'message_id': messagelist[0]['message_id']}
    
#Testing numbers
def test_message_send_3():
    reset_messages()
    assert message_send(user1, channel1, '1234567890') == {'message_id': messagelist[0]['message_id']}

#Testing mixture of characters,numbers,special characters
def test_message_send_4():
    reset_messages()
    assert message_send(user1, channel2, 'HeLlo123!@#%') == {'message_id': messagelist[0]['message_id']}
    
#Testing 999 character string
def test_message_send_5():
    reset_messages()
    assert message_send(user1, channel2, 999*'a') == {'message_id': messagelist[0]['message_id']}

#Testing 1000 character string
def test_message_send_6():
    reset_messages()
    assert message_send(user1, channel1, 1000*'a') == {'message_id': messagelist[0]['message_id']}

#Testing string 1001 character string
def test_message_send_7():
    reset_messages()
    with pytest.raises(ValueError):
	    message_send(user1, channel1, 1001*'a')

#Testing string definitely > 1000 characters
def test_message_send_8():
    reset_messages()
    with pytest.raises(ValueError):
	    message_send(user1, channel1, 5000*'a')
