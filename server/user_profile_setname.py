import pytest
from auth_login_test import auth_login

## This function does:
## Update the authorised user's first and last name

## Function will fail if:
## 1. First name > 50 characters
## 2. Last name > 50 characters

def user_profile_setname(token, name_first, name_last)
	if len(name_first) > 50:
		raise ValueError("First name is larger than 50 characters")
	if len(name_last) > 50:
		raise ValueError("Last name is larger than 50 characters")
	pass


def test_name_first_fails():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	
	with pytest.raises(ValueError):
		user_profile_setname(intendedUser, 50*'John', 'Smith')

def test_name_last_fails():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	
	with pytest.raises(ValueError):
		user_profile_setname(intendedUser, 'John', 50*'Smith')