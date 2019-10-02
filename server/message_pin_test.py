def message_pin(token, message_id):
	pass

#Value error on: message_id not valid message
#user isn't an admin
#message is already pinned

#Access error on: user is not member of channel message is in

#For tests 1-3, it is assumed that the user/admin is a member of the channel
#the message is in.
def message_pin_test_1():
	#assuming message_id '1' doesn't contain a message
	with raises.pytest(ValueError):
		message_pin(admin1, 1)

def message_pin_test_2():
	#assuming user1 isn't an admin
	with raises.pytest(ValueError):
		message_pin(user1, 2)

def message_pin_test_3():
	message_pin(admin1, 2)
	with raises.pytest(ValueError):
		message_pin(admin1, 2)

def message_pin_test_4():
	#assuming message 2 is in a channel that admin1 isn't a member of
	with raises.pytest(AccessError):
		message_pin(admin1,2)