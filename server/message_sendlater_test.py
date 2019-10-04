from datetime import date, time, datetime
#import pytest


def message_sendlater(token, channel_id, message, time_sent):
    if is_invalid_channel():
        raise ValueError("Channel ID does NOT exist.")
    if len(message) > 1000:
        raise ValueError("Message length is more than 1000 characters")

'''
ValueError when:
    Channel (based on ID) does not exist
    Message is more than 1000 characters
    Time sent is a time in the past
'''
