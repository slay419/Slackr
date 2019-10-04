import pytest
from auth_login_test import auth_login

## This function does:
## Update the authorised user's handle (i.e. display name)

## Function will fail if:
## 1. Handle > 20 characters

def user_profile_setname(token, handle_str)
	if len(handle_str) > 20:
		raise ValueError("Handle is larger than 20 characters")
	pass


def test_name_first_fails():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(ValueError):
		user_profile_setname(intendedUser, 10*'JohnnySmith')
