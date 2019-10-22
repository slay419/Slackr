from data import *

def user_profile_setemail(token, email):
	
	regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
	  
	# pass the regualar expression 
	# and the string in search() method 
	if(re.search(regex,email)):
		pass
	else:
		raise ValueError("Email entered is not a valid email")
	if is_email_free(email) == 0:
		raise ValueError("Email is already in use")
	return {}

	
	
## Returns 1 if the email is free to use
## Returns 0 if the email is being used

def is_email_free(email):
	data = get_users()
	for user in data:
		if user['email'] is email:		
			return 0	
	user['email'] = email
	return 1

def user_profile_sethandle(token, handle_str):
	data = get_users()
	if len(handle_str) > 20:
		raise ValueError("Handle is larger than 20 characters")
	if len(handle_str) < 1:
		raise ValueError("Handle is less than 1 character")	

	data['handle'] = handle_str
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
	
	data['name_first'] = name_first
	data['name_last'] = name_last

	return {}

def user_profile(token,u_id):

	data = get_users()

	if u_id in data:
		valid = 1

	if valid is 0:
		raise ValueError("User ID does not exist")
		return
	else:
		for user in data:
			if user['u_id'] is u_id:
				new_dict = {email:user["email"], name_first:user["firstName"], name_last:user["lastName"], handle_str:user["handle"]}

	return new_dict	#returns dict containing {email,name_first,name_last,handle_str}
