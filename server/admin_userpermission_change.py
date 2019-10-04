import pytest
from auth_login_test import auth_login
import requests


## This function does:
## Given a User by their user ID, set their permissions to
## new permissions described by permission_id

## Function will fail if:
## 1. u_id does not refer to a valid user
## 2. permission_id does not refer to a value permission
## 3. The authorised user is not an admin or owner

def admin_userpermission_change(token,u_id,permission_id)
	
	if u_id is 0:
    	raise ValueError("u_id does not refer to a valid user")
  	if permission_id is 0:
      	raise ValueError("Permission_id does not refer to a value permission")
    if token is 0:
      	raise AccessError("The authorised user is not an admin or owner")

def test_invalid_uid()
	userDictionary = auth_login'johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	admin_userpermission_change(intendedUser, 0, 500)

def test_invalid_pid()
	userDictionary = auth_login'johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
		admin_userpermission_change(intendedUser, 500, 0)

def test_no_auth()
	userDictionary = auth_login'johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	intendedUser = 0
	admin_userpermission_change(intendedUser, 500, 500)