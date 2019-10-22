from auth_register_test         import auth_register
from channels_create_test       import channels_create
from channel_join_test          import channel_join
from channel_addowner_test      import channel_addowner
from error                      import AccessError
import datetime
import pytest


'''
####################### ASSUMPTIONS ######################
Assume "invalid channel id" means the channel has not been created yet OR user
hasn't joined the channel yet
Assume messages must be at least one character long
Assume time in the past means any time before the current time on the user's system
Assume can still use this feature to send messages with no delay
i.e. exactly the same as message_send()
'''


def message_sendlater(token, channel_id, message, time_sent):
    if is_invalid_channel():
        raise ValueError("Channel ID does NOT exist.")
    if len(message) > 1000:
        raise ValueError("Message length is more than 1000 characters")
    if is_in_past(time_sent):
        raise ValueError("Message cannot be set to a time in the past.")

def is_in_past(time_sent):
    now = datetime.datetime.now()
    if time_sent < now:
        return 1

    return 0


######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['u_id']

##########################    END SETUP   ########################

# Testing sending a message in a channel which hasn't been created yet
def test_message_sendlater_1():
    future_time = datetime.datetime(3000, 1, 1)
    with pytest.raises(ValueError):
        message_sendlater(u_token, 1234, "message", future_time)

# Testing sending a message to an incorrect channel id
def test_message_sendlater_2():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    invalid_id = channel_id + 1
    with pytest.raises(ValueError):
        message_sendlater(u_token, invalid_id, "message", future_time)

# Testing sending a message to a channel that hasn't been joined yet
def test_message_sendlater_3():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, "message", future_time)

# Testing sending a message that is more than 1000 characters long
def test_message_sendlater_4():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, 1001 * "a", future_time)

# Testing sending a message exactly 1000 characters long should not raise an error
def test_message_sendlater_5():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    message_sendlater(u_token, channel_id, 1000 * "a", future_time)

# Testing sending a message less than 1000 characters long
def test_message_sendlater_6():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    message_sendlater(u_token, channel_id, 999 * "a", future_time)

# Testing sending a message with numbers should not raise an error
def test_message_sendlater_7():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    message_sendlater(u_token, channel_id, "1234567890", future_time)

# Testing sending a message with too many numbers
def test_message_sendlater_8():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, 1000 * "12345", future_time)

# Testing sending a message with various symbols should not raise an error
def test_message_sendlater_9():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    message_sendlater(u_token, channel_id, "~!@#$%^&*()_+[]{}\|;:'',.<>/?", future_time)

# Testing sending a message with too many symbols
def test_message_sendlater_8():
    future_time = datetime.datetime(3000, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, 1000 * "!@#$%", future_time)

# Testing sending a message with no delay should not raise errors
def test_message_sendlater_9():
    now_time = datetime.datetime.now()
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    message_sendlater(u_token, channel_id, "Message", now_time)

# Testing sending a message a year in the past
def test_message_sendlater_10():
    past_time = datetime.datetime(2018, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, "Message", past_time)

# Testing sending a message with accuracy to up to a second
def test_message_sendlater_11():
    accurate_time = datetime.datetime(2018, 12, 25, 1, 1, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    message_sendlater(u_token, channel_id, "Message", accurate_time)

# Testing sending a message one second into the past
def test_message_sendlater_12():
    now = datetime.datetime(now)
    one_second_ago = now - datetime.delta(0, 1)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, "Message", one_second_ago)

# Testing sending a message an hour into the past
def test_message_sendlater_13():
    now = datetime.datetime(now)
    one_hour_ago = now - datetime.delta(0, 60 * 60)
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        message_sendlater(u_token, channel_id, "Message", one_hour_ago)
