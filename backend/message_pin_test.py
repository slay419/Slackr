from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join
from functions.message_functions import message_send, message_remove, message_pin
from functions.misc_functions import admin_userpermission_change
from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 and user2 are normal users
It is assumed that messages sent must be atleast one character long
'''

#Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend


######################## GLOBAL VARIABLES SETUP ######################
reset_data()
userDict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']
user = user_dict(user_id1)
user['permission_id'] = 3

adminDict1 = auth_register('adminsteven@gmail.com','adminhello123','adminSteven','Lay')
admin1 = adminDict1['token']
admin_id1 = adminDict1['u_id']
admin = user_dict(admin_id1)
admin['permission_id'] = 1

adminDict2 = auth_register('2adminsteven@gmail.com','adminhello123','adminSteven','Lay')
admin2 = adminDict2['token']
admin_id2 = adminDict2['u_id']
admin_2 = user_dict(admin_id2)
admin_2['permission_id'] = 1

channelDict1 = channels_create(admin1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(admin2, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1, channel1)

##########################    END SETUP   ########################

#Testing admin pinning own message
def test_message_pin_1():
    reset_messages()
    message_send(admin1, channel1, 'testing 123')
    assert message_pin(admin1, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == True

#Testing admin pinning another persons message (a users)
def test_message_pin_2():
    reset_messages()
    message_send(user1, channel1, 'could an admin pin this message, it is very important')
    assert message_pin(admin1, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == True

#Testing user pinning another persons message (an admins)
def test_message_pin_3():
    reset_messages()
    message_send(admin1, channel1, 'could a user pin this message for test purposes')
    with pytest.raises(ValueError):
	    message_pin(user1, 1)

#Testing admin pinning an already pinned message
def test_message_pin_4():
    reset_messages()
    message_send(admin1, channel1, 'I wonder what happens if I pin my own message twice')
    message_pin(admin1, 1)
    with pytest.raises(ValueError):
	    message_pin(admin1, 1)

#Testing admin pinning message that doesn't exist
def test_message_pin_5():
    reset_messages()
    with pytest.raises(ValueError):
	    message_pin(admin1, 1)
	    
#Member is not a part of channel
def test_message_pin_6():
    reset_messages()
    message_send(admin1, channel1, 'Test message')
    with pytest.raises(AccessError):
        message_pin(admin2, 1)
