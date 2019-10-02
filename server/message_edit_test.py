
#Given a message, update it's text with new text
def message_edit(token, message_id, message):
	pass

#For tests, we need a token and message_id of previous message
#All tests assume no messages have been written previously

#Value error when attempting to edit a message not sent by yourself (someone elses message)
#Attempting to edit an edited message that you didn't create
#Editing a message that wasn't sent by channel owner
#Editing a message that wasn't sent by slack owner/ an admin

def message_edit_test_1():
	userDict1 = auth_register()
	message_edit(,,'hello')