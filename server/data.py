
'''
File of global variables to be used by other functions
'''


# List of users -- ASSUME TOKEN WORKS RIGHT NOW
USERS_LIST = [
    {'email': 'kevin@gmail.com', 'password': 'passwordkevin',
     'name_first': 'kevin', 'name_last': 'chau', 'u_id': 1, 'token': 'token1'},
    {'email': 'steven@gmail.com', 'password': 'passwordsteven',
     'name_first': 'steven', 'name_last': 'lay', 'u_id': 2, 'token': 'token2'},
    {'email': 'yasin@gmail.com', 'password': 'passwordyasin',
     'name_first': 'yasin', 'name_last': 'khan', 'u_id': 3, 'token': 'token3'},
    {'email': 'peter@gmail.com', 'password': 'passwordpeter',
     'name_first': 'peter', 'name_last': 'chen', 'u_id': 4, 'token': 'token4'}
]

def get_users():
    global USERS_LIST
    return USERS_LIST

# List of channel info e.g. [id: 1, name: "channelname", is_public: True]
CHANNELS_LIST = []

def get_channels():
    global CHANNELS_LIST
    return CHANNELS_LIST


'''
empties the list of channels for debugging/testing
'''
def reset_channel():
    channels = get_channels()
    channels.clear()
