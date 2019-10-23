from .data import *

# Returns messages featuring the 'query_str' keyword from
# channels that the user is part of
def search(token, query_str):
	data = get_data()

	messages = []

	for channel in channels_list(token):
		for message in data['channels']['messages']:
			if query_str in data['messages']['message']:
				message.append(data['messages']['message'])
	
	return messages

def admin_userpermission_change(token, u_id, permission_id):
	data = get_data()

	callersPermission = 0

	myID = decode_token(token)
	for user in data['users']:
		if myID == data['users']['u_id']:
			callersPermission = data['users']['permission_id']

	if valid_u_id(u_id) is 0:
    	raise ValueError("u_id does not refer to a valid user")
  	if callersPermission is not 1 or is not 2 or is not 3:
      	raise ValueError("Permission_id does not refer to a value permission")
    if callersPermission is 3:
      	raise AttributeError("The authorised user is not an admin or owner")

	# At this point, the caller is authorised to make changes
	# it is also assured the target user is valid

	for user in data['users']:
		if u_id == data['users']['u_id']:
			data['users']['permission_id'] = permission_id
			print("Successfully updated user's permissions")

	return {}
	