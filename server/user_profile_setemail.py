import pytest
import re
from auth_login_test import auth_login 
from auth_login_test import auth_register

## This function does:
## Update the authorised user's email address

## Function will fail if:
## 1. Email entered is not a valid email.
## 2. Email address is already being used by another user

def user_profile_setemail(token, email)
	
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      
	# Define a function for 
	# for validating an Email 
	def check(email):  
  
		# pass the regualar expression 
		# and the string in search() method 
		if(re.search(regex,email)):  
			return
			  
		else:  
			raise ValueError("Email entered is not a valid email") 
		  

	if email in #####???:
		raise ValueError("Email is already in use")
	pass


def test_not_valid_email():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	
	with pytest.raises(ValueError):
		user_profile_setname(intendedUser, 'myemail.com')

def test_in_use_email():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	
	with pytest.raises(ValueError):
		user_profile_setname(intendedUser, 'johnsmith123@gmail.com')