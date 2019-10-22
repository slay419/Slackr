
'''
####################### ASSUMPTIONS ######################
Assume you need to need to create a channel first before joining
Also you cannot join a channel you are already in
Assume "Channel does not exist" means channels you have already joined OR
channel_id hasn't been created yet

Admins are the very first person to sign up to slackr
Admin privileges cover all of slackr
Owners are the first person to create the channel
Owner privileges cover ONLY their channel created

'''

def channel_join(token, channel_id):
    if is_invalid_channel(channel_id):
        raise ValueError("Channel ID does NOT Exist")
    if is_authorised(token) == 0 and is_private(channel_id) == 1:
        raise AccessError("Cannot join a private channel as a member")
    pass

'''
Returns 1 if the channel id does not exist and is invalid
Returns 0 if the channel id otherwise
'''
def is_invalid_channel(channel_id):
    pass
