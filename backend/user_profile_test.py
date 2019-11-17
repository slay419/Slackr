#pylint: disable=missing-docstring
#pylint: disable=unused-variable

import pytest
from functions.auth_functions import auth_register
from functions.profile_functions import user_profile, user_profile_sethandle

from functions.data import reset_users

from functions.exceptions import ValueError


'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 is a normal user and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
Assume NONE is returned in handle_str field if no handle has been set

'''


#Testing user1's profile with no handle
def test_user_profile_1():
    reset_users()
    user_dict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
    user1 = user_dict1['token']
    user1_id = user_dict1['u_id']
    profile_dict1 = user_profile(user1, user1_id)
    assert(profile_dict1 == {
        'email' : 'steven@gmail.com',
        'name_first' : 'Steven',
        'name_last' : 'Lay',
        'handle_str' : 'StevenLay'
    })

#Testing user2's profile with handle
def test_user_profile_2():
    reset_users()
    user_dict2 = auth_register('steven2@gmail.com', 'hello123', 'Steven2', 'Lay')
    user2 = user_dict2['token']
    user2_id = user_dict2['u_id']
    user_profile_sethandle(user2, 'l33thack3r')
    profile_dict2 = user_profile(user2, user2_id)
    assert(profile_dict2 == {
        'email' : 'steven2@gmail.com',
        'name_first' : 'Steven2',
        'name_last' : 'Lay',
        'handle_str' : 'l33thack3r'
    })

#Testing invalid users profile
def test_user_profile_3():
    reset_users()
    user_dict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
    user1 = user_dict1['token']
    user1_id = user_dict1['u_id']
    invalid_id = user1_id + 1
    with pytest.raises(ValueError):
        profile_dict3 = user_profile(user1, invalid_id)
