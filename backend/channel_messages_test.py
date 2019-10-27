from functions.auth_functions import auth_register
from functions.channel_functions import channels_create, channel_join, channels_list, channel_messages
from functions.message_functions import message_send
from functions.misc_functions import admin_userpermission_change

from functions.data import *

import pytest

#Assuming there are 80 messages in the chat, since there is no function that
#returns the number of messages in the chat
#start must be atleast 0




#different cases where the user should be able to view the message

#edge case, view from most recent message
def test_channel_messages_1():
    ######################## BEGIN SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']

    channel_dict = channels_create(owner_token, 'channel name', True)
    channel_id = channel_dict['channel_id']

    channel_dict2 = channels_create(owner_token, 'channel 2', True)
    channel_id2 = channel_dict['channel_id']

    channel_join(u_token, channel_id)

    m1 = message_send(owner_token, channel_id, "message1")
    m2 = message_send(owner_token, channel_id, "message2")
    m3 = message_send(owner_token, channel_id, "message3")
    m4 = message_send(owner_token, channel_id, "message4")
    m5 = message_send(owner_token, channel_id, "message5")
    m6 = message_send(owner_token, channel_id, "message6")
    m7 = message_send(owner_token, channel_id, "message7")
    m8 = message_send(owner_token, channel_id, "message8")
    m9 = message_send(owner_token, channel_id, "message9")
    m10 = message_send(owner_token, channel_id, "message10")
    m11 = message_send(owner_token, channel_id, "message10")
    m12 = message_send(owner_token, channel_id, "message10")
    m13 = message_send(owner_token, channel_id, "message10")
    m14 = message_send(owner_token, channel_id, "message10")
    m15 = message_send(owner_token, channel_id, "message10")
    m16 = message_send(owner_token, channel_id, "message10")
    m17 = message_send(owner_token, channel_id, "message10")
    m18 = message_send(owner_token, channel_id, "message10")
    m19 = message_send(owner_token, channel_id, "message10")
    m20 = message_send(owner_token, channel_id, "message10")
    m21 = message_send(owner_token, channel_id, "message10")
    m22 = message_send(owner_token, channel_id, "message10")
    m23 = message_send(owner_token, channel_id, "message10")
    m24 = message_send(owner_token, channel_id, "message10")
    m25 = message_send(owner_token, channel_id, "message10")
    m26 = message_send(owner_token, channel_id, "message10")
    m27 = message_send(owner_token, channel_id, "message10")
    m28 = message_send(owner_token, channel_id, "message10")
    m29 = message_send(owner_token, channel_id, "message10")
    m30 = message_send(owner_token, channel_id, "message10")
    m31 = message_send(owner_token, channel_id, "message10")
    m32 = message_send(owner_token, channel_id, "message10")
    m33 = message_send(owner_token, channel_id, "message10")
    m34 = message_send(owner_token, channel_id, "message10")
    m35 = message_send(owner_token, channel_id, "message10")
    m36 = message_send(owner_token, channel_id, "message10")
    m37 = message_send(owner_token, channel_id, "message10")
    m38 = message_send(owner_token, channel_id, "message10")
    m39 = message_send(owner_token, channel_id, "message10")
    m40 = message_send(owner_token, channel_id, "message10")
    m41 = message_send(owner_token, channel_id, "message10")
    m42 = message_send(owner_token, channel_id, "message10")
    m43 = message_send(owner_token, channel_id, "message10")
    m44 = message_send(owner_token, channel_id, "message10")
    m45 = message_send(owner_token, channel_id, "message10")
    m46 = message_send(owner_token, channel_id, "message10")
    m47 = message_send(owner_token, channel_id, "message10")
    m48 = message_send(owner_token, channel_id, "message10")
    m49 = message_send(owner_token, channel_id, "message10")
    m50 = message_send(owner_token, channel_id, "message10")
    m51 = message_send(owner_token, channel_id, "message10")
    m52 = message_send(owner_token, channel_id, "message10")

    messagelist = data['messages']
    messagelist.sort(key = lambda i: i['time_created'],reverse=True)
    ##########################    END SETUP   ########################
    
    list1 = []
    start = 0
    end = start + 50
    for i in range(start, end):
        list1.append(messagelist[i])
    assert(channel_messages(owner_token, channel_id, 0) == {
        'messages': list1,
        'start': 0,
        'end': 50,
    })

