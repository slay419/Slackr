from .data import *

def search(token, query_str):
    data = get_data()

    messages = []

    for channel in channels_list(token):
        for message in channel['messages']:
            if query_str in message['message']]:
                message.append(message['message'])
	
	return messages