from error import AccessError

import pytest

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
    if is_valid_channel(channel_id):
        pass
    else:
        raise ValueError("Channel ID does NOT exist.")
    if is_owner(u_id):
        pass
    else:
        raise ValueError("User is NOT an owner")
    if is_authorised(token):
        pass
    else:
        raise AccessError("User with token does not have the permission to perform this action.")
    pass

'''
Returns 1 if the channel id exists and is valid
Returns 0 if the channel id does not exist and is invalid
'''
def is_valid_channel(channel_id):
    pass

'''
If the user with u_id is an owner/admin, returns 1
If the user is a member, returns 0
'''
def is_owner(u_id):
    pass

'''
If the user with token is an owner or admin, returns 1
If the user is a member, returns 0
'''
def is_authorised(token):
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

# Testing demoting a user from a channel not created yet
def test_channel_removeowner_1():
    admin_userpermission_change(owner_token, u_id, 1)
    with pytest.raises(ValueError):
        channel_removeowner(owner_token, 1234, u_id)

# Testing demoting an owner from a wrong channel id
def test_channel_removeowner_2():
    channel_id = channels_create(owner_token, "Channel Name", True)
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    invalid_id = channel_id + 1
    with pytest.raises(ValueError):
        channel_removeowner(owner_token, invalid_id, u_id)

# Testing demoting a member that has not joined the channel yet
def test_channel_removeowner_3():
    channel_id = channels_create(owner_token, "Channels Name", True)
    with pytest.raises(ValueError):
        channel_removeowner(owner_token, channel_id, u_id)

# Testing demoting a member in a channel they have joined
def test_channel_removeowner_4():
    channel_id = channels_create(owner_token, "Channels Name", True)
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        channel_removeowner(owner_token, channel_id, u_id)

# Testing demoting a member in a channel they have been demoted before
def test_channel_removeowner_5():
    channel_id = channels_create(owner_token, "Channel Name", True)
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    channel_removeowner(owner_token, channel_id, u_id)
    with pytest.raises(ValueError):
        channel_removeowner(owner_token, channel_id, u_id)

# Testing a member attempting to demote himself - has no authority
def test_channel_removeowner_6():
    channel_id = channels_create(owner_token, "Channels Name", True)
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        channel_removeowner(u_token, channel_id, u_id)

# Testing a member attempting to demote an owner
def test_channel_removeowner_7():
    channel_id = channels_create(owner_token, "Channels Name", True)
    channel_join(u_token, channel_id)
    with pytest.raises(AccessError):
        channel_removeowner(u_token, channel_id, owner_token)

# Testing a member attempting to demote another member - has no authority
def test_channel_removeowner_8():
    channel_id = channels_create(owner_token, "Channels Name", True)
    channel_join(u_token, channel_id)
    memberDict = auth_register("person2@gmail.com", "password", "person", "two")
    member_id = memberDict['id']
    member_token = memberDict['token']
    channel_join(member_token, channel_id)
    with pytest.raises(ValueError):
        channel_removeowner(u_token, channel_id, member_id)

# Testing an owner demoting another owner under the right conditions
def test_channel_removeowner_9():
    channel_id = channels_create(owner_token, "Channel Name", True)
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    channel_removeowner(owner_token, channel_id, u_id)
    assert(is_owner(u_id) == 0)
    assert(is_owner(owner_id) == 1)
