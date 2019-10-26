from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list, channel_messages
from functions.message_functions import message_send
from functions.misc_functions import admin_userpermission_change

from functions.data import *

import pytest

#Assuming there are 80 messages in the chat, since there is no function that
#returns the number of messages in the chat
#start must be atleast 0


#SETUP BEGIN

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownerDict['token']
owner_id = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict['token']
u_id = userDict['u_id']

channel_dict = channels_create(owner_token, 'channel name', True)
channel_id = channel_dict['channel_id']

m1 = message_send(owner_token, channel_id, "message1")
m2 = message_send(owner_token, channel_id, "message2")
m3 = message_send(owner_token, channel_id, "message3")
m4 = message_send(owner_token, channel_id, "message4")
m5 = message_send(owner_token, channel_id, "message5")
m6 = message_send(owner_token, channel_id, "message6")
m7 = message_send(owner_token, channel_id, "message7")
m8 = message_send(owner_token, channel_id, "message8")
m9 = message_send(owner_token, channel_id, "message9")
m10 = message_send(owner_token, channel_id, "message10")
md1 = message_dict(m1['message_id'])
md2 = message_dict(m2['message_id'])
md3 = message_dict(m3['message_id'])
md4 = message_dict(m4['message_id'])
md5 = message_dict(m5['message_id'])
md6 = message_dict(m6['message_id'])
md7 = message_dict(m7['message_id'])
md8 = message_dict(m8['message_id'])
md9 = message_dict(m9['message_id'])
md10 = message_dict(m10['message_id'])

list1 = [
    md1, md2, md3, md4, md5, md6, md7, md8, md9, md10
]

#SETUP END

#different cases where the user should be able to view the message

#edge case, view from most recent message
def test_channel_messages_1():
    print(list1)
    print(list1.sort(key = lambda i: i['time_created'],reverse=True))
    assert(channel_messages(owner_token, channel_id, 0) == {
        'messages': list1.sort(key = lambda i: i['time_created'],reverse=True),
        'start': 0,
        'end': -1
    })

'''
#view from  middle messages
def test_channel_messages_2():
    channel_messages(owner_token, channel_id, 25)

def test_channel_messages_3():
    channel_messages(owner_token, channel_id, 50)

#view from very last message
def test_channel_messages_4():
    channel_messages(owner_token, channel_id, 80)

#start is greater than number of messages in channel
def test_channel_messages_5():
    with pytest.raises(ValueError):
        channel_messages(owner_token, channel_id, 81)

#channel_id does not exist, valid start index (edge case: 80)
def test_channel_messages_6():
    with pytest.raises(ValueError):
        channel_messages(owner_token, channel_id + 1, 80)

#both channel_d does not exist and invalid start index
def test_channel_messages_7():
    with pytest.raises(ValueError):
        channel_messages(owner_token, channel_id + 1, 81)

#channel_id does not exist valid start index (edge case: 0)
def test_channel_messages_8():
    with pytest.raises(ValueError):
        channel_messages(u_token, channel_id + 1, 0)

#user is not a member of channel

def test_channel_messages_9():
    with pytest.raises(AccessError):
        channel_messages(u_token, channel_id, 0)

def test_channel_messages_10():
    with pytest.raises(AccessError):
        channel_messages(u_token, channel_id, 81)

def test_channel_messages_11():
    with pytest.raises(AccessError):
        channel_messages(u_token, channel_id, 50)
'''
