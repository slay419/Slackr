from .data import *

def user_profile_setemail(token, email):
	data = get_users()
	myID = decode_token(token)
	
	if valid_email(email) is False:
		raise ValueError("Email entered is not a valid email")
	if is_email_free(email) == 0:
		raise ValueError("Email is already in use")
	# At this point, the email is valid and untaken
	for user in data['users']:
		if myID == data['users']['u_id']:
			data['users']['email'] = email
			print("Successfully updated user's email")

	return {}

	
	
## Returns 1 if the email is free to use
## Returns 0 if the email is being used

def is_email_free(email):
	for user in data['users']:
		if data['users']['email'] is email:		
			return 0	
	return 1

def user_profile_sethandle(token, handle_str):
	data = get_users()
	if len(handle_str) > 20:
		raise ValueError("Handle is larger than 20 characters")
	if len(handle_str) < 1:
		raise ValueError("Handle is less than 1 character")	

	myID = decode_token(token)
	for user in data['users']:
		if myID == data['users']['u_id']:
			data['users']['handle'] = handle_str
			print("Successfully updated user's handle")

	return {}

def user_profile_setname(token, name_first, name_last):

	data = get_users()

	if len(name_first) > 50:
		raise ValueError('First name is larger than 50 character')
	if len(name_first) < 1:
		raise ValueError('First name is less than 1 character')	
	if len(name_last) > 50:
		raise ValueError('Last name is larger than 50 characters')
	if len(name_last) < 1:
		raise ValueError('Last name is less than 1 character')	

	myID = decode_token(token)
	for user in data['users']:
		if myID == data['users']['u_id']:
			data['users']['name_first'] = name_first
			data['users']['name_last'] = name_last
			print("Successfully updated user's first and last name")

	return {}

def user_profile(token,u_id):

	data = get_users()

	valid = 0

	for user in data['users']:
		if u_id == data['users']['u_id']:
			valid = 1

	if valid == 0:
		raise ValueError("User ID does not exist")
		return
	else:
		for user in data['users']:
			if data['users']['u_id'] == u_id:
				new_dict = {email:data['users']['email'], name_first:data['users']['firstName'], name_last:data['users']['lastName'], handle_str:user["handle"]}
	print("Successfully found and located user's information")
	return new_dict	#returns dict containing {email,name_first,name_last,handle_str}
