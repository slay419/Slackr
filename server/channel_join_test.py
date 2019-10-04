import pytest

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
    pass

'''
Returns 1 if the channel id does not exist and is invalid
Returns 0 if the channel id otherwise
'''
def is_invalid_channel(channel_id):
    pass

######################## GLOBAL VARIABLES SETUP ######################

ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['id']

##########################    END SETUP   ########################

# Testing joining a channel that hasn't been created yet
def test_channel_join_1():
    with pytest.raises(ValueError):
        channel_join(u_token, 1234)

# Testing joining a channel with a different id to one that has been created
def test_channel_join_2():
    channel_id = channels_create(owner_token, "Name", True)
    invalid_channel_id = channel_id + 1
    with pytest.raises(ValueError):
        channel_join(u_token, invalid_channel_id)

# Testing joining a channel you have already joined
def test_channel_join_3():
    channel_id = channels_create(owner_token, "Name", True)
    channel_join(u_token, channel_id)
    with pytest.raises(ValueError):
        channel_join(u_token, channel_id)

# Testing joining a different channel id to a list of already created channels
def test_channel_join_4():
    channel_id1 = channels_create(owner_token, "Channel Name", True)
    channel_id2 = channels_create(owner_token, "Second Channel", True)
    channel_id3 = channels_create(owner_token, "Third Channel", True)
    invalid_channel_id = channel_id1 + channel_id2 + channel_id3
    with pytest.raises(ValueError):
        channel_join(channels_create(u_token, invalid_channel_id))

# Testing joining a channel already joined in a list of channels
def test_channel_join_5():
    channel_id1 = channels_create(owner_token, "Channel Name", True)
    channel_id2 = channels_create(owner_token, "Second Channel", True)
    channel_id3 = channels_create(owner_token, "Third Channel", True)
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    with pytest.raises(ValueError):
        channel_join(u_token, channel_id2)

# Testing joining a single channel already created
def test_channel_join_6():
    channel_id1 = channels_create(owner_token, "Name", True)
    channel_join(u_token, channel_id)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Name"}])

# Testing joining only one channel out of a list of channels
def test_channel_join_7():
    channel_id1 = channels_create(owner_token, "Channel Name", True)
    channel_id2 = channels_create(owner_token, "Second Channel", True)
    channel_id3 = channels_create(owner_token, "Third Channel", True)
    channel_join(u_token, channel_id2)
    assert(channels_list(u_token) == [{'id': channel_id2, 'name': "Second Channel"}])


# Testing joining multiple channels
def test_channel_join_8():
    channel_id1 = channels_create(owner_token, "Channel Name", True)
    channel_id2 = channels_create(owner_token, "Second Channel", True)
    channel_id3 = channels_create(owner_token, "Third Channel", True)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    assert(channels_list(u_token) == [{'id': channel_id2, 'name': "Second Channel"},
                                    {'id': channel_id3, 'name': "Third Channel"}])

# Testing joining all available channels
def test_channel_join_9():
    channel_id1 = channels_create(owner_token, "Channel Name", True)
    channel_id2 = channels_create(owner_token, "Second Channel", True)
    channel_id3 = channels_create(owner_token, "Third Channel", True)
    channel_join(u_token, channel_id1)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    assert(channels_list(u_token) == [{'id': channel_id1, 'name': "Channel Name"},
                                    {'id': channel_id2, 'name': "Second Channel"},
                                    {'id': channel_id3, 'name': "Third Channel"}])

# Testing joining a private channel with no admin privileges
def test_channel_join_10():
    channel_id = channels_create(owner_token, "Private Channel", False)
    with pytest.raises(AccessError):
        channel_join(u_token, channel_id)

# Testing joining a private channel with admin privileges
def test_channel_join_11():
    channel_id = channels_create(owner_token, "Private Channel", False)
    admin_userpermission_change(owner_token, u_id, 2)
    channel_join(u_token, channel_id)
    assert(channels_list(u_token) == [{'id': channel_id, 'name': "Private Channel"}])

# Testing joining a private channel after already joined
def test_channel_join_12():
    channel_id = channels_create(owner_token, "Private Channel", False)
    admin_userpermission_change(owner_token, u_id, 2)
    channel_join(u_token, channel_id)
    with pytest.raises(AccessError):
        channel_join(u_token, channel_id)

# Testing joining a few different channels as an admin
def test_channel_join_13():
    channel_id1 = channels_create(owner_token, "Channel Name", True)
    channel_id2 = channels_create(owner_token, "Second Channel", True)
    channel_id3 = channels_create(owner_token, "Third Channel", True)
    channel_id4 = channels_create(owner_token, "Private1", False)
    channel_id5 = channels_create(owner_token, "Private2", False)
    channel_id6 = channels_create(owner_token, "Private3", False)
    admin_userpermission_change(owner_token, u_id, 2)
    channel_join(u_token, channel_id2)
    channel_join(u_token, channel_id3)
    channel_join(u_token, channel_id5)
    assert(channels_list(u_token) == [{'id': channel_id2, 'name': "Second Channel"},
                                      {'id': channel_id3, 'name': "Third Channel"},
                                      {'id': channel_id5, 'name': "Private3"}])
