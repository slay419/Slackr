from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail

from functions.data import *

from functions.exceptions import ValueError, AccessError

import pytest

###SIDE NOTE: Web resources were used in order to create the basic algorithm to determine
### what a valid email is

'''
####################### ASSUMPTIONS #####################
Assume the current email used is valid and not empty
Assume normal protocol for what is a valid email applies, i.e what is already specified
by other interenet algorithms
Assume the function returns a ValueError if the string is empty
'''

# Testing an invalid email
def test_user_profile_setemail_1():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_setemail(u_token, 'myemail.com')

# Testing an empty email
def test_user_profile_setemail_2():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	with pytest.raises(ValueError):
		user_profile_setemail(u_token, '')

# Testing an long but valid email
def test_user_profile_setemail_3():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setemail(u_token, 'abcdefghijklmnopqrstuvwxyz@email.com')
	assert (user_profile(u_token, u_id) == {
        'email' : 'abcdefghijklmnopqrstuvwxyz@email.com',
        'name_first' : 'firstname',
        'name_last' : 'lastname',
        'handle_str' : 'firstnamelastname'
    })

# Testing an short but valid email
def test_user_profile_setemail_4():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "firstname", "lastname")
	u_token = userDict['token']
	u_id = userDict['u_id']
	user_profile_setemail(u_token, 'abc@email.com')
	assert (user_profile(u_token, u_id) == {
        'email' : 'abc@email.com',
        'name_first' : 'firstname',
        'name_last' : 'lastname',
        'handle_str' : 'firstnamelastname'
    })

# Testing a email that is being used
def test_user_profile_setemail_5():
	reset_users()
	userDict = auth_register("person1@gmail.com", "password", "person", "one")
	userDict2 = auth_register("person2@gmail.com", "password", "person2", "two")
	u_token2 = userDict2['token']
	with pytest.raises(ValueError):
		user_profile_setemail(u_token2, 'person1@gmail.com')
