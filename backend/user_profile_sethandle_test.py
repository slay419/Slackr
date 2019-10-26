from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS #####################
Assume special characters should be valid
Assume numbers should be valid
Assume the user is authorised to call the function
Assume two people can have the same handle
Assume the function returns a value error when 0 characters are entered
'''

#Test a handle larger than 20 characters
def test_user_profile_sethandle_1():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_sethandle(u_token, 20*'JohnnySmith')

#Test a handle with 21 characters
def test_user_profile_sethandle_2():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_sethandle(u_token, 21*'A')

#Test a handle with 20 characters
def test_user_profile_sethandle_3():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_sethandle(u_token, 20*'A')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'firstname',
        'name_last' : 'lastname',
        'handle_str' : 20*'A'
    })

#Test a handle with 19 characters
def test_user_profile_sethandle_4():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_sethandle(u_token, 19*'A')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'firstname',
        'name_last' : 'lastname',
        'handle_str' : 19*'A'
    })

#Test a handle with too many special characters
def test_user_profile_sethandle_5():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_sethandle(u_token, '!@#$%^&*()+_-=|/\{}[];:?><~""')

#Test a handle with 20 special characters
def test_user_profile_sethandle_6():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_sethandle(u_token, '!@#$%^&*()+_-=|/\{}?')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'firstname',
        'name_last' : 'lastname',
        'handle_str' : '!@#$%^&*()+_-=|/\{}?'
    })

#Test a handle with 0 characters
def test_user_profile_sethandle_7():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_sethandle(u_token, '')
