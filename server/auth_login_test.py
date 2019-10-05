import pytest
from auth_register_test import auth_register

#Assumptions: Email validation function is already implemented in auth_login.
#The database of registered users is empty.

def auth_login(email, password):
    if (email_validate(email) is False):
        raise ValueError
    pass

def email_validate(email):
    pass 


#BEGIN SETUP
auth_register('myemail@gmail.com', 'mypassword', 'Kevin', 'Yasin')
auth_register('myemail2@gmail.com', 'mypassword2', 'Steven', 'Peter')
#END SETUP

#registered email and correct password
def test_auth_login_1():
    auth_login("myemail@gmail.com", "mypassword")

#registered email and incorrect pass
def test_auth_login_2():
    with pytest.raises(ValueError):
        auth_login("myemail@gmail.com", "incorrectpass")

#unregistered email
def test_auth_login_3():
    with pytest.raises(ValueError):
        auth_login("unregistereduser@gmail.com", "randompass")

#invalid email
def test_auth_login_4():
    with pytest.raises(ValueError):
        auth_login("inVAL1D3mail$", "randompass")

#invalid email
def test_auth_login_5():
    with pytest.raises(ValueError):
        auth_login("1", "1")

#invalid email
def test_auth_login_6():
    with pytest.raises(ValueError):
        auth_login("", "")

#registered user, incorrect pass
def test_auth_login_7():
    with pytest.raises(ValueError):
        auth_login("myemail2@gmail.com", "mypassword")

#registered user, correct pass
def test_auth_login_8():
    auth_login("myemail2@gmail.com", "mypasswor2")