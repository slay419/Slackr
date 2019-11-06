from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join
from functions.message_functions import message_send, message_remove
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

#Given a message_id for a message, this message is removed from the channel




#Testing removing a message sent by an admin in a joined channel
def test_message_remove_1():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(admin1, channel1, 'testing 123')
    assert message_remove(admin1, 1) == {}
    assert is_valid_message(1) == False

#Testing removing messages of messages with different ID's
def test_message_remove_2():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(admin1, channel1, 'test message one')
    message_send(admin1, channel1, 'test message two')
    assert message_remove(admin1, 1) == {}
    assert is_valid_message(1) == False
    assert message_remove(admin1, 2) == {}
    assert is_valid_message(2) == False

#Testing user removing another users message
def test_message_remove_3():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(admin1, channel1, 'sorry guys only admins can remove other peoples messages')
    message_send(user1, channel1, 'are you joking? let me test that')
    with pytest.raises(AccessError):
	    message_remove(user1, 1)

#Testing admin trying to remove another persons message (in this case another admin)
def test_message_remove_4():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(admin1, channel1, "hey admin 2, apparently we can remove each others messages")
    message_send(admin2, channel1, 'that sounds pretty fair to me')
    assert message_remove(admin1, 2) == {}
    assert is_valid_message(2) == False

#Testing admin trying to remove another persons message (in this case a users)
def test_message_remove_5():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(user1, channel1, "hey admin, did you hear you can remove other people messages")
    message_send(admin1, channel1, 'yep, let me show you my admin rights')
    assert message_remove(admin1, 1) == {}
    assert is_valid_message(1) == False

#Testing an admin removing a message that was previously removed
def test_message_remove_6():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(admin1, channel1, 'Hello world!')
    message_remove(admin1, 1)
    with pytest.raises(ValueError):
	    message_remove(admin1, 1)

#Testing an admin removing a message that doesn't exist
def test_message_remove_7():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    with pytest.raises(ValueError):
	    message_remove(admin1, 1)

#Testing a user removing another users message
def test_message_remove_8():
    ######################## BEGIN SETUP ######################
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
    admin['permission_id'] = 2

    adminDict2 = auth_register('admin2steven@gmail.com','adminhello123','adminSteven','Lay')
    admin2 = adminDict2['token']
    admin_id2 = adminDict2['u_id']
    admin_2 = user_dict(admin_id2)
    admin_2['permission_id'] = 2

    channelDict1 = channels_create(admin1, 'chat1', True)
    channel1 = channelDict1['channel_id']

    channelDict2 = channels_create(user1, 'chat2', True)
    channel2 = channelDict2['channel_id']

    channel_join(user1,channel1)
    channel_join(admin2,channel1)
    ##########################    END SETUP   ########################
    
    message_send(admin1, channel1, 'Hello world!')
    with pytest.raises(AccessError):
        message_remove(user1, 1)
