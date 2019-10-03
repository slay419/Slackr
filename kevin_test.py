import pytest

# Given a channel ID, the user removed as a member of this channel
channel_leave(token, channel_id)
return NULL
'''
ValueError when:
    Channel (based on ID) does not exist
'''
# Given a channel_id of a channel that the authorised user can join, adds them to that channel
channel_join(token, channel_id)
return NULL
'''
ValueError when:
    Channel (based on ID) does not exist
AccessError when:
    channel_id refers to a channel that is private (when the authorised user is not an admin)
'''

# Make user with user id u_id an owner of this channel
channel_addowner(token, channel_id, u_id)
return NULL
'''
ValueError when:
    Channel (based on ID) does not exist
    user with user id u_id is already an owner of the channel
AccessError when:
    the authorised user is not an owner of the slackr, or an owner of this channel
'''


# Remove user with user id u_id an owner of this channel
channel_removeowner(token, channel_id, u_id)
return NULL
'''
ValueError when:
    Channel (based on ID) does not exist
    user with user id u_id is not an owner of the channel
AccessError when:
    the authorised user is not an owner of the slackr, or an owner of this channel
'''
# Provide a list of all channels (and their associated details) that the authorised user is part of
channels_list(token)
return {channels} # list of dictionary with {id: ' ', name: ' '}


# Provide a list of all channels (and their associated details)
channels_listall(token)
return {channels}  # list of dictionary with {id: ' ', name: ' '}



# Creates a new channel with that name that is either a public or private channel
channels_create(token, name, is_public)
return {channel_id} # integer
'''
ValueError when:
    Name is more than 20 characters long
'''

# Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
message_sendlater(token, channel_id, message, time_sent)
return NULL
'''
ValueError when:
    Channel (based on ID) does not exist
    Message is more than 1000 characters
    Time sent is a time in the past
'''
