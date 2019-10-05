import pytest

#Database of registered users is empty.

def auth_register(email, password, name_first, name_last):
    pass

#All details are valid
def test_auth_register_1():
    auth_register('email1@gmail.com', 'validpass', 'Yasin', 'Kevin')

#All details are valid
def test_auth_register_2():
    auth_register('email2@gmail.com', 'validpass', 'Yasin Kevin', 'Peter Steven')

#All details are valid
def test_auth_register_3():
    auth_register('email3@gmail.com', 'validpass', 'Same', 'Same')

#All details are valid
def test_auth_register_4():
    auth_register('email4@gmail.com', 'validpass', 'Y()@#@!#*##@', '#@$)(#)$(()#$()(#)@$)')

#All details are valid (name is exactly 50 characters)
def test_auth_register_5():
    auth_register('emaail5@gmail.com', 'validpass', 'thisisindeeddefinitelyfiftycharacterslongexactlyxx', 'thisisindeeddefinitelyfiftycharacterslongexactlyxy')

#Password is less than 5 characters (4)
def test_auth_register_6():
    with pytest.raises(ValueError):
        auth_register('email6@gmail.com', 'four', 'First', 'Last')

#First name exceeds 50 characters
def test_auth_register_7():
    with pytest.raises(ValueError):
        auth_register('email6@gmail.com', 'validPasss', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'Last')

#Last name exceeds 50 characters
def test_auth_register_8():
    with pytest.raises(ValueError):
        auth_register('email6@gmail.com', 'validPasss', 'First', 'GreaterthanfiftycharactersLastnamewhichiswaytoolong')

#Email address is already registered
def test_auth_register_9():
    with pytest.raises(ValueError):
        auth_register('email1@gmail.com', 'validPasss', 'First', 'Last')

#invalid email address
def test_auth_register_10():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'validPasss', 'First', 'Last')


#Different combinations of invalid email, pass, first name, last name

def test_auth_register_11():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'four', 'First', 'Last')

def test_auth_register_12():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'four', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'Last')

def test_auth_register_13():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'four', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'GreaterthanfiftycharactersLastnamewhichiswaytoolong')

def test_auth_register_14():
    with pytest.raises(ValueError):
        auth_register('', '', '', '')