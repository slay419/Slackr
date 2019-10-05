import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create

def channel_invite(token, channel_id, u_id):
    pass

#The only channels and users that exist are those created from
#this test. When you create a channel you join it.

#SETUP BEGIN
dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
token1 = dict1['token']
u_id1 = dict1['u_id']

dict2 = auth_register('email2@gmail.com', 'validpass', 'Peter', 'Steven')
token2 = dict2['token']
u_id2 = dict2['u_id']

dict3 = auth_register('email3@gmail.com', 'validpass', 'Peter', 'Steven')
token3 = dict3['token']
u_id3 = dict3['u_id']

dict4 = channels_create(token1, 'someChannel', 1)
channel_id1 = dict4['channel_id']

dict5 = channels_create(token2, 'someChannel', 0)
channel_id2 = dict5['channel_id']
#SETUP END


#invite second user to channel created by first user
def test_channel_invite_test_1():
    channel_invite(token2, channel_id1, u_id2)


#invite first user to channel created by second user
def test_channel_invite_test_2():
    channel_invite(token1, channel_id2, u_id1)
    
#inviting user to channel with a channel_id that does not exist i.e.
#(channel_id1 + channel_id2)
def test_channel_invite_test_3():
    with pytest.raises(ValueError):
        channel_invite(token1, channel_id1 + channel_id2, u_id1)

#inviting user with user_id that does not exist (U_id1 + u_id2)
def test_channel_invite_test_4():
    with pytest.raises(ValueError):
        channel_invite(token1, channel_id2, u_id1 + u_id2)

#both user_id and channel_id do not exist
def test_channel_invite_test_5():
    with pytest.raises(ValueError):
        channel_invite(token1, channel_id1 + channel_id2, u_id1 + u_id2)

#invite multiple people (2 users)
def test_channel_invite_test_6():
    channel_invite(token2, channel_id1, u_id2)
    channel_invite(token3, channel_id1, u_id3)

#user is already in the channel so cant invite himself
def test_channel_invite_test_7():
    channel_invite(token2, channel_id1, u_id2)
    with pytest.raises(ValueError):
        channel_invite(token2, channel_id1, u_id2)




