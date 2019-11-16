import urllib.request
from PIL import Image
from .data import decode_token, valid_email, is_email_free, user_dict, get_data
from .exceptions import ValueError, AccessError


def user_profile_setemail(token, email):
    # Using helper functions, return data
    u_id = decode_token(token)
    user_data = user_dict(u_id)
    # Raise errors if the user and email are not valid
    if valid_email(email) is False:
        raise ValueError(f"Email: {email} entered is not a valid email")
    if is_email_free(email) == 0:
        raise ValueError(f"Email: {email} is already in use")
    # At this point, the email is valid and untaken, so replace the old one

    user_data['email'] = email
    print("Successfully updated user's email")

    return {}


def user_profile_sethandle(token, handle_str):
    # Using helper functions, return data
    u_id = decode_token(token)
    user_data = user_dict(u_id)
    # Raise errors if the user and handle are not valid
    if len(handle_str) > 20:
        raise ValueError(f"Handle: {handle_str} is larger than 20 characters")
    if len(handle_str) < 1:
        raise ValueError("Handle cannot be empty")
    # At this point, the handle is valid, so replace the old one
    user_data['handle'] = handle_str
    print("Successfully updated user's handle")

    return {}

def user_profile_setname(token, name_first, name_last):
    # Using helper functions, return data
    u_id = decode_token(token)
    user_data = user_dict(u_id)
    # Raise errors if the user and names are not valid
    if len(name_first) > 50:
        raise ValueError(f"First name: {name_first} is longer than 50 characters")
    if len(name_first) < 1:
        raise ValueError(f"First name: {name_first} cannot be empty")
    if len(name_last) > 50:
        raise ValueError(f"Last name: {name_last} is longer than 50 characters")
    if len(name_last) < 1:
        raise ValueError(f"Last name: {name_last} cannot be empty")
    # At this point, the names are valid, so replace the old one
    user_data['name_first'] = name_first
    user_data['name_last'] = name_last
    print("Successfully updated user's first and last name")

    return {}

def user_profile(token, u_id):
    # Using helper functions, return data
    user_data = user_dict(u_id)
    # Raise errors if the user and names are not valid
    if user_data == None:
        raise ValueError(f"User ID: {u_id} does not exist")
    # Return the user dictionary of information
    new_dict = {
        'email': user_data['email'],
        'name_first': user_data['name_first'],
        'name_last': user_data['name_last'],
        'handle_str': user_data["handle"]
    }
    # Returns dict containing {email,name_first,name_last,handle_str}
    print("Successfully found and located user's information")
    return new_dict

def user_profile_uploadphoto(token, img_url, x_start, y_start, x_end, y_end):
    # Append img_url to user data
    data = get_data()
    user = user_dict(decode_token(token))
    user['profile_img_url'] = img_url
    # Extract the image from the URL and store at 'file_path' location

    # Create a counter to store unique photos i.e photo1.png, photo2.png etc
    # At the moment this doesnt work because I haven't made it global so it
    # will always be 1
    n_users = len(data['users'])
    file_path = "backend/functions/pictures/profile_pic" + str(n_users) + ".jpg"
    # Save the picture from the URL to the file_path
    urllib.request.urlretrieve(img_url, file_path)
    # Print to debug to terminal
    print("Successfully saved the user image")

    # Crop picture section
    # Open the image
    image_object = Image.open(file_path)
    # Crop to dimensions and save
    cropped = image_object.crop((x_start, y_start, x_end, y_end))
    cropped.save(file_path)
    # Print to debug to terminal
    print("Successfully cropped the user image")
    # Return nothing as specified
    return{}

def user_listall(token):
    data = get_data()
    user_list = []
    for user_dict in data['users']:
        # Extract the relevant info into a dictionary and append to a list to return
        dict = {
            'u_id': user_dict['u_id'],
            'email': user_dict['email'],
            'name_first': user_dict['name_first'],
            'name_last': user_dict['name_last'],
            'handle_str': user_dict['handle'],
            'profile_img_url': user_dict['profile_img_url']
        }
        user_list.append(dict)

    return {'users': user_list}
