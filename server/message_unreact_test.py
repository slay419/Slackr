def message_unreact(token, message_id, react_id):
	pass
#Value error when message_id is not valid message in currently joined channel
#react id doesn't exist
#message with id doesn't contain react with react_id

def message_unreact_test_1():
	#assuming there is no message currently assosciated to message_id 3
	with pytest.raises(ValueError):
		message_unreact(user1,3,1)

def message_unreact_test_2():
	#assuming there isn't a 'react' associated to react_id 4
	with pytest.raises(ValueError):
		message_unreact(user1,1,4)

def message_unreact_test_3():
	#assuming there a react with id '1' exist message '1' doesn't contain a react with id '1'
	with pytest.raises(ValueError):
		message_unreact(user1,1,1)