import pytest
from auth_login_test import auth_login
import requests

## This function does:
## Given a URL of an image on the internet, crops the image within bounds 
## (x_start, y_start) and (x_end, y_end). 
## Position (0,0) is the top left.

## Function will fail if:
## 1. img_url is returns an HTTP status other than 200.
## 2. x_start, y_start, x_end, y_end are all within the dimensions of the image at the URL.

def user_profiles_uploadphoto(token, img_url, x_start, y_start, x_end, y_end)
	HTTPStatus = img_url.status_code
	
	if HTTPStatus is not 200:
		raise ValueError("URL is invalid")
	if x_start < 0 or y_start < 0 or x_end < 0 or y_end < 0:
		raise ValueError("Dimensions are invalid for image")


def test_invalid_url():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(intendedUser, "https://somewebsite", 0, 0, 200, 200)

def test_invalid_dimensions():
	userDictionary = auth_login('johnsmith123@gmail.com', 'password123')
	intendedUser = userDictionary['token']
	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(intendedUser, "https://somewebsite", -200, -200, 200, 200)
		user_profiles_uploadphoto(intendedUser, "https://somewebsite", -200, -200, 200, 200)