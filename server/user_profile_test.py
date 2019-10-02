def user_profile(token,u_id):
	#returns dict containing {email,name_first,name_last,handle_str}
	pass

#Value error when u_id isn't a valid user

def user_profile_test_1():
	#assuming u_id '1' isn't valid
	with pytest.raises(ValueError):
		user_profile(user1, 1)

def user_profile_test_2():
	profileDict2 = user_profile(user2,2)
	#assuming user2 profile is made up of 'email2','name_first2','name_last2','handle_str2'
	assert(profileDict2) == {'email2','name_first2','name_last2','handle_str2'}
	

