import pytest
from auth_login_test import auth_login 
from flask import Flask, request

from .data import *

@APP.route('user/profile/setname', methods=['PUT'])
def user_profile_setname(token, name_first, name_last):

	if len(name_first) > 50:
		raise ValueError('First name is larger than 50 character')
	if len(name_first) < 1:
		raise ValueError('First name is less than 1 character')	
	if len(name_last) > 50:
		raise ValueError('Last name is larger than 50 characters')
	if len(name_last) < 1:
		raise ValueError('Last name is less than 1 character')		
	
	data['name_first'] = name_first
	data['name_last'] = name_last

	pass
