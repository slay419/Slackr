from auth_register_test                 import auth_register
from auth_login_test                    import auth_login
from channels_create_test               import channels_create
from channel_join_test                  import channel_join
from error                              import AccessError

import pytest

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
    if is_invalid_channel(channel_id):
        # Cannot promote a user in a channel they have not joined or does not exist
        raise ValueError("Channel ID does NOT exist.")
    if is_owner(u_id):
        # Cannot promote a user that is already an owner
        raise ValueError("User is already an owner.")
    if is_authorised(token) == 0:
        # Cannot promote a user if the person conducting the action does not have the authority
        raise AccessError("User with token does not have the permission to perform this action.")
    pass

'''
Returns 1 if the channel id does not exist and is invalid
Returns 0 if the channel id otherwise
'''
def is_invalid_channel(channel_id):
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
ownerLogin = auth_login("owner@gmail.com", "password")
owner_token = ownderDict['token']
owner_id = ownerDict['u_id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
userLogin = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']
u_id = userDict1['u_id']

##########################    END SETUP   ########################

# Testing promoting a user to a channel that has not been created yet
def test_channel_addowner_1():
    with pytest.raises(ValueError):
        channel_addowner(owner_token, 1234, u_id)

# Testing promoting a user to the wrong channel id
def test_channel_addowner_2():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    invalid_id = channel_id + 1
    with pytest.raises(ValueError):
        channel_addowner(owner_token, invalid_id, u_id)

# Testing promoting a user in a channel id they have not joined yet
def test_channel_addowner_3():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    with pytest.raises(ValueError):
        channel_addowner(owner_token, channel_id, u_id)

# Testing promoting the original owner of the channel
def test_channel_addowner_4():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel1['channel_id']
    with pytest.raises(ValueError):
        channel_addowner(owner_token, channel_id, owner_id)

# Testing promoting a member of the channel who has already been promoted before
def test_channel_addowner_5():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    with pytest.raises(ValueError):
        channel_addowner(owner_token, channel_id, u_id)

# Testing promoting a member if the person conducting the action does not have authority
# e.g. promoting themself
def test_channel_addowner_6():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    with pytest.raises(AccessError):
        channel_addowner(u_token, channel_id, u_id)

# Testing promoting a member if the person conducting the action does not have authority
# e.g. member promoting another member
def test_channel_addowner_7():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    # Creating a new member
    newUserDict = auth_register("person2@gmail.com", "password", "person", "two")
    newUserLogin = auth_login("person2@gmail.com", "password")
    member_token = newUserDict['token']
    member_id = newUserDict['u_id']
    # End member setup
    channel_join(member_token, channel_id)
    with pytest.raises(AccessError):
        channel_addowner(u_token, channel_id, member_id)

# Testing promoting a member to owner under correct conditions
def test_channel_addowner_8():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    assert(is_owner(u_id))                              # Checking user is now owner
    # Creating a new member
    memberDict = auth_register("person2@gmail.com", "password", "person", "two")
    newUserLogin = auth_login("person2@gmail.com", "password")
    member_id = memberDict['id']
    member_token = memberDict['token']
    # End member setup
    channel_join(member_token, channel_id)
    assert(is_owner(member_id) == 0)                    # Checking not owner since did not get promoted

# Testing a user promoted by another owner can promote others too
def test_channel_addowner_9():
    channel = channels_create(owner_token, "Channel Name", True)
    channel_id = channel['channel_id']
    channel_join(u_token, channel_id)
    channel_addowner(owner_token, channel_id, u_id)
    assert(is_owner(u_id))
    # Creating a new member
    newUserDict = auth_register("person2@gmail.com", "password", "person", "two")
    newUserLogin = auth_login("person2@gmail.com", "password")
    member_token = newUserDict['token']
    member_id = newUserDict['u_id']
    # End member setup
    channel_join(member_token, channel_id)
    channel_addowner(u_token, channel_id, member_id)
    assert(is_owner(member_id))
