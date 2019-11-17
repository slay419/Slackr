#pylint: disable=missing-docstring
#pylint: disable=unused-variable
from datetime import datetime
import pytest

from functions.auth_functions import auth_register
from functions.channel_functions import channels_create
from functions.misc_functions import standup_start, standup_active
from functions.data import reset_data

from functions.exceptions import ValueError, AccessError


'''
####################### ASSUMPTIONS ######################
Assume the function can either have two states, active or deactive
'''

######################## GLOBAL VARIABLES SETUP ######################
def setup():
    reset_data()
    # First user
    owner_dict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
    owner_token = owner_dict['token']

    # Second user
    user_dict = auth_register("person2@gmail.com", "password123", "firstname", "lastname")
    u_token = user_dict['token']

    return owner_token, u_token
##########################    END SETUP   ########################


# Testing a invalid channel_id
def test_standup_active_1():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    with pytest.raises(ValueError):
        standup_active(owner_token, channel_id1 + 1)

# Testing a channel id that the user is not part
def test_standup_active_2():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    with pytest.raises(AccessError):
        standup_active(u_token, channel_id1)

# Testing starting a standup that is already running
def test_standup_active_3():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    standup_start(owner_token, channel_id1, 10)
    assert standup_active(owner_token, channel_id1)['is_active'] is True

# Testing starting a standup that is not running
def test_standup_active_4():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']
    assert standup_active(owner_token, channel_id1)['is_active'] is False

# Testing starting a standup that just finished
def test_standup_active_5():
    owner_token, u_token = setup()
    channel1 = channels_create(owner_token, 'SERVER1', True)
    channel_id1 = channel1['channel_id']

    channel1['standup_queue'] = ["Peter: List", "Peter: Of", "Peter: Messages"]

    end_time = datetime.now()
    timestamp = end_time.replace().timestamp()
    channel1['standup_end'] = timestamp

    assert standup_active(owner_token, channel_id1)['is_active'] is False
