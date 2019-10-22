import pytest
# re module provides support 
# for regular expressions 
import re
from auth_login_test import auth_login 
from flask import Flask, request

from .data import *

###SIDE NOTE: Web resources were used in order to create the basic algorithm to determine
### what a valid email is

def user_profile_setemail(token, email):
	
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
      
	# Define a function for 
	# for validating an Email 
	def check(email):  
  
		# pass the regualar expression 
		# and the string in search() method 
		if(re.search(regex,email)):  
			pass
		else:  
			raise ValueError("Email entered is not a valid email") 	
	
		if is_email_free(email) == 0:
			raise ValueError("Email is already in use")
		pass

	
	
'''
Returns 1 if the email is free to use
Returns 0 if the email is being used
'''
def is_email_free(email):
	data = get_users()
	for user in data:
		if user['email'] is email:		
			return 0	
	user['email'] = email
	return 1