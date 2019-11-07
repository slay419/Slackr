from .data import *

def user_profile_setemail(token, email):
	data = get_data()
	u_id = decode_token(token)
	userData = user_dict(u_id)

	if userData == None:
		raise ValueError(f"User ID: {u_id} does not exist")
	if valid_email(email) is False:
		raise ValueError(f"Email: {email} entered is not a valid email")
	if is_email_free(email) == 0:
		raise ValueError(f"Email: {email} is already in use")
	# At this point, the email is valid and untaken

	userData['email'] = email
	print("Successfully updated user's email")

	return {}



## Returns 1 if the email is free to use
## Returns 0 if the email is being used

def is_email_free(email):
	for user in data['users']:
		if user['email'] == email:
			return 0
	return 1

def user_profile_sethandle(token, handle_str):
	data = get_data()
	u_id = decode_token(token)
	userData = user_dict(u_id)

	if userData == None:
		raise ValueError(f"User ID: {u_id} does not exist")
	if len(handle_str) > 20:
		raise ValueError(f"Handle: {handle_str} is larger than 20 characters")
	if len(handle_str) < 1:
		raise ValueError("Handle cannot be empty")

	userData['handle'] = handle_str
	print("Successfully updated user's handle")

	return {}

def user_profile_setname(token, name_first, name_last):
	data = get_data()
	u_id = decode_token(token)
	userData = user_dict(u_id)

	if userData == None:
		raise ValueError(f"User ID: {u_id} does not exist")
	if len(name_first) > 50:
		raise ValueError(f"First name: {name_first} is longer than 50 characters")
	if len(name_first) < 1:
		raise ValueError(f"First name: {name_first} cannot be empty")
	if len(name_last) > 50:
		raise ValueError(f"Last name: {name_last} is longer than 50 characters")
	if len(name_last) < 1:
		raise ValueError(f"Last name: {name_last} cannot be empty")

	userData['name_first'] = name_first
	userData['name_last'] = name_last
	print("Successfully updated user's first and last name")

	return {}

def user_profile(token,u_id):
	data = get_data()
	userData = user_dict(u_id)
	if userData == None:
		raise ValueError(f"User ID: {u_id} does not exist")

	new_dict = {
        'email': userData['email'],
        'name_first': userData['name_first'],
        'name_last': userData['name_last'],
        'handle_str': userData["handle"]
    }
	print("Successfully found and located user's information")
	return new_dict	#returns dict containing {email,name_first,name_last,handle_str}

def user_profile_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
	# Extract the image from the URL and store at 'filePath' location
	userCounter = 1
	filePath = "./pictures/profilepic" + str(userCounter) + ".jpg"
	urllib.request.urlretrieve(img_url,filePath)

	data = get_data()
	imageObject = Image.open(img_url)
	cropped = imageObject.crop((x_start,y_start,x_end,y_end))
	cropped.save(img_url)
