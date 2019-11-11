from .data import *

def auth_register(email, password, name_first, name_last):

    data = get_data()
    #check if email already exist
    if valid_email(email) == True:
        if get_u_id(email) != None:
            raise ValueError(f"Email: {email} is already registered")
    else:
        raise ValueError(f"Email: {email} is invalid")

    #rules for length of pasword
    if len(password) < 6: 
        raise ValueError(f"Password Length is too short")

    #rules for first and last name
    if len(name_first) < 1:
        raise ValueError(f"First name: {name_first} is too short")
    elif len(name_first) > 50:
        raise ValueError(f"First name: {name_first} is too long")
    elif len(name_last) < 1:
        raise ValueError(f"Last name: {name_last} is too short")
    elif len(name_last) > 50:
        raise ValueError(f"Last name: {name_last} is too long")

    handle = ''.join((name_first, name_last))
    for user in data['users']: #generate unique handle
        if handle == user['handle']:
            handle += str(1 + len(data['users']))

    hashedPassword = hash_password(password)
    u_id = 101 + len(data['users'])
    token = generate_token(u_id)

    #generate appropriate permission id
    if len(data['users']) == 0:
        permission_id = 1
    else:
        permission_id = 3


    #append all relevant information to users dictionary
    data['users'].append({
        'email' : email,
        'password' : hashedPassword,
        'name_first' : name_first,
        'name_last' : name_last,
        'u_id': u_id,
        'permission_id' : permission_id,
        'handle' : handle,
        'tokens'  : [token],
        'reset_code' : None,
        'profile_img_url' : None
    })
    #auth_login(email, password)
    return {
        'u_id': u_id,
        'token' : token
    }

def auth_login(email, password):

    data = get_data()
    if valid_email(email) == False: #check valid email
        raise ValueError(f"Email: {email} is invalid")

    #check if email exists and if so check if password matches
    for user in data['users']:
        if user['email'] == email and user['password'] == hash_password(password):
            u_id = user['u_id']
            token = generate_token(u_id)
            user['tokens'].append(token)
            return {
                'u_id' : u_id,
                'token': token
            }

    raise ValueError(f"Email: {email} does not exist or password is incorrect")



def auth_logout(token):
    if is_logged_in(token) == True: #only logout if user is already logged in
        u_id = decode_token(token)
        user = user_dict(u_id)
        user['tokens'].remove(token)
        return {'is_success' : True}
    else:
        return {'is_success' : False}


def auth_passwordreset_reset(reset_code, new_password):
    data = get_data()
    if len(new_password) < 6:
        raise ValueError("New password is too short")
    for user in data['users']:
        if user['reset_code'] == reset_code and reset_code != None:
            user['reset_code'] = None
            user['password'] = new_password
            return {}
    raise ValueError(f"User does not exist")
