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
	if permission_id != 1 or permission_id != 2 or permission_id != 3:
		return "invalid permission id change requested"

	caller_id = decode_token(token)
	caller_user = user_dict(caller_id)
	secondary_user = user_dict(u_id)
	if secondary_user == None:
		return "u_id does not refer to a valid user"

	caller_permission = caller_user['permission_id']
	if caller_permission == 3:
		return "authorised user is not an admin or owner"

	if caller_permission == 1 or secondary_user['permission_id'] != 1:
		secondary_user['permission_id'] = permission_id
	else:
		return "owner cannot change admin permissions"

	return {}


	