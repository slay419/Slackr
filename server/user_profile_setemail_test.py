import pytest
# re module provides support 
# for regular expressions 
import re
from auth_login_test import auth_login 
from flask import Flask, request

from .data import *

###SIDE NOTE: Web resources were used in order to create the basic algorithm to determine
### what a valid email is

'''
####################### ASSUMPTIONS #####################
Assume the current email used is valid and not empty
Assume normal protocol for what is a valid email applies, i.e what is already specified
by other interenet algorithms
Assume the function returns a ValueError if the string is empty
'''


## This function does:
## Update the authorised user's email address

## Function will fail if:
## 1. Email entered is not a valid email.
## 2. Email address is already being used by another user

def user_profile_setemail(token, email):
	pass
'''
Returns 1 if the email is free to use
Returns 0 if the email is being used
'''

def is_email_free(email):
	pass

######################## GLOBAL VARIABLES SETUP ######################

userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']

##########################    END SETUP   ########################


# Testing an invalid email
def test_user_profile_setemail_1():
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 'myemail.com')

# Testing an empty email
def test_user_profile_setemail_2():
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, '')

# Testing an long but valid email
def test_user_profile_setemail_3():

	user_profile_setname(u_token, 'abcdefghijklmnopqrstuvwxyz@email.com')

# Testing an short but valid email
def test_user_profile_setemail_4():

	user_profile_setname(u_token, 'abc@email.com')
	
# Testing a email that is being used
def test_user_profile_setemail_5():
	userDict2 = auth_register("person2@gmail.com", "password", "person2", "two")
	u_token2 = userDict2['token']
	
	with pytest.raises(ValueError):
		user_profile_setname(u_token, 'person2@gmail@gmail.com')