import datetime
#import pytest


def message_sendlater(token, channel_id, message, time_sent):
    if is_invalid_channel():
        raise ValueError("Channel ID does NOT exist.")
    if len(message) > 1000:
        raise ValueError("Message length is more than 1000 characters")
    if is_in_past(time_sent):
        raise ValueError("Message cannot be set to a time in the past.")

def is_in_past(time_sent):
    now = datetime.datetime.now()
    if time_sent < now:
        return 1

    return 0

'''
ValueError when:
    Channel (based on ID) does not exist
    Message is more than 1000 characters
    Time sent is a time in the past

now = datetime.datetime.now()
print(now)


a = datetime.datetime(2019, 10, 4, 17, 17)
print(a)
check = is_in_past(a)
print(check)
'''

######################## GLOBAL VARIABLES SETUP ######################
# Assume owner_id is an admin since he is the first person to sign up
ownerDict = auth_register("owner@gmail.com", "password", "owner", "privileges")
owner_token = ownderDict['token']
owner_id = ownerDict['id']

userDict = auth_register("person1@gmail.com", "password", "person", "one")
u_token = userDict1['token']
u_id = userDict1['id']

##########################    END SETUP   ########################

# Testing sending a message in a channel which hasn't been created yet
def test_message_sendlater_1():
    


#
