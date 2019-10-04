import pytest
from auth_login_test import auth_login
import requests

## This function does:
## Given a query string, return a collection of messages that match the query

## Function will fail if:
## NA

def search(token, query_str):
	messages['message1', 'message2', 'message3']
	
    return messages
  
def test_search():
	userDictionary = auth_login'johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	searchStr = 'searchMessage'		
	assert (search(intendedUser,searchStr) ==  ['message1', 'message2', 'message3'])