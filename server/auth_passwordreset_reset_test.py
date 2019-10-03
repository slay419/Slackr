import pytest

def auth_passwordreset_reset(reset_code, new_password):
    pass

def test_auth_passwordreset_reset_1():
    auth_passwordreset_reset('validresetcode', 'validpassowrd')

def test_auth_passwordreset_reset_2():
    auth_passwordreset_reset('validresetcode', 'fivel')

def test_auth_passwordreset_reset_3():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('validresetcode;', '@#%')

def test_auth_passwordreset_reset_4():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('validresetcode;', 'four')

def test_auth_passwordreset_reset_5():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('invalidresetcode;', 'validpassowrd')

def test_auth_passwordreset_reset_6():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('invalidresetcode;', 'four')

def test_auth_passwordreset_reset_7():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('invalidresetcode;', '$@!')

def test_auth_passwordreset_reset_8():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('', '$@!')

def test_auth_passwordreset_reset_9():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('', 'validpassword')