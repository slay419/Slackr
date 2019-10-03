import pytest
from auth_login_test import auth_login
from channels_create_test import channels_create

#Assumptions channel_id 12345 does not exist
#Attribute error is used as a placeholder for AccessError

def channel_details(token, channel_id):
    pass


#SETUP BEGIN
dict1 = auth_login('validemail@gmail.com', 'correctpass')
token1 = dict1['token']

dict2 = auth_login('validemail2@gmail.com', 'correctpass2')
token2 = dict2['token']

dict3 = channels_create(token1, 'somechannel1', 1)
channel_id1 = dict3['channel_id']

dict4 = channels_create(token2, 'somechannel2', 0)
channel_id2 = dict4['channel_id']

#SETUP END

def test_channel_details_1():
    channel_details(token1, channel_id1)

def test_channel_details_2():
    channel_details(token2, channel_id2)

def test_channel_details_3():
    with pytest.raises(ValueError)
        channel_details(token1, 12345)

def test_channel_details_4():
    with pytest.raises(ValueError)
        channel_details(token2, 12345)

def test_channel_details_5():
    with pytest.raises(AttributeError)
        channel_details(token2, channel_id1)

def test_channel_details_6():
    with pytest.raises(AttributeError)
        channel_details(token1, channel_id2)
