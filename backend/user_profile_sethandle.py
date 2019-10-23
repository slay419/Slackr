import pytest
from auth_login_test import auth_login 
from flask import Flask, request

from .data import *

@APP.route('user/profile/sethandle', methods=['PUT'])
def user_profile_sethandle(token, handle_str):
	data = get_users()
	if len(handle_str) > 20:
		raise ValueError("Handle is larger than 20 characters")
	if len(handle_str) < 1:
		raise ValueError("Handle is less than 1 character")	

	data['handle'] = handle_str
	pass