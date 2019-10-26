import pytest
from functions.auth_functions import auth_register, auth_logout
from functions.channel_functions import channels_create, channel_invite, channel_leave, channel_details
from functions.data import *



#user views details of channel he created
def test_channel_details_1():
    reset_data()

    dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
    token1 = dict1['token']
    u_id1 = dict1['u_id']

    dict2 = channels_create(token1, 'someChannel', 1)
    channel_id1 = dict2['channel_id']

    assert(channel_details(token1, channel_id1) == {
        'name' : 'someChannel',
        'owner_members' : [{'u_id' : u_id1, 'name_first' : 'Yasin' , 'name_last' : 'Kevin'}],
        'all_members' :  [{'u_id' : u_id1, 'name_first' : 'Yasin' , 'name_last' : 'Kevin'}]
    })

#user invites someone then views details of channel he created
def test_channel_details_2():
    reset_data()

    dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
    token1 = dict1['token']
    u_id1 = dict1['u_id']

    dict2 = auth_register('email2@gmail.com', 'validpass', 'Peter', 'Steven')
    u_id2 = dict2['u_id']

    dict3 = channels_create(token1, 'someChannel', 1)
    channel_id1 = dict3['channel_id']

    channel_invite(token1, channel_id1, u_id2)

    assert(channel_details(token1, channel_id1) == {
        'name' : 'someChannel',
        'owner_members' : [{'u_id' : u_id1, 'name_first' : 'Yasin' , 'name_last' : 'Kevin'}],
        'all_members' :  [{'u_id' : u_id1, 'name_first' : 'Yasin' , 'name_last' : 'Kevin'}, {'u_id' : u_id2, 'name_first' : 'Peter' , 'name_last' : 'Steven'}]
    })

#user invites someone then invitee views channel just joined
def test_channel_details_3():
    reset_data()

    dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
    token1 = dict1['token']
    u_id1 = dict1['u_id']

    dict2 = auth_register('email2@gmail.com', 'validpass', 'Peter', 'Steven')
    u_id2 = dict2['u_id']
    token2 = dict2['token']

    dict3 = channels_create(token1, 'someChannel', 1)
    channel_id1 = dict3['channel_id']

    channel_invite(token1, channel_id1, u_id2)

    assert(channel_details(token2, channel_id1) == {
        'name' : 'someChannel',
        'owner_members' : [{'u_id' : u_id1, 'name_first' : 'Yasin' , 'name_last' : 'Kevin'}],
        'all_members' :  [{'u_id' : u_id1, 'name_first' : 'Yasin' , 'name_last' : 'Kevin'}, {'u_id' : u_id2, 'name_first' : 'Peter' , 'name_last' : 'Steven'}]
    })

#user invites someone to his channel. Owner then levaes. Invitee views.
def test_channel_details_4():
    reset_data()

    dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
    token1 = dict1['token']
    u_id1 = dict1['u_id']

    dict2 = auth_register('email2@gmail.com', 'validpass', 'Peter', 'Steven')
    u_id2 = dict2['u_id']
    token2 = dict2['token']

    dict3 = channels_create(token1, 'someChannel', 1)
    channel_id1 = dict3['channel_id']

    channel_invite(token1, channel_id1, u_id2)
    channel_leave(token1, channel_id1)

    assert(channel_details(token2, channel_id1) == {
        'name' : 'someChannel',
        'owner_members' : [],
        'all_members' :  [{'u_id' : u_id2, 'name_first' : 'Peter' , 'name_last' : 'Steven'}]
    })


#user tries to view details of channel with id that does not exist
def test_channel_details_5():
    reset_data()

    dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
    token1 = dict1['token']
    u_id1 = dict1['u_id']

    dict2 = channels_create(token1, 'someChannel', 1)
    channel_id1 = dict2['channel_id']

    with pytest.raises(ValueError):
        channel_details(token1, channel_id1 + 1)


#user tries to view details of channel he is not part of
def test_channel_details_6():
    reset_data()

    dict1 = auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')
    token1 = dict1['token']
    u_id1 = dict1['u_id']

    dict2 = auth_register('email2@gmail.com', 'validpass', 'Peter', 'Steven')
    u_id2 = dict2['u_id']
    token2 = dict2['token']

    dict3 = channels_create(token1, 'someChannel', 1)
    channel_id1 = dict3['channel_id']

    with pytest.raises(AccessError):
        channel_details(token2, channel_id1)
