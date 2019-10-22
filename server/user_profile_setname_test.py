import pytest
from auth_login_test import auth_login 
from flask import Flask, request

from .data import *

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

@APP.route('user/profile/setname', methods=['PUT'])
def user_profile_setname(token, name_first, name_last):
	pass


######################## GLOBAL VARIABLES SETUP ######################

userDict = auth_login("person1@gmail.com", "password")
u_token = userDict['token']


##########################    END SETUP   ########################

# Test that first name is greater than 50 characters
def test_user_profile_setname_1():
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 51*'A', 'Smith')

# Test that last name is greater than 50 characters
def test_user_profile_setname_2():
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 'John', 51*'A')
		
# Test that first name is exactly 50 characters
def test_user_profile_setname_3():
	
	user_profile_setname(u_token, 50*'A', 'Chen')

# Test that last name is exactly 50 characters
def test_user_profile_setname_4():
	
	user_profile_setname(u_token, 'Peter', 50*'A')
	
# Test that first name is exactly 49 characters
def test_user_profile_setname_5():
	
	user_profile_setname(u_token, 49*'A', 'Smith')

# Test that last name is exactly 49 characters
def test_user_profile_setname_6():
	
	user_profile_setname(u_token, 'Hayden', 49*'A')

# Test that first name that has special characters
def test_user_profile_setname_7():
	
	user_profile_setname(u_token, '!@#$%^&*()+_-=|/\}{][;:?><~""', 'Smith')

# Test that last name that has special characters
def test_user_profile_setname_8():
	
	user_profile_setname(u_token, 'John', '!@#$%^&*()+_-=|/\}{][;:?><~""')

# Test a mix of special characters and letters
def test_user_profile_setname_9():
	
	user_profile_setname(u_token, 'John!@#$%^&*()', 'Smith')

# Test a mix of special characters and letters
def test_user_profile_setname_10():
	
	user_profile_setname(u_token, 'John', 'Smith!@#$%^&*()')
		
# Test a valid name
def test_user_profile_setname_11():
	
	user_profile_setname(u_token, 'John', 'Smith')

# Test when the first name is empty
def test_user_profile_setname_12():
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, '', 'Smith')
		
# Test when the last name is empty
def test_user_profile_setname_13():
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 'John', '')
		