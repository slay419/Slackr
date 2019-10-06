import pytest
from auth_login_test import auth_login
import requests

'''
####################### ASSUMPTIONS ######################
Assume the caller of this function is either an admin or owner to successfully work
Assume permission_id is either 1,2,3 as specified by data table
Assume changing the permissions of a user to be the same does not return an error
'''

## This function does:
## Given a User by their user ID, set their permissions to
## new permissions described by permission_id

## Function will fail if:
## 1. u_id does not refer to a valid user
## 2. permission_id does not refer to a value permission
## 3. The authorised user is not an admin or owner

def admin_userpermission_change(token,u_id,permission_id)
	
	if valid_u_id(u_id) is 0:
    	raise ValueError("u_id does not refer to a valid user")
  	if permission_id is not 1 or is not 2 or is not 3:
      	raise ValueError("Permission_id does not refer to a value permission")
    if permission_id is 3:
      	raise AttributeError("The authorised user is not an admin or owner")
	
'''
If the user id is valid, return 1
If the user id is invalid, return 0
'''
def valid_u_id(u_id):
	pass

'''
If the user is an owner, return 1
If the user is an admin, return 2
if the user is a member, return 3
'''
def is_permission(u_id):
	pass

######################## GLOBAL VARIABLES SETUP ######################
# First user
userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']
user1_id = userDict1['u_id']

invalid_u_id = 123

##########################    END SETUP   ########################

# Test if the user id is not valid
def admin_userpermission_change_1()
	with pytest.raises(ValueError):
		admin_userpermission_change(u_token, invalid_u_id, 1)

# Test if the permission is not valid
def admin_userpermission_change_2()
	with pytest.raises(ValueError):	
		admin_userpermission_change(u_token, user1_id, 50)

# Test if the permission is not valid
def admin_userpermission_change_3()
	with pytest.raises(ValueError):	
		admin_userpermission_change(u_token, user1_id, -30)

# Test if the user is a member and calls the function
def admin_userpermission_change_4()
	with pytest.raises(AttributeError):
		admin_userpermission_change(u_token, user1_id, 3)
	
# Test if the use has permission
def admin_userpermission_change_5()
	admin_userpermission_change(u_token, user1_id, 1)
	assert(is_permission(user1_id) == 1)

# Test if the use has permission
def admin_userpermission_change_6()
	admin_userpermission_change(u_token, user1_id, 2)
	assert(is_permission(user1_id) == 2)
