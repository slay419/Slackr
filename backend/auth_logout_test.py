#pylint: disable=missing-docstring
#pylint: disable=unused-variable

import pytest
from functions.auth_functions import auth_register, auth_login, auth_logout
from functions.data import reset_data, is_logged_in

from functions.exceptions import ValueError, AccessError

#register user then log out
def test_auth_logout_1():
    reset_data()
    dict1 = auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
    token1 = dict1['token']
    dict2 = auth_logout(token1)
    assert dict2['is_success']
    assert not is_logged_in(token1)

#register user, logout then log in then log out
def test_auth_logout_2():
    reset_data()
    dict1 = auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
    token1 = dict1['token']
    dict2 = auth_logout(token1)
    assert dict2['is_success']
    assert not is_logged_in(token1)
    dict3 = auth_login("myemail@gmail.com", "mypassword")
    token2 = dict3['token']
    dict4 = auth_logout(token2)
    assert dict4['is_success']
    assert not is_logged_in(token2)

#register user, login in from another device as well, logout of 1 device
def test_auth_logout_3():
    reset_data()
    dict1 = auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
    token1 = dict1['token']

    dict2 = auth_login("myemail@gmail.com", "mypassword")
    token2 = dict2['token']

    dict3 = auth_logout(token1)
    assert dict3['is_success']
    assert is_logged_in(token2)
    assert not is_logged_in(token1)



#register ruser, login in from another device as well, logout of both devices
def test_auth_logout_4():
    reset_data()
    dict1 = auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
    token1 = dict1['token']

    dict2 = auth_login("myemail@gmail.com", "mypassword")
    token2 = dict2['token']

    dict3 = auth_logout(token1)
    dict4 = auth_logout(token2)
    assert dict3['is_success']
    assert dict4['is_success']
    assert not is_logged_in(token2)
    assert not is_logged_in(token1)


#register user, logout then log out again
def test_auth_logout_5():
    reset_data()
    dict1 = auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
    token1 = dict1['token']

    dict2 = auth_logout(token1)
    assert dict2['is_success']

    #logging out with invalid token
    dict3 = auth_logout(token1)
    assert not dict3['is_success']
    assert not is_logged_in(token1)

#register user, login then logout then log out again
def test_auth_logout_6():
    #register
    reset_data()
    dict1 = auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
    token1 = dict1['token']

    #logout
    dict2 = auth_logout(token1)
    assert dict2['is_success']
    assert not is_logged_in(token1)

    #login
    dict3 = auth_login("myemail@gmail.com", "mypassword")
    token2 = dict3['token']

    #logout
    dict4 = auth_logout(token2)
    assert dict4['is_success']
    assert not is_logged_in(token2)

    #logging out with invalid token
    dict5 = auth_logout(token2)
    assert not dict5['is_success']
    assert not is_logged_in(token2)
