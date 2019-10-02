def message_unpin(token, message_id):
	pass

#Value error on: message_id not valid message
#user isn't an admin
#message is already unpinned

#Access error on: user is not member of channel message is in

#For tests 1-3, it is assumed that the user/admin is a member of the channel
#the message is in.
def message_pin_test_1():
	#assuming message_id '1' doesn't contain a message
	with raises.pytest(ValueError):
		message_unpin(admin1, 1)

def message_pin_test_2():
	#assuming user1 isn't an admin
	with raises.pytest(ValueError):
		message_unpin(user1, 2)

def message_pin_test_3():
	#assuming message '3' isn't a pinned message
	with raises.pytest(ValueError):
		message_unpin(admin1, 3)

def message_pin_test_4():
	#assuming message 2 is in a channel that admin1 isn't a member of
	with raises.pytest(AccessError):
		message_unpin(admin1,2)
