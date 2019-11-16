from datetime import datetime, timedelta
from .message_functions import message_send
from .exceptions import ValueError, AccessError
from .data import get_data, decode_token, user_dict, channel_dict, is_member, format_message, standup_string_messages

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

    owner_perm_id = 1
    admin_perm_id = 2
    member_perm_id = 3

    # Check if the permissons are valid
    if permission_id != owner_perm_id and permission_id != admin_perm_id and permission_id != member_perm_id:
        raise ValueError(f"Invalid permission id change: {permission_id} requested")

    # Retrieve data
    caller_id = decode_token(token)
    caller_user = user_dict(caller_id)
    secondary_user = user_dict(u_id)
    # Check if the user being called is valid
    if secondary_user is None:
        raise ValueError(f"User ID: {u_id} does not refer to a valid user")

    caller_permission = caller_user['permission_id']

    # Members not allowed to change anyones permission
    if caller_permission == member_perm_id:
        raise AccessError(f"Authorised user: {caller_id} is not an admin or owner")
    # Only owner's can moidify other owners permission.
    # If caller is admin instead, then the secondary user cannot be an owner
    if caller_permission == owner_perm_id or secondary_user['permission_id'] != owner_perm_id:
        secondary_user['permission_id'] = permission_id
    else:
        raise AccessError("Admin cannot change owner permissions")

    return {}

def standup_start(token, channel_id, length):


    # Check if the channel exists and if the user is part of the channel
    if channel_dict(channel_id) is None:
        raise ValueError(f"Channel ID: {channel_id} does not exist")
    if is_member(decode_token(token), channel_id) is False:
        raise AccessError(f"Authorised User: {decode_token(token)} is not a member of the channel")
    # Retrieve data
    channel_handler = channel_dict(channel_id)
    # If no standup is running, start a standup and calculate the end time
    if channel_handler['standup_active'] is False:
        channel_handler['standup_active'] = True
        # Using datetime, fetch the current time and calculate the end time
        end_time = datetime.now() + timedelta(seconds=length)
        end_time_str = end_time.strftime("%H:%M:%S")
        # Print the time for debugging
        print("The standup has begun, and will stop at: ")
        print(end_time_str)
        timestamp = end_time.replace().timestamp()
        channel_handler['standup_end'] = timestamp
        return {'time_finish': timestamp}
    raise ValueError(f"Standup already running on this channel ID: {channel_id}")



def standup_send(token, channel_id, message):


    u_id = decode_token(token)
    # Retrieve data
    channel_handler = channel_dict(channel_id)
    # Check if the channel exists
    if channel_dict(channel_id) is None:
        raise ValueError(f"Channel ID: {channel_id} does not exist")
    # Check if the message is valid
    if len(message) > 1000:
        raise ValueError("Message is more than 1000 characters long")
    if len(message) < 1:
        raise ValueError("Message cannot be empty")
    # Check if the user is a member, and if there is a standup active
    if is_member(u_id, channel_id) is False:
        raise AccessError(f"Authorised User: {u_id} is not a member of the channel")
    if channel_handler['standup_active'] is False:
        raise ValueError(f"There is no standup running in channel ID: {channel_id}")

    # Format message in the style of a standup as required
    full_message = format_message(u_id, message)

    channel_handler['standup_queue'].append(full_message)
    return{}

def standup_active(token, channel_id):

    # Check if the channel exists and if the user is a valid member
    if channel_dict(channel_id) is None:
        raise ValueError(f"Channel ID: {channel_id} does not exist")
    if is_member(decode_token(token), channel_id) is False:
        raise AccessError(f"Authorised User: {decode_token(token)} is not a member of the channel")

    channel_handler = channel_dict(channel_id)
    # Retrieve current datetime and check if it is later on
    now_time = datetime.now()
    compare_time = now_time.replace().timestamp()
    # If no standup running, set the flag to true
    if compare_time < channel_handler['standup_end']:
        channel_handler['standup_active'] = True
        return {
            'is_active': True,
            'time_finish': channel_handler['standup_end']
        }
    else:
        # If the standup just finishes, return a list of messages
        if channel_handler['standup_active']:
            new_message = standup_string_messages(channel_id)
            message_send(token, channel_id, new_message)
            channel_handler['standup_queue'].clear()
        # Set the flag to false and return
        channel_handler['standup_active'] = False
        return {
            'is_active': False,
            'time_finish': channel_handler['standup_end']
        }
