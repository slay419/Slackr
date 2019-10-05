import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_invite_test import channel_invite

#Attribute error is used as a placeholder for AccessError

def channel_details(token, channel_id):
    pass


#SETUP BEGIN
dict1 = auth_register('validemail@gmail.com', 'correctpass')
token1 = dict1['token']

dict2 = auth_register('validemail2@gmail.com', 'correctpass2')
token2 = dict2['token']
u_id2 = dict2['u_id']

dict3 = channels_create(token1, 'somechannel1', 1)
channel_id1 = dict3['channel_id']

dict4 = channels_create(token2, 'somechannel2', 0)
channel_id2 = dict4['channel_id']

#SETUP END

#user1 views details of channel he created
def test_channel_details_1():
    channel_details(token1, channel_id1)

#user2 views details of channel he created
def test_channel_details_2():
    channel_details(token2, channel_id2)

#user1 tries to view details of channel with id that does not exist
def test_channel_details_3():
    with pytest.raises(ValueError):
        channel_details(token1, channel_id1 + channel_id2)

#user2 tries to view details of channel with id that does not exist
def test_channel_details_4():
    with pytest.raises(ValueError):
        channel_details(token2, channel_id1 + channel_id2)

#user2 tries to view details of channel he is not part of
def test_channel_details_5():
    with pytest.raises(AttributeError):
        channel_details(token2, channel_id1)

#user1 tries to view details of a channel he is not part of
def test_channel_details_6():
    with pytest.raises(AttributeError):
        channel_details(token1, channel_id2)

#invite user2 to join channel and then view it.   
def test_channel_details_7():
    channel_invite(token2, channel_id1, u_id2)
    channel_details(token2, channel_id1)