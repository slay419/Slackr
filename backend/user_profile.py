import pytest
from auth_register_test import auth_register
from channels_create_test import channels_create
from channel_join_test import channel_join
from user_profile_sethandle_test import user_profile_sethandle

from .data import *

def user_profile(token,u_id):

    data = get_users()

    if u_id in data:
        valid = 1

    if valid is 0:
        raise ValueError("User ID does not exist")
        return
    else:
        for user in data:
            if user['u_id'] is u_id:
                new_dict = {email:user["email"], name_first:user["firstName"], name_last:user["lastName"], handle_str:user["handle"]}

    return new_dict	#returns dict containing {email,name_first,name_last,handle_str}
