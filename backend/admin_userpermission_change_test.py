from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list
from functions.misc_functions import admin_userpermission_change
from functions.profile_functions import user_profile, user_profile_sethandle, user_profile_setemail

from functions.data import *

import pytest

'''
####################### ASSUMPTIONS ######################
Assume the caller of this function is either an admin or owner to successfully work
Assume permission_id is either 1,2,3 as specified by data table
Assume changing the permissions of a user to be the same does not return an error

#ADMIN slackr permssion_id 1 - First user to sign up
#OWNER slackr permission_id 2 - Share same priviliges as admin but cant change
admin's permission_id
#MEMBER permission_id 3
'''


# Test if the user id is not valid
def test_admin_userpermission_change_1():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']
	invalid_u_id = admin_id + 1
	with pytest.raises(ValueError):
		admin_userpermission_change(admin_token, invalid_u_id, 1)

# Test if the permission is not valid
def test_admin_userpermission_change_2():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']
	with pytest.raises(ValueError):
		admin_userpermission_change(admin_token, admin_id, 50)

# Test if the permission is not valid
def test_admin_userpermission_change_3():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']
	with pytest.raises(ValueError):
		admin_userpermission_change(admin_token, admin_id, -30)

# Test if the user is a member and calls the function
def test_admin_userpermission_change_4():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']

	memberDict = auth_register("member@gmail.com", "password", "member", "privileges")
	member_token = memberDict['token']
	member_id = memberDict['u_id']
	with pytest.raises(AccessError):
		admin_userpermission_change(member_token, member_id, 3)

# Test if the user has permission 
def test_admin_userpermission_change_5():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']
	admin_userpermission_change(admin_token, admin_id, 1)
	assert(get_permission_id(admin_id) == 1)

# Test if the user has permission
def test_admin_userpermission_change_6():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']
	admin_userpermission_change(admin_token, admin_id, 2)
	assert(get_permission_id(admin_id) == 2)


# owner cant change admin user permsssion
def test_admin_userpermission_change_7():
	reset_users()
	adminDict = auth_register("admin@gmail.com", "password", "admin", "privileges")
	admin_token = adminDict['token']
	admin_id = adminDict['u_id']

	memberDict = auth_register("member@gmail.com", "password", "member", "privileges")
	member_token = memberDict['token']
	member_id = memberDict['u_id']

	#admin changes member to owner (permission_id 3 --> 2)
	admin_userpermission_change(admin_token, member_id, 2)
	owner_token = member_token 
	owner_id = member_id

	#owner tries to change admin's permission (LOL)
	with pytest.raises(AccessError):
		admin_userpermission_change(owner_token, admin_id, 2)