#Viewing from 2nd message in
def test_channel_messages_2():
    ######################## BEGIN SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']

    channel_dict = channels_create(owner_token, 'channel name', True)
    channel_id = channel_dict['channel_id']

    channel_dict2 = channels_create(owner_token, 'channel 2', True)
    channel_id2 = channel_dict['channel_id']

    channel_join(u_token, channel_id)

    m1 = message_send(owner_token, channel_id, "message1")
    m2 = message_send(owner_token, channel_id, "message2")
    m3 = message_send(owner_token, channel_id, "message3")
    m4 = message_send(owner_token, channel_id, "message4")
    m5 = message_send(owner_token, channel_id, "message5")
    m6 = message_send(owner_token, channel_id, "message6")
    m7 = message_send(owner_token, channel_id, "message7")
    m8 = message_send(owner_token, channel_id, "message8")
    m9 = message_send(owner_token, channel_id, "message9")
    m10 = message_send(owner_token, channel_id, "message10")
    m11 = message_send(owner_token, channel_id, "message10")
    m12 = message_send(owner_token, channel_id, "message10")
    m13 = message_send(owner_token, channel_id, "message10")
    m14 = message_send(owner_token, channel_id, "message10")
    m15 = message_send(owner_token, channel_id, "message10")
    m16 = message_send(owner_token, channel_id, "message10")
    m17 = message_send(owner_token, channel_id, "message10")
    m18 = message_send(owner_token, channel_id, "message10")
    m19 = message_send(owner_token, channel_id, "message10")
    m20 = message_send(owner_token, channel_id, "message10")
    m21 = message_send(owner_token, channel_id, "message10")
    m22 = message_send(owner_token, channel_id, "message10")
    m23 = message_send(owner_token, channel_id, "message10")
    m24 = message_send(owner_token, channel_id, "message10")
    m25 = message_send(owner_token, channel_id, "message10")
    m26 = message_send(owner_token, channel_id, "message10")
    m27 = message_send(owner_token, channel_id, "message10")
    m28 = message_send(owner_token, channel_id, "message10")
    m29 = message_send(owner_token, channel_id, "message10")
    m30 = message_send(owner_token, channel_id, "message10")
    m31 = message_send(owner_token, channel_id, "message10")
    m32 = message_send(owner_token, channel_id, "message10")
    m33 = message_send(owner_token, channel_id, "message10")
    m34 = message_send(owner_token, channel_id, "message10")
    m35 = message_send(owner_token, channel_id, "message10")
    m36 = message_send(owner_token, channel_id, "message10")
    m37 = message_send(owner_token, channel_id, "message10")
    m38 = message_send(owner_token, channel_id, "message10")
    m39 = message_send(owner_token, channel_id, "message10")
    m40 = message_send(owner_token, channel_id, "message10")
    m41 = message_send(owner_token, channel_id, "message10")
    m42 = message_send(owner_token, channel_id, "message10")
    m43 = message_send(owner_token, channel_id, "message10")
    m44 = message_send(owner_token, channel_id, "message10")
    m45 = message_send(owner_token, channel_id, "message10")
    m46 = message_send(owner_token, channel_id, "message10")
    m47 = message_send(owner_token, channel_id, "message10")
    m48 = message_send(owner_token, channel_id, "message10")
    m49 = message_send(owner_token, channel_id, "message10")
    m50 = message_send(owner_token, channel_id, "message10")
    m51 = message_send(owner_token, channel_id, "message10")
    m52 = message_send(owner_token, channel_id, "message10")

    messagelist = data['messages']
    messagelist.sort(key = lambda i: i['time_created'],reverse=True)
    ##########################    END SETUP   ########################
    
    list1 = []
    start = 2
    end = start + 50
    for i in range(start, end):
        list1.append(messagelist[i])
    assert(channel_messages(owner_token, channel_id, 2) == {
        'messages': list1,
        'start': 2,
        'end': 52,
    })

