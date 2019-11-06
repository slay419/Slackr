#MANUAL TESTING HAS BEEN DONE ON SERVER SIDE

#FUNCTION REQUIRES CALL FROM auth_passwordreset_request() which can only be called when server.py is running. (For more details please check test_auth_passwordreset_request.py)


'''

#Valid reset code and valid password
def test_auth_passwordreset_reset_1():
    
    auth_passwordreset_reset('validresetcode', 'newpassword')

#valid reset code and valid password
def test_auth_passwordreset_reset_2():
    auth_passwordreset_reset('validresetcode', 'fivel')

#valid reset code and invalid password (less than 5 characters)
def test_auth_passwordreset_reset_3():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('validresetcode;', '@#%')

#valid reset code and invalid password (less than 5 characters)
def test_auth_passwordreset_reset_4():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('validresetcode;', 'four')

#invalid reset code and valid pass
def test_auth_passwordreset_reset_5():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('invalidresetcode;', 'validpassowrd')

#invalid reset code and invalid pass
def test_auth_passwordreset_reset_6():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('invalidresetcode;', 'four')

#invalid reset code and invalid pass
def test_auth_passwordreset_reset_7():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('invalidresetcode;', '$@!')

#invalid reset code and invalid pass
def test_auth_passwordreset_reset_8():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('', '$@!')

#invalid reset code and invalid pass
def test_auth_passwordreset_reset_9():
    with pytest.raises(ValueError):
        auth_passwordreset_reset('', 'validpassword')

#reset password twice 
def test_auth_passwordreset_reset_10():
    auth_passwordreset_reset('validresetcode', 'validpassword')
    auth_passwordreset_reset('validresetcode', 'validpassword2')

#reset password twice (second time invalid resetcode)
def test_auth_passwordreset_reset_11():
    auth_passwordreset_reset('validresetcode', 'validpassword')
    auth_passwordreset_reset('invalidresetcode', 'validpassword2')
'''

import pytest
from auth_passwordreset_request_test import auth_passwordreset_request
from functions.data import *
from functions.auth_functions import auth_register, auth_passwordreset_reset

def test_1():
    reset_data()
    dict1 = auth_register('yasin.k101@gmail.com', 'mypass1234', 'Yasin', 'Khan')
    u_id = dict1['u_id']
    auth_passwordreset_request('yasin.k101@gmail.com')
    user = user_dict(u_id)
    reset_code = user['reset_code']
    auth_passwordreset_reset(reset_code, 'newpassword')
    assert(user['password'] == 'newpassword')

def test_2():
    reset_data()
    dict1 = auth_register('yasin.k101@gmail.com', 'mypass1234', 'Yasin', 'Khan')
    u_id = dict1['u_id']
    auth_passwordreset_request('yasin.k101@gmail.com')
    user = user_dict(u_id)
    reset_code = user['reset_code']
    assert(u_id == int(reset_code[:3]))
