from .data import *
'''
####################### ASSUMPTIONS ######################
Assume can only demote an owner if they are already an owner and have joined the
channel previously
Assume "invalid channel id" means they have not joined the channel OR it has not been created yet
Assume cannot demote the ONLY owner of the channel since there would be no owner to promote others

Admins are the very first person to sign up to slackr
Admin privileges cover all of slackr
Owners are the first person to create the channel
Owner privileges cover ONLY their channel created
'''

def channel_removeowner(token, channel_id, u_id):
    channel = channel_dict(channel_id)
    print(f"channel owners are: {channel['owners']}")
    # remove user from list of owners
    channel['owners'].remove(u_id)
    print(f"channel owners are: {channel['owners']} after removing")
    return {}