#view from  middle messages (overflow)
def test_channel_messages_3():
    ######################## BEGIN SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']

    channel_dict = channels_create(owner_token, 'channel name', True)
    channel_id = channel_dict['channel_id']

    channel_dict2 = channels_create(owner_token, 'channel 2', True)
    channel_id2 = channel_dict['channel_id']

    channel_join(u_token, channel_id)

    m1 = message_send(owner_token, channel_id, "message1")
    m2 = message_send(owner_token, channel_id, "message2")
    m3 = message_send(owner_token, channel_id, "message3")
    m4 = message_send(owner_token, channel_id, "message4")
    m5 = message_send(owner_token, channel_id, "message5")
    m6 = message_send(owner_token, channel_id, "message6")
    m7 = message_send(owner_token, channel_id, "message7")
    m8 = message_send(owner_token, channel_id, "message8")
    m9 = message_send(owner_token, channel_id, "message9")
    m10 = message_send(owner_token, channel_id, "message10")
    m11 = message_send(owner_token, channel_id, "message10")
    m12 = message_send(owner_token, channel_id, "message10")
    m13 = message_send(owner_token, channel_id, "message10")
    m14 = message_send(owner_token, channel_id, "message10")
    m15 = message_send(owner_token, channel_id, "message10")
    m16 = message_send(owner_token, channel_id, "message10")
    m17 = message_send(owner_token, channel_id, "message10")
    m18 = message_send(owner_token, channel_id, "message10")
    m19 = message_send(owner_token, channel_id, "message10")
    m20 = message_send(owner_token, channel_id, "message10")
    m21 = message_send(owner_token, channel_id, "message10")
    m22 = message_send(owner_token, channel_id, "message10")
    m23 = message_send(owner_token, channel_id, "message10")
    m24 = message_send(owner_token, channel_id, "message10")
    m25 = message_send(owner_token, channel_id, "message10")
    m26 = message_send(owner_token, channel_id, "message10")
    m27 = message_send(owner_token, channel_id, "message10")
    m28 = message_send(owner_token, channel_id, "message10")
    m29 = message_send(owner_token, channel_id, "message10")
    m30 = message_send(owner_token, channel_id, "message10")
    m31 = message_send(owner_token, channel_id, "message10")
    m32 = message_send(owner_token, channel_id, "message10")
    m33 = message_send(owner_token, channel_id, "message10")
    m34 = message_send(owner_token, channel_id, "message10")
    m35 = message_send(owner_token, channel_id, "message10")
    m36 = message_send(owner_token, channel_id, "message10")
    m37 = message_send(owner_token, channel_id, "message10")
    m38 = message_send(owner_token, channel_id, "message10")
    m39 = message_send(owner_token, channel_id, "message10")
    m40 = message_send(owner_token, channel_id, "message10")
    m41 = message_send(owner_token, channel_id, "message10")
    m42 = message_send(owner_token, channel_id, "message10")
    m43 = message_send(owner_token, channel_id, "message10")
    m44 = message_send(owner_token, channel_id, "message10")
    m45 = message_send(owner_token, channel_id, "message10")
    m46 = message_send(owner_token, channel_id, "message10")
    m47 = message_send(owner_token, channel_id, "message10")
    m48 = message_send(owner_token, channel_id, "message10")
    m49 = message_send(owner_token, channel_id, "message10")
    m50 = message_send(owner_token, channel_id, "message10")
    m51 = message_send(owner_token, channel_id, "message10")
    m52 = message_send(owner_token, channel_id, "message10")

    messagelist = data['messages']
    messagelist.sort(key = lambda i: i['time_created'],reverse=True)
    ##########################    END SETUP   ########################
    
    list1 = []
    start = 25
    end = 52
    for i in range(start, end):
        list1.append(messagelist[i])
    assert (channel_messages(owner_token, channel_id, 25) == {
        'messages': list1,
        'start': 25,
        'end': -1
    })

#view from out of index
def test_channel_messages_4():
    ######################## BEGIN SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']

    channel_dict = channels_create(owner_token, 'channel name', True)
    channel_id = channel_dict['channel_id']

    channel_dict2 = channels_create(owner_token, 'channel 2', True)
    channel_id2 = channel_dict['channel_id']

    channel_join(u_token, channel_id)

    m1 = message_send(owner_token, channel_id, "message1")
    m2 = message_send(owner_token, channel_id, "message2")
    m3 = message_send(owner_token, channel_id, "message3")
    m4 = message_send(owner_token, channel_id, "message4")
    m5 = message_send(owner_token, channel_id, "message5")
    m6 = message_send(owner_token, channel_id, "message6")
    m7 = message_send(owner_token, channel_id, "message7")
    m8 = message_send(owner_token, channel_id, "message8")
    m9 = message_send(owner_token, channel_id, "message9")
    m10 = message_send(owner_token, channel_id, "message10")
    m11 = message_send(owner_token, channel_id, "message10")
    m12 = message_send(owner_token, channel_id, "message10")
    m13 = message_send(owner_token, channel_id, "message10")
    m14 = message_send(owner_token, channel_id, "message10")
    m15 = message_send(owner_token, channel_id, "message10")
    m16 = message_send(owner_token, channel_id, "message10")
    m17 = message_send(owner_token, channel_id, "message10")
    m18 = message_send(owner_token, channel_id, "message10")
    m19 = message_send(owner_token, channel_id, "message10")
    m20 = message_send(owner_token, channel_id, "message10")
    m21 = message_send(owner_token, channel_id, "message10")
    m22 = message_send(owner_token, channel_id, "message10")
    m23 = message_send(owner_token, channel_id, "message10")
    m24 = message_send(owner_token, channel_id, "message10")
    m25 = message_send(owner_token, channel_id, "message10")
    m26 = message_send(owner_token, channel_id, "message10")
    m27 = message_send(owner_token, channel_id, "message10")
    m28 = message_send(owner_token, channel_id, "message10")
    m29 = message_send(owner_token, channel_id, "message10")
    m30 = message_send(owner_token, channel_id, "message10")
    m31 = message_send(owner_token, channel_id, "message10")
    m32 = message_send(owner_token, channel_id, "message10")
    m33 = message_send(owner_token, channel_id, "message10")
    m34 = message_send(owner_token, channel_id, "message10")
    m35 = message_send(owner_token, channel_id, "message10")
    m36 = message_send(owner_token, channel_id, "message10")
    m37 = message_send(owner_token, channel_id, "message10")
    m38 = message_send(owner_token, channel_id, "message10")
    m39 = message_send(owner_token, channel_id, "message10")
    m40 = message_send(owner_token, channel_id, "message10")
    m41 = message_send(owner_token, channel_id, "message10")
    m42 = message_send(owner_token, channel_id, "message10")
    m43 = message_send(owner_token, channel_id, "message10")
    m44 = message_send(owner_token, channel_id, "message10")
    m45 = message_send(owner_token, channel_id, "message10")
    m46 = message_send(owner_token, channel_id, "message10")
    m47 = message_send(owner_token, channel_id, "message10")
    m48 = message_send(owner_token, channel_id, "message10")
    m49 = message_send(owner_token, channel_id, "message10")
    m50 = message_send(owner_token, channel_id, "message10")
    m51 = message_send(owner_token, channel_id, "message10")
    m52 = message_send(owner_token, channel_id, "message10")

    messagelist = data['messages']
    messagelist.sort(key = lambda i: i['time_created'],reverse=True)
    ##########################    END SETUP   ########################
    
    list1 = []
    start = 53
    with pytest.raises(ValueError):
        channel_messages(owner_token, channel_id, 53)

#Testing invalid channel
def test_channel_messages_5():
    ######################## BEGIN SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']

    channel_dict = channels_create(owner_token, 'channel name', True)
    channel_id = channel_dict['channel_id']

    channel_dict2 = channels_create(owner_token, 'channel 2', True)
    channel_id2 = channel_dict['channel_id']

    channel_join(u_token, channel_id)

    m1 = message_send(owner_token, channel_id, "message1")
    m2 = message_send(owner_token, channel_id, "message2")
    m3 = message_send(owner_token, channel_id, "message3")
    m4 = message_send(owner_token, channel_id, "message4")
    m5 = message_send(owner_token, channel_id, "message5")
    m6 = message_send(owner_token, channel_id, "message6")
    m7 = message_send(owner_token, channel_id, "message7")
    m8 = message_send(owner_token, channel_id, "message8")
    m9 = message_send(owner_token, channel_id, "message9")
    m10 = message_send(owner_token, channel_id, "message10")
    m11 = message_send(owner_token, channel_id, "message10")
    m12 = message_send(owner_token, channel_id, "message10")
    m13 = message_send(owner_token, channel_id, "message10")
    m14 = message_send(owner_token, channel_id, "message10")
    m15 = message_send(owner_token, channel_id, "message10")
    m16 = message_send(owner_token, channel_id, "message10")
    m17 = message_send(owner_token, channel_id, "message10")
    m18 = message_send(owner_token, channel_id, "message10")
    m19 = message_send(owner_token, channel_id, "message10")
    m20 = message_send(owner_token, channel_id, "message10")
    m21 = message_send(owner_token, channel_id, "message10")
    m22 = message_send(owner_token, channel_id, "message10")
    m23 = message_send(owner_token, channel_id, "message10")
    m24 = message_send(owner_token, channel_id, "message10")
    m25 = message_send(owner_token, channel_id, "message10")
    m26 = message_send(owner_token, channel_id, "message10")
    m27 = message_send(owner_token, channel_id, "message10")
    m28 = message_send(owner_token, channel_id, "message10")
    m29 = message_send(owner_token, channel_id, "message10")
    m30 = message_send(owner_token, channel_id, "message10")
    m31 = message_send(owner_token, channel_id, "message10")
    m32 = message_send(owner_token, channel_id, "message10")
    m33 = message_send(owner_token, channel_id, "message10")
    m34 = message_send(owner_token, channel_id, "message10")
    m35 = message_send(owner_token, channel_id, "message10")
    m36 = message_send(owner_token, channel_id, "message10")
    m37 = message_send(owner_token, channel_id, "message10")
    m38 = message_send(owner_token, channel_id, "message10")
    m39 = message_send(owner_token, channel_id, "message10")
    m40 = message_send(owner_token, channel_id, "message10")
    m41 = message_send(owner_token, channel_id, "message10")
    m42 = message_send(owner_token, channel_id, "message10")
    m43 = message_send(owner_token, channel_id, "message10")
    m44 = message_send(owner_token, channel_id, "message10")
    m45 = message_send(owner_token, channel_id, "message10")
    m46 = message_send(owner_token, channel_id, "message10")
    m47 = message_send(owner_token, channel_id, "message10")
    m48 = message_send(owner_token, channel_id, "message10")
    m49 = message_send(owner_token, channel_id, "message10")
    m50 = message_send(owner_token, channel_id, "message10")
    m51 = message_send(owner_token, channel_id, "message10")
    m52 = message_send(owner_token, channel_id, "message10")

    messagelist = data['messages']
    messagelist.sort(key = lambda i: i['time_created'],reverse=True)
    ##########################    END SETUP   ########################
    
    list1 = []
    start = 0
    end = start + 50
    for i in range(start, end):
        list1.append(messagelist[i])
    with pytest.raises(ValueError):
        channel_messages(owner_token, 3, 0)

