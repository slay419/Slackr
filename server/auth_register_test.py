import pytest

#Input are taken literally. E.g 'unusedValidemail@gmail.com' is assumed to be an email that is actually unique and valid.

def auth_register(email, password, name_first, name_last):
    pass

def test_auth_register_1():
    assert(auth_register('unusedValidemail@gmail.com', 'validpass', 'Yasin', 'Khan'))

def test_auth_register_2():
    assert(auth_register('unusedValidemail@gmail.com', 'validpass', 'Yasin Kevin', 'Peter Steven'))

def test_auth_register_3():
    with pytest.raises(ValueError):
        auth_register('validemail2@gamil.com', 'four', 'First', 'Last')

def test_auth_register_4():
    with pytest.raises(ValueError):
        auth_register('validemail2@gamil.com', 'validPasss', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'Last')

def test_auth_register_5():
    with pytest.raises(ValueError):
        auth_register('validemail2@gamil.com', 'validPasss', 'First', 'GreaterthanfiftycharactersLastnamewhichiswaytoolong')

def test_auth_register_6():
    with pytest.raises(ValueError):
        auth_register('already_used_email@gamil.com', 'validPasss', 'First', 'Last')

def test_auth_register_7():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'validPasss', 'First', 'Last')

def test_auth_register_8():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'four', 'First', 'Last')

def test_auth_register_9():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'four', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'Last')

def test_auth_register_10():
    with pytest.raises(ValueError):
        auth_register('1nVal1d3mail', 'four', 'Greaterthanfiftycharactersfirstnamewhichiswaytoolong', 'GreaterthanfiftycharactersLastnamewhichiswaytoolong')

def test_auth_register_11():
    with pytest.raises(ValueError):
        auth_register('', '', '', '')