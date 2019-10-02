def message_react(token,message_id,react_id):
	pass

#Value error when: message_id is not a valid message in the current channel
#react_id doesn't belong to a valid id
#message with message_id already has a react_id (no react dupes)

def message_react_test_1():
	#assuming there is no message currently assosciated to message_id 3
	with pytest.raises(ValueError):
		message_react(user1,3,1)

def message_react_test_2():
	#assuming there isn't a 'react' associated to react_id 4
	with pytest.raises(ValueError):
		message_react(user1,1,4)

def message_react_test_3():
	#apply react '1' to message '1'
	message_react(user1,1,1)
	#Error raised when calling the same react on the same message again
	with pytest.raises(ValueError):
		message_react(user1,1,1)