#Testing channel member not a part of
def test_channel_messages_6():
    ######################## BEGIN SETUP ######################
    reset_data()
    ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
    owner_token = ownerDict['token']
    owner_id = ownerDict['u_id']

    userDict = auth_register("person1@gmail.com", "password", "person", "one")
    u_token = userDict['token']
    u_id = userDict['u_id']

    channel_dict = channels_create(owner_token, 'channel name', True)
    channel_id = channel_dict['channel_id']

    channel_dict2 = channels_create(owner_token, 'channel 2', True)
    channel_id2 = channel_dict['channel_id']

    channel_join(u_token, channel_id)

    m1 = message_send(owner_token, channel_id, "message1")
    m2 = message_send(owner_token, channel_id, "message2")
    m3 = message_send(owner_token, channel_id, "message3")
    m4 = message_send(owner_token, channel_id, "message4")
    m5 = message_send(owner_token, channel_id, "message5")
    m6 = message_send(owner_token, channel_id, "message6")
    m7 = message_send(owner_token, channel_id, "message7")
    m8 = message_send(owner_token, channel_id, "message8")
    m9 = message_send(owner_token, channel_id, "message9")
    m10 = message_send(owner_token, channel_id, "message10")
    m11 = message_send(owner_token, channel_id, "message10")
    m12 = message_send(owner_token, channel_id, "message10")
    m13 = message_send(owner_token, channel_id, "message10")
    m14 = message_send(owner_token, channel_id, "message10")
    m15 = message_send(owner_token, channel_id, "message10")
    m16 = message_send(owner_token, channel_id, "message10")
    m17 = message_send(owner_token, channel_id, "message10")
    m18 = message_send(owner_token, channel_id, "message10")
    m19 = message_send(owner_token, channel_id, "message10")
    m20 = message_send(owner_token, channel_id, "message10")
    m21 = message_send(owner_token, channel_id, "message10")
    m22 = message_send(owner_token, channel_id, "message10")
    m23 = message_send(owner_token, channel_id, "message10")
    m24 = message_send(owner_token, channel_id, "message10")
    m25 = message_send(owner_token, channel_id, "message10")
    m26 = message_send(owner_token, channel_id, "message10")
    m27 = message_send(owner_token, channel_id, "message10")
    m28 = message_send(owner_token, channel_id, "message10")
    m29 = message_send(owner_token, channel_id, "message10")
    m30 = message_send(owner_token, channel_id, "message10")
    m31 = message_send(owner_token, channel_id, "message10")
    m32 = message_send(owner_token, channel_id, "message10")
    m33 = message_send(owner_token, channel_id, "message10")
    m34 = message_send(owner_token, channel_id, "message10")
    m35 = message_send(owner_token, channel_id, "message10")
    m36 = message_send(owner_token, channel_id, "message10")
    m37 = message_send(owner_token, channel_id, "message10")
    m38 = message_send(owner_token, channel_id, "message10")
    m39 = message_send(owner_token, channel_id, "message10")
    m40 = message_send(owner_token, channel_id, "message10")
    m41 = message_send(owner_token, channel_id, "message10")
    m42 = message_send(owner_token, channel_id, "message10")
    m43 = message_send(owner_token, channel_id, "message10")
    m44 = message_send(owner_token, channel_id, "message10")
    m45 = message_send(owner_token, channel_id, "message10")
    m46 = message_send(owner_token, channel_id, "message10")
    m47 = message_send(owner_token, channel_id, "message10")
    m48 = message_send(owner_token, channel_id, "message10")
    m49 = message_send(owner_token, channel_id, "message10")
    m50 = message_send(owner_token, channel_id, "message10")
    m51 = message_send(owner_token, channel_id, "message10")
    m52 = message_send(owner_token, channel_id, "message10")

    messagelist = data['messages']
    messagelist.sort(key = lambda i: i['time_created'],reverse=True)
    ##########################    END SETUP   ########################
    
    list1 = []
    start = 0
    end = start + 50
    for i in range(start, end):
        list1.append(messagelist[i])
    with pytest.raises(AccessError):
        channel_messages(u_token, 2, 0)
