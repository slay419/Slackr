import pytest

#Input are taken literally. E.g 'unusedValidemail@gmail.com' is assumed to be an email that is actually unique and valid.

def auth_register(email, password, name_first, name_last):
    pass

def test_auth_register_1():
    auth_register('unusedValidemail@gmail.com', 'validpass', 'Yasin', 'Khan')

def test_auth_register_2():
    auth_register('unusedValidemail@gmail.com', 'validpass', 'Yasin Kevin', 'Peter Steven')

def test_auth_register_3():
    auth_register('unusedValidemail@gmail.com', 'validpass', 'Same', 'Same')

def test_auth_register_4():
    auth_register('unusedValidemail@gmail.com', 'validpass', 'Y()@#@!#*##@', '#@$)(#)$(()#$()(#)@$)')

def test_auth_register_5():
    auth_register('unusedValidemail@gmail.com', 'validpass', 'thisisindeeddefinitelyfiftycharacterslongexactlyxx', 'thisisindeeddefinitelyfiftycharacterslongexactlyxy')

def test_auth_register_6():
    with pytest.raises(ValueError):
        auth_register('validemail2@gamil.com', 'four', 'First', 'Last')

def test_auth_register_7():
    with pytest.raises(ValueError):
        auth_register('validemail2@gamil.com', 'validPasss', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'Last')

def test_auth_register_8():
    with pytest.raises(ValueError):
        auth_register('validemail2@gamil.com', 'validPasss', 'First', 'GreaterthanfiftycharactersLastnamewhichiswaytoolong')

def test_auth_register_9():
    with pytest.raises(ValueError):
        auth_register('already_used_email@gamil.com', 'validPasss', 'First', 'Last')

def test_auth_register_10():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'validPasss', 'First', 'Last')

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