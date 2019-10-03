import pytest

def user_profile(token,u_id):
	#returns dict containing {email,name_first,name_last,handle_str}
	pass

#Value error when u_id isn't a valid user
#Assume NONE is returned in handle_str field if no handle has been set
def test_user_profile_1():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	user1_id = userDict1['u_id']
	user1 = userDict1['token']
	profileDict1 = user_profile(user1,user1_id)
	assert(profileDict1) == {'steven@gmail.com','Steven','Lay',NONE}

def test_user_profile_2():
	userDict2 = auth_register('stevenlayno1@gmail.com','secretpassword','Lay','Steven')
	user2_id = userDict2['u_id']
	user2 = userDict2['token']
	profileDict2 = user_profile(user2,user2_id)
	assert(profileDict2) == {'stevenlayno1@gmail.com','Lay','Steven',NONE}

def test_user_profile_3():
	userDict2 = auth_register('stevenlayno1@gmail.com','secretpassword','Lay','Steven')
	user2_id = userDict2['u_id']
	user2 = userDict2['token']
	user_profile_sethandle(user2, 'l33thack3r')
	profileDict2 = user_profile(user2,user2_id)
	assert(profileDict2) == {'stevenlayno1@gmail.com','Lay','Steven','l33thack3r'}

def test_user_profile_4():
	userDict1 = auth_register('steven@gmail.com','hello123','Steven','Lay')
	user1_id = userDict1['u_id']
	user1 = userDict1['token']
	with pytest.raises(ValueError):
		profileDict2 = user_profile(user2,user2_id)