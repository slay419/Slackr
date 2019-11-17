#pylint: disable=missing-docstring
#pylint: disable=unused-variable

from functions.auth_functions import auth_register
from functions.misc_functions import admin_userpermission_change
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail, user_listall

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
Assume the order of the list of dictionaries is in ascending order of u_id
i.e. order of u_id created
You cannot call this function if there  are no users
'''

######################## BEGIN SETUP ######################
def setup():
    reset_data()

    user_dict1 = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = user_dict1['token']
    u_id = user_dict1['u_id']

    return u_token, u_id
##########################    END SETUP   ########################

# Test list with one user
def test_user_listall_1():
    u_token, u_id = setup()
    assert(user_listall(u_token) =={'users': [{'email': 'person1@gmail.com',
        'handle_str': 'personone',
        'name_first': 'person',
        'name_last': 'one',
        'profile_img_url': None,
        'u_id': 101}]})

# Test list with two users
def test_user_listall_2():
    u_token, u_id = setup()

    user_dict2 = auth_register("person2@gmail.com", "password2", "person2", "two")
    u_token2 = user_dict2['token']
    u_id2 = user_dict2['u_id']

    assert(user_listall(u_token) == {'users': [{'email': 'person1@gmail.com',
        'handle_str': 'personone',
        'name_first': 'person',
        'name_last': 'one',
        'profile_img_url': None,
        'u_id': 101},
        {'email': 'person2@gmail.com',
        'handle_str': 'person2two',
        'name_first': 'person2',
        'name_last': 'two',
        'profile_img_url': None,
        'u_id': 102}]}
)

# Test list with three users
def test_user_listall_3():
    u_token, u_id = setup()

    user_dict2 = auth_register("person2@gmail.com", "password2", "person2", "two")
    u_token2 = user_dict2['token']
    u_id2 = user_dict2['u_id']


    user_dict3 = auth_register("person3@gmail.com", "password3", "person3", "three")
    u_token3 = user_dict3['token']
    u_id3 = user_dict3['u_id']

    assert(user_listall(u_token) == {'users': [{'email': 'person1@gmail.com',
        'handle_str': 'personone',
        'name_first': 'person',
        'name_last': 'one',
        'profile_img_url': None,
        'u_id': 101},
        {'email': 'person2@gmail.com',
        'handle_str': 'person2two',
        'name_first': 'person2',
        'name_last': 'two',
        'profile_img_url': None,
        'u_id': 102},
        {'email': 'person3@gmail.com',
        'handle_str': 'person3three',
        'name_first': 'person3',
        'name_last': 'three',
        'profile_img_url': None,
        'u_id': 103}]})
