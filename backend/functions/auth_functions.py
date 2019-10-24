from .data import *

def auth_register(email, password, name_first, name_last):


    data = get_data()
    #check if email already exist
    if valid_email(email) == True:
        for user in data['users']:
            if email == user['email']:
                return 'already used email'
    else:
        return 'invalid email'

    if len(password) < 6: #rules for length of pasword
        return 'password too short'


    if len(name_first) < 1 or len(name_first) > 50 or len(name_last) < 1 or len(name_last) > 50: #rules for length of name (first and last)
        return 'names too long/short'

    handle = ''.join((name_first, name_last))
    for user in data['users']:
        if handle == user['handle']:
            handle += str(1 + len(data['users']))

    hashedPassword = hash_password(password)
    u_id = 101 + len(data['users'])
    token = generate_token(u_id)

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
        'reset_code' : None
    })
    #auth_login(email, password)
    return {
        'u_id': u_id,
        'token' : token
    }

def auth_login(email, password):

    data = get_data()
    if valid_email(email) == False: #check valid email
        return 'invalid email'

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

    return 'email does not exist or password is incorrect'



def auth_logout(token):

    u_id = decode_token(token)

    user = user_dict(u_id)
    if user == None:
        return {'is_success' : False}
    user['tokens'].remove(token)

    return {'is_success' : True}

def auth_passwordreset_request(mail, email):
    u_id = get_u_id(email)
    if u_id == None:
        return "email not registered"
    user = user_dict(u_id)

    try:
        msg = Message("Reset Code",
            sender="masterbranch101@gmail.com",
            recipients=[email])
        reset_code = str(u_id) + str(randin(100,999))
        user['reset_code'] = reset_code
        msg.body = f"Your reset code is {reset_code}"
        mail.send(msg)
        return {}
    except Exception as e:
        return (str(e))


def auth_passwordreset_reset(reset_code, new_password):
    data = get_data()
    if len(new_password) < 6:
        return "password entered is not a valid password"
    for user in data['users']:
        if user['reset_code'] == reset_code and reset_code != None:
            user['reset_code'] = None
            user['password'] = new_password
            return {}
    return "user does not exist, althougth this should not ever be returned"
