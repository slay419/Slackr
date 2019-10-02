import pytest
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

#Assumptions: Email validation function is already implemented in auth_login.
#Input names are taken literally. E.g in first test, assumed that
#the email and passowrd entered are actually registered and correct.

def auth_login(email, password):
    if (email_validate(email) is False):
        raise ValueError
    pass

def email_validate(email):
    if(re.search(regex,email)):  
        return True 
          
    else:  
        return False  

def test_auth_login_1():
    auth_login("registereduser@gmail.com", "correctpassword")

def test_auth_login_2():
    with pytest.raises(ValueError):
        auth_login("registereduser@gmail.com", "incorrectpass")

def test_auth_login_3():
    with pytest.raises(ValueError):
        auth_login("unregistereduser@gmail.com", "randompass")

def test_auth_login_4():
    with pytest.raises(ValueError):
        auth_login("inVAL1D3mail$", "randompass")

def test_auth_login_5():
    with pytest.raises(ValueError):
        auth_login("1", "1")

def test_auth_login_6():
    with pytest.raises(ValueError):
        auth_login("", "")