import pytest
from auth_login_test import auth_login
import requests

'''
####################### ASSUMPTIONS ######################
Assume entering an empty search	message is not possible as there is 
no way to prevent this at the moment
Assume searching will be 'find-in-word'. i.e searching for 'a' will result in 'example'
because the letter a is present
Assume the search message is not case sensetive because it is not possible at the moment
'''

## This function does:
## Given a query string, return a collection of messages that match the query

## Function will fail if:
## NA

def search(token, query_str):
	messages['message1', 'message2', 'message3']
	
    return messages

######################## GLOBAL VARIABLES SETUP ######################

userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']

##########################    END SETUP   ########################
 
#Test a basic search
def test_search_1():
	assert (search(u_token,'message') ==  ['message1', 'message2', 'message3'])

#Test find-in-word search
def test_search_2():
	assert (search(u_token,'a') ==  ['message1', 'message2', 'message3'])

#Test find-in-word search
def test_search_3():
	assert (search(u_token,'1') ==  ['message1', 'apple2', 'pizza1'])
	
#Test case sensetivity
def test_search_3():
	assert (search(u_token,'message') ==  ['message1', 'Message2', 'mEsSaGe3'])
