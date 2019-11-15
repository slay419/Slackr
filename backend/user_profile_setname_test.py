from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail, user_profile_setname

from functions.data import *

from functions.exceptions import ValueError, AccessError

import pytest

## This function does:
## Update the authorised user's first and last name

## Function will fail if:
## 1. First name > 50 characters
## 2. Last name > 50 characters

'''
####################### ASSUMPTIONS #####################
Assume special characters should be valid
Assume numbers should be valid
Assume the user is authorised to call the function
Assume the function returns a value error when 0 characters are entered
'''


# Test that first name is greater than 50 characters
def test_user_profile_setname_1():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 51*'A', 'Smith')

# Test that last name is greater than 50 characters
def test_user_profile_setname_2():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 'John', 51*'A')

# Test that first name is exactly 50 characters
def test_user_profile_setname_3():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 50*'A', 'Chen')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 50*'A',
        'name_last' : 'Chen',
        'handle_str' : 'firstnamelastname'
    })

# Test that last name is exactly 50 characters
def test_user_profile_setname_4():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 'Peter', 50*'A')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'Peter',
        'name_last' : 50*'A',
        'handle_str' : 'firstnamelastname'
    })

# Test that first name is exactly 49 characters
def test_user_profile_setname_5():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 49*'A', 'Smith')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 49*'A',
        'name_last' : 'Smith',
        'handle_str' : 'firstnamelastname'
    })

# Test that last name is exactly 49 characters
def test_user_profile_setname_6():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 'Hayden', 49*'A')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'Hayden',
        'name_last' : 49*'A',
        'handle_str' : 'firstnamelastname'
    })

# Test that first name that has special characters
def test_user_profile_setname_7():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, '!@#$%^&*()+_-=|/\}{][;:?><~""', 'Smith')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : '!@#$%^&*()+_-=|/\}{][;:?><~""',
        'name_last' : 'Smith',
        'handle_str' : 'firstnamelastname'
    })

# Test that last name that has special characters
def test_user_profile_setname_8():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 'John', '!@#$%^&*()+_-=|/\}{][;:?><~""')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'John',
        'name_last' : '!@#$%^&*()+_-=|/\}{][;:?><~""',
        'handle_str' : 'firstnamelastname'
    })

# Test a mix of special characters and letters
def test_user_profile_setname_9():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 'John!@#$%^&*()', 'Smith')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'John!@#$%^&*()',
        'name_last' : 'Smith',
        'handle_str' : 'firstnamelastname'
    })

# Test a mix of special characters and letters
def test_user_profile_setname_10():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 'John', 'Smith!@#$%^&*()')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'John',
        'name_last' : 'Smith!@#$%^&*()',
        'handle_str' : 'firstnamelastname'
    })

# Test a valid name
def test_user_profile_setname_11():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setname(u_token, 'John', 'Smith')
	assert (user_profile(u_token, u_id) == {
        'email' : 'person1@gmail.com',
        'name_first' : 'John',
        'name_last' : 'Smith',
        'handle_str' : 'firstnamelastname'
    })

# Test when the first name is empty
def test_user_profile_setname_12():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	with pytest.raises(ValueError):
		user_profile_setname(u_token, '', 'Smith')

# Test when the last name is empty
def test_user_profile_setname_13():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 'John', '')
