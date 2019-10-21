
'''
####################### ASSUMPTIONS ######################
Assume the person who created the channel is the owner and has authority to promote
others to owner as well
Assume that the u_id being promoted has already joined the channel but as a member
Assume "invalid channel id" means they have not joined the channel yet OR it has not been created yet

Admins are the very first person to sign up to slackr
Admin privileges cover all of slackr
Owners are the first person to create the channel
Owner privileges cover ONLY their channel created
'''

def channel_addowner(token, channel_id, u_id):
    channel = channel_dict(channel_id)
    u_id = decode_token(token)
    print(channel)
    # append user to list of owners
    channel['owners'].append(u_id)
    print(channel)
    return {}
