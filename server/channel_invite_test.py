import pytest
from auth_login_test import auth_login
from channels_create_test import channels_create

def channel_invite(token, channel_id, u_id):
    pass

#Assumption: 12345 is a channel_id that does not exist
#56789 is a u_id that does not eist

#SETUP BEGIN
dict1 = auth_login('validemail@gmail.com', 'correctpassword')
token = dict1['token']
u_id = dict1['u_id']
dict2 = channels_create(token, 'someChannel', 1)
channel_id = dict2['channel_id']
#SETUP END

def test_channel_invite_test_1():
    channel_invite(token, channel_id, u_id)
    
def test_channel_invite_test_2():
    with pytest.raises(ValueError):
        channel_invite(token, 12345, u_id)

def test_channel_invite_test_3():
    with pytest.raises(ValueError):
        channel_invite(token, channel_id, 56789)

def test_channel_invite_test_4():
    with pytest.raises(ValueError):
        channel_invite(token, 12345, 56789)

