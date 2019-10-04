from error import AccessError

import pytest

'''
####################### ASSUMPTIONS ######################
Assume the person who created the channel is the owner and has authority to promote
others to owner as well
Assume that the u_id being promoted has already joined the channel but as a member

Admins are the very first person to sign up to slackr
Admin privileges cover all of slackr
Owners are the first person to create the channel
Owner privileges cover ONLY their channel created

'''

def channel_addowner(token, channel_id, u_id):
    if is_valid_channel(channel_id):
        pass
    else:
        # Cannot add an owner to a channel which does not exist
        raise ValueError("Channel ID does NOT exist.")

    if is_owner(u_id):
        # Cannot promote a user that is already an owner
        raise ValueError("User is already an owner.")

    if is_authorised(token):
        pass
    else:
        # Cannot promote a user if the person conducting the action does not have the authority
        raise AccessError("User with token is NOT an owner of Slackr or the current Channel")
    pass

'''
If the user with u_id is an owner/admin, returns 1
If the user is a member, returns 0
'''
def is_owner(u_id):
    pass


######################## GLOBAL VARIABLES SETUP ######################
# Assume owner_id is an admin since he is the first person to sign up
ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['id']

##########################    END SETUP   ########################

# Testing promoting a user to a channel that has not been created yet
def test_channel_addowner_1():
    admin_userpermission_change(owner_token, u_id, 1)
    with pytest.raises(ValueError):
        channel_addowner(owner_token, 1234, u_id)

# Testing promoting a user to the wrong channel id
def test_channel_addowner_2():
    channel_id = channels_create(owner_token, "Channel Name", True)
    channel_join(u_token, channel_id)
    invalid_id = channel_id + 1
    with pytest.raises(ValueError):
        channel_addowner(owner_token, invalid_id, u_id)

# Testing promoting the original owner of the channel
def test_channel_addowner_3():
    channel_id = channels_create(owner_token, "Channel Name", True)
    with pytest.raises(ValueError):
        channel_addowner(owner_token, channel_id, owner_id)

# Testing promoting a member of the channel who has already been promoted before
def test_channel_addowner_4():
    channel_id = channels_create(owner_token, "Channel Name", True)
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    with pytest.raises(ValueError):
        channel_addowner(owner_token, channel_id, u_id)

# Testing promoting a member if the person conducting the action does not have authority
def test_channel_addowner_5():
    channel_id = channels_create(owner_token, "Channel Name", True)
    












#
