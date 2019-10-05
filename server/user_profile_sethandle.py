import pytest
from auth_login_test import auth_login 


'''
####################### ASSUMPTIONS #####################
Assume special characters should be valid
Assume numbers should be valid
Assume the user is authorised to call the function
Assume two people can have the same handle
Assume the function returns a value error when 0 characters are entered
'''


## This function does:
## Update the authorised user's handle (i.e. display name)

## Function will fail if:
## 1. Handle > 20 characters

def user_profile_setname(token, handle_str):
	if len(handle_str) > 20:
		raise ValueError("Handle is larger than 20 characters")
	if len(handle_str) < 1:
		raise ValueError("Handle is less than 1 character")	
	pass
	
######################## GLOBAL VARIABLES SETUP ######################

userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']

##########################    END SETUP   ########################

#Test a handle larger than 20 characters
def test_user_profile_setname_1():
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 20*'JohnnySmith')
		
#Test a handle with 21 characters
def test_user_profile_setname_2():
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 21*'A')

#Test a handle with 20 characters
def test_user_profile_setname_3():
	user_profile_setname(u_token, 20*'A')		
	
#Test a handle with 19 characters
def test_user_profile_setname_4():
	user_profile_setname(u_token, 19*'A')
	
#Test a handle with too many special characters
def test_user_profile_setname_5():
	with pytest.raises(ValueError):
		user_profile_setname(u_token, '!@#$%^&*()+_-=|/\{}[];:?><~""')

#Test a handle with 20 special characters
def test_user_profile_setname_6():
	user_profile_setname(u_token, '!@#$%^&*()+_-=|/\{}?')

#Test a handle with 0 characters
def test_user_profile_setname_7():
	with pytest.raises(ValueError):
		user_profile_setname(u_token, '')
