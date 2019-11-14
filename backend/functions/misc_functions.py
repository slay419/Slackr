from .data import *
from datetime import datetime, timedelta, timezone
from .message_functions import message_send

# Returns messages featuring the 'query_str' keyword from
# channels that the user is part of
def search(token, query_str):
	data = get_data()
	messages = []
	# Loop through each message and find the sub-string
	for message_dict in data['messages']:
		if query_str in message_dict['message']:
			messages.append(message_dict)

	return {'messages': messages}

def admin_userpermission_change(token, u_id, permission_id):
	# Check if the permissons are valid
	if permission_id != 1 and permission_id != 2 and permission_id != 3:
		raise ValueError(f"Invalid permission id change: {permission_id} requested")

	# Retrieve data
	caller_id = decode_token(token)
	caller_user = user_dict(caller_id)
	secondary_user = user_dict(u_id)
	# Check if the user
	if secondary_user == None:
		raise ValueError(f"User ID: {u_id} does not refer to a valid user")

	caller_permission = caller_user['permission_id']
	# Check if the operation is valid
	if caller_permission == 3:
		raise AccessError(f"Authorised user: {caller_id} is not an admin or owner")
	# Change permissions, unless already an admin
	if caller_permission == 1 or secondary_user['permission_id'] != 1:
		secondary_user['permission_id'] = permission_id
	else:
		raise AccessError("Owner cannot change admin permissions")

	return {}

def standup_start(token, channel_id, length):

	data = get_data()
	# Check if the channel exists and if the user is part of the channel
	if channel_dict(channel_id) is None:
		raise ValueError(f"Channel ID: {channel_id} does not exist")
	if is_member(decode_token(token), channel_id) is False:
		raise AccessError(f"Authorised User: {decode_token(token)} is not a member of the channel")
	# Retrieve data
	channelHandler = channel_dict(channel_id)
	# If no standup is running, start a standup and calculate the end time
	if channelHandler['standup_active'] is False:
		channelHandler['standup_active'] = True
		# Using datetime, fetch the current time and calculate the end time		
		EndTime = datetime.now() + timedelta(seconds=length)
		EndTimeStr = EndTime.strftime("%H:%M:%S")
		# Print the time for debugging
		print("The standup has begun, and will stop at: ")
		print(EndTimeStr)
		timestamp = EndTime.replace().timestamp()
		channelHandler['standup_end'] = timestamp
		return {'time_finish': timestamp}
	else:
		raise ValueError(f"Standup already running on this channel ID: {channel_id}")



def standup_send(token, channel_id, message):

	data = get_data()
	u_id = decode_token(token)
	# Retrieve data
	channelHandler = channel_dict(channel_id)
	# Check if the channel exists
	if channel_dict(channel_id) is None:
		raise ValueError(f"Channel ID: {channel_id} does not exist")
	# Check if the message is valid
	if len(message) > 1000:
		raise ValueError ("Message is more than 1000 characters long")
	if len(message) < 1:
		raise ValueError ("Message cannot be empty")
	# Check if the user is a member, and if there is a standup active
	if is_member(u_id ,channel_id) is False:
		raise AccessError(f"Authorised User: {u_id} is not a member of the channel")
	if channelHandler['standup_active'] is False:
		raise ValueError (f"There is no standup running in channel ID: {channel_id}")
	# Modify the message to accomodate more info
	FullMessage = ""
	FullMessage += str(get_first_name(u_id))
	FullMessage += ": "
	FullMessage += str(message)
	FullMessage += "\n"

	channelHandler['standup_queue'].append(FullMessage)
	return{}

def standup_active(token, channel_id):
	data = get_data()
	# Check if the channel exists and if the user is a valid member
	channelHandler = channel_dict(channel_id)
	if channel_dict(channel_id) is None:
		raise ValueError(f"Channel ID: {channel_id} does not exist")
	if is_member(decode_token(token), channel_id) is False:
		raise AccessError(f"Authorised User: {decode_token(token)} is not a member of the channel")

	channelHandler = channel_dict(channel_id)
	# Retrieve current datetime and check if it is later on
	NowTime = datetime.now()
	CompareTime = NowTime.replace().timestamp()
	# If no standup running, set the flag to true
	if CompareTime < channelHandler['standup_end']:
		channelHandler['standup_active'] = True
		return {
			'is_active': True,
			'time_finish': channelHandler['standup_end']
		}
	else:
		# If the standup just finishes, return a list of messages
		if channelHandler['standup_active'] == True:
			newMessage = ""
			for messageSummary in channelHandler['standup_queue']:
				newMessage += messageSummary
			message_send(token, channel_id, newMessage)
		# Set the flag to false and return
		channelHandler['standup_active'] = False
		return {
			'is_active': False,
			'time_finish': channelHandler['standup_end']
		}
