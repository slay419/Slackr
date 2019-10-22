import pytest
from auth_login_test import auth_login
from channels_create_test import channels_create
from error import AcessError

#Assuming there are 80 messages in the chat, since there is no function that
#returns the number of messages in the chat
#start must be atleast 0


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

#different cases where the user should be able to view the message

#edge case, view from most recent message
def test_channel_messages_1():
    channel_messages(token1, channel_id, 0)

#view from  middle messages
def test_channel_messages_2():
    channel_messages(token1, channel_id, 25)

def test_channel_messages_3():
    channel_messages(token1, channel_id, 50)

#view from very last message
def test_channel_messages_4():
    channel_messages(token1, channel_id, 80)

#start is greater than number of messages in channel
def test_channel_messages_5():
    with pytest.raises(ValueError):
        channel_messages(token1, channel_id, 81)

#channel_id does not exist, valid start index (edge case: 80)
def test_channel_messages_6():
    with pytest.raises(ValueError):
        channel_messages(token1, channel_id + 1, 80)

#both channel_d does not exist and invalid start index
def test_channel_messages_7():
    with pytest.raises(ValueError):
        channel_messages(token1, channel_id + 1, 81)

#channel_id does not exist valid start index (edge case: 0)
def test_channel_messages_8():
    with pytest.raises(ValueError):
        channel_messages(token2, channel_id + 1, 0)

#user is not a member of channel

def test_channel_messages_9():
    with pytest.raises(AccessError):
        channel_messages(token2, channel_id, 0)

def test_channel_messages_10():
    with pytest.raises(AccessError):
        channel_messages(token2, channel_id, 81)

def test_channel_messages_11():
    with pytest.raises(AccessError):
        channel_messages(token2, channel_id, 50)