from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join
from functions.message_functions import message_send, message_remove, message_pin, message_unpin
from functions.misc_functions import admin_userpermission_change
from functions.data import *

import pytest
'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 is a normal user and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
'''

#Given a message within a channel, remove it's mark as unpinned


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

adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','admin2Steven','Lay')
admin2 = adminDict2['token']
admin_id2 = adminDict2['u_id']
admin_2 = user_dict(admin_id2)
admin_2['permission_id'] = 1

channelDict1 = channels_create(admin1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(admin1, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1, channel1)
channel_join(admin2, channel1)
##########################    END SETUP   ########################


#Testing admin unpinning own pinned message
def test_message_unpin_1():
    reset_messages()
    message_send(admin1, channel1, 'testing 123')
    message_pin(admin1, 1)
    assert message_unpin(admin1, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == False

#Testing admin pinning and unpinning message for a user
def test_message_unpin_2():
    reset_messages()
    message_send(user1, channel1, 'could an admin pin and unpin this message, it is very important')
    message_pin(admin1, 1)
    assert message_unpin(admin1, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == False

#Testing admin2 unpinning a message that admin1 pinned
def test_message_unpin_3():
    reset_messages()
    message_send(admin1, channel1, 'apparently we can unpin each others messages')
    message_send(admin2, channel1, 'let me try that')
    message_pin(admin1, 1)
    assert message_unpin(admin2, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == False

#Testing user unpinning a pinned message
def test_message_unpin_4():
    reset_messages()
    message_send(admin1, channel1, 'could a user try unpinning this message for test purposes')
    message_pin(admin1, 1)
    with pytest.raises(ValueError):
	    message_unpin(user1, 1)

#Testing admin unpinning an unpinned message (unpinning twice)
def test_message_unpin_5():
    reset_messages()
    message_send(admin1, channel1, 'I wonder what happens if I unpin my own message twice')
    message_pin(admin1, 1)
    message_unpin(admin1, 1)
    with pytest.raises(ValueError):
	    message_unpin(admin1, 1)

#Testing admin pinning an unpinned message
def test_message_unpin_6():
    reset_messages()
    message_send(admin1, channel1, 'I wonder what happens if I unpin my own message twice')
    message_pin(admin1, 1)
    assert message_unpin(admin1, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == False
    assert message_pin(admin1, 1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['is_pinned'] == True

#Testing unpinning message that doesn't exist
def test_message_unpin_7():
    reset_messages()
    with pytest.raises(ValueError):
	    message_unpin(admin1, 1)
