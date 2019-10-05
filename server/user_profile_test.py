
import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_join_test import channel_join
from user_profile_sethandle_test import user_profile_sethandle
'''
####################### ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 is a normal user and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
Assume NONE is returned in handle_str field if no handle has been set

'''

#For a valid user, returns information about their email, first name, last name, and handle
def user_profile(token,u_id):
    pass	#returns dict containing {email,name_first,name_last,handle_str}


################# GLOBAL VARIABLES SETUP ######################

userDict1 = auth_register('steven@gmail.com', 'hello123', 'Steven', 'Lay')
user1 = userDict1['token']
user_id1 = userDict1['u_id']

userDict2 = auth_register('steven2@gmail.com','hello123','Steven2','Lay')
user2 = userDict2['token']
user_id2 = userDict2['u_id']

channelDict1 = channels_create(user1, 'chat1', True)
channel1 = channelDict1['channel_id']

channelDict2 = channels_create(user1, 'chat2', True)
channel2 = channelDict2['channel_id']

channel_join(user1,channel1)
channel_join(user2,channel1)
##########################    END SETUP   ########################


#Testing user1's profile with no handle
def test_user_profile_1():
	profileDict1 = user_profile(user1, user1_id)
	assert(profileDict1) == {email : 'steven@gmail.com', name_first : 'Steven', name_last : 'Lay', handle_str : NONE}

#Testing user2's profile with no handle
def test_user_profile_2():
	profileDict2 = user_profile(user2, user2_id)
	assert(profileDict2) == {email : 'stevenlayno1@gmail.com', name_first : 'Lay', name_last : 'Steven', handle_str : NONE}

#Testing user2's profile with handle
def test_user_profile_3():
	user_profile_sethandle(user2, 'l33thack3r')
	profileDict2 = user_profile(user2, user2_id)
	assert(profileDict2) == {email : 'stevenlayno1@gmail.com', name_first : 'Lay', name_last : 'Steven', handle_str : 'l33thack3r'}

#Testing invalid users profile 
def test_user_profile_4():
	with pytest.raises(ValueError):
		profileDict3 = user_profile(user3, user3_id)