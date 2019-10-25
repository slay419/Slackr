from .data import *
from datetime import datetime, timedelta, timezone

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
	if permission_id != 1 and permission_id != 2 and permission_id != 3:
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

def standup_start(token, channel_id):

	data = get_data()

	if channel_dict(channel_id) is None:
		raise ValueError("Channel does not exist")
	if is_member(decode_token(token), channel_id) is False:
		raise AccessError("Authorised User is not a member of the channel")

	channelHandler = channel_dict(channel_id)

	if channelHandler['standup_active'] is False:
		channelHandler['standup_active'] = True
		# Change 15 down for debugging purposes if needed
		EndTime = datetime.now() + timedelta(minutes=15)
		EndTimeStr = EndTime.strftime("%H:%M:%S")
		print("The standup has begun, and will stop at: ")
		print(EndTimeStr)
	else:
		raise AccessError("Standup already running on this channel")
		return {}

	timestamp = EndTime.replace(tzinfo=timezone.utc).timestamp()
	return timestamp

def standup_send(token, channel_id, message):

	data = get_data()

	channelHandler = channel_dict(channel_id)

	if channel_dict(channel_id) is None:
		raise ValueError("Channel does not exist")
	if len(message) > 1000:
		raise ValueError ("Message more than 1000 characters")
	if len(message) < 1:
		raise ValueError ("Message empty")
	if is_joined(token ,channel_id) is False:
		raise AttributeError("Authorised User is not a member of the channel")
	if channelHandler['standup_active'] is False:
		raise ValueError ("There is no standup running in this channel")

	channelHandler['standup_queue'].append(message)

	return{}
