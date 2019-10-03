import pytest
from auth_login_test import auth_login
from channels_create_test import channels_create

#Assuming there are 80 messages in the chat, since there is no function that
#returns the number of messages in the chat
#12345 is a channel id that does not exist
#start must be atleast 0
#AttributError is a placeholder for AccessError


#SETUP BEGIN
dict1 = auth_login('validemail@gmail.com', 'correctpass')
token1 = dict1['token']

dict2 = auth_login('validemail2@gmail.com', 'correctpass2')
token2 = dict2['token']

dict3 = channels_create(token1, 'somechannel', 1)
channel_id = dict3['channel_id']

#SETUP END


def channel_messages(token, channel_id, start):
    pass

def test_channel_messages_1():
    channel_messages(token1, channel_id, 0)

def test_channel_messages_2():
    channel_messages(token1, channel_id, 25)

def test_channel_messages_3():
    channel_messages(token1, channel_id, 50)

def test_channel_messages_4():
    channel_messages(token1, channel_id, 80)

def test_channel_messages_5():
    with pytest.raises(ValueError):
        channel_messages(token1, channel_id, 81)

def test_channel_messages_6():
    with pytest.raises(ValueError):
        channel_messages(token1, 12345, 80)

def test_channel_messages_7():
    with pytest.raises(ValueError):
        channel_messages(token1, 12345, 81)

def test_channel_messages_8():
    with pytest.raises(ValueError):
        channel_messages(token2, 12345, 0)

def test_channel_messages_9():
    with pytest.raises(AttributeError):
        channel_messages(token2, channel_id, 0)

def test_channel_messages_10():
    with pytest.raises(AttributeError):
        channel_messages(token2, channel_id, 81)

def test_channel_messages_11():
    with pytest.raises(AttributeError):
        channel_messages(token2, channel_id, 50)