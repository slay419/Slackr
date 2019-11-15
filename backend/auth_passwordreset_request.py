import pytest
from flask_mail import Mail, Message
from flask import Flask, request
from functions.auth_functions import auth_register
from functions.data import *

from backend.functions.exceptions import ValueError, AccessError

#MANUAL TESTING HAS BEEN DONE ON THE SERVER SIDE. Since auth_password_request()
# requires configuration set up on the flask server that is established when running server.py

#i.e lines 25-31 (server.py)

'''

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'masterbranch101@gmail.com',
    MAIL_PASSWORD = "comp1531"
)


'''

# line 95 (server.py)

'''
mail = Mail(APP)

'''

APP = Flask(__name__)

APP.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'masterbranch101@gmail.com',
    MAIL_PASSWORD = "comp1531"
)
APP.run(port=5003)

def auth_passwordreset_request(email):

    mail = Mail(APP)
    u_id = get_u_id(email)
    if u_id == None:
        raise ValueError(f"Email: {email} not registered")
    user = user_dict(u_id)

    try:
        msg = Message("Reset Code",
            sender="masterbranch101@gmail.com",
            recipients=[email])
        reset_code = str(u_id) + str(randint(100,999))
        user['reset_code'] = reset_code
        msg.body = f"Your reset code is {reset_code}"
        mail.send(msg)
        return {}
    except Exception as e:
        return (str(e))

def test_auth_passwordreset_request_1():
    #reset_data()
    #dict1 = auth_register('yasin.k101@gmail.com', 'mypass1234', 'Yasin', 'Khan')
    #u_id = dict1['u_id']

  #  auth_passwordreset_request('yasin.k101@gmail.com')

   # user = user_dict(u_id)
   # reset_code = user['reset_code']
  #  assert(u_id == int(reset_code[:3]))


    #exit()
    pass
