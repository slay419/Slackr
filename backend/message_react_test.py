from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join
from functions.message_functions import message_send, message_remove, message_react
from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
It is assumed that messages sent must be atleast one character long
All test assume that reacts exist from react_id 0 -> react_id 50
'''
#Given a message within a channel the authorised user is part of, add a "react" to that particular message


######################## GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
user2 = userDict2['token']
user2id = userDict2['u_id']

channelDict1 = channels_create(user1,'chat1',True)
channel1 = channelDict1['channel_id']

channel_join(user2,channel1)
##########################    END SETUP   ########################


#Value error when: message_id is not a valid message in the current channel
#react_id doesn't belong to a valid id
#message with message_id already has a react_id (no react dupes)

#Testing user reacting to own message (React_id 1)
def test_message_react_1():
    reset_messages()
    message_send(user1,channel1,'Hey guys they just released reacts on slackr')
    assert message_react(user1,1,1) == {}
    for messagedict in data['messages']:
        if messagedict['message_id'] == 1:
            assert messagedict['reacts'][0] == 1

#Testing user reacting to own message with invalid react (React_id 2)
def test_message_react_2():
    reset_messages()
    message_send(user1,channel1,'I wonder what happens if I react with react 2')
    with pytest.raises(ValueError):
	    message_react(user1,1,2)

#Testing user reacting to invalid message (Message doesn't exist)
def test_message_react_3():
    reset_messages()
    with pytest.raises(ValueError):
	    message_react(user1,1,1)

#Testing 2 users reacting to same message with the same reacts (1,1)
def test_message_react_4():
    reset_messages()
    message_send(user1,channel1,'okay try using the same react as me')
    message_send(user2,channel1,'okay here I go again')
    message_react(user1,1,1)
    with pytest.raises(ValueError):
	    message_react(user2,1,1)
