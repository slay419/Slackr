import pytest
from auth_login_test import auth_login 
import requests
## 'Requests' will provide clarity to the status of an URL

'''
####################### ASSUMPTIONS ######################
Assume URL code 200 to be the only valid URL code
URL status is accessible and not blocked by third party security
Image size fits between a minimum and maximum size, for this case, 
assume minimum is 200x200 and maximum is 1000x1000
Assume the photo is not empty i.e all dimensions are 0
Assume the photo to be of a compadible type, e.g .JPEG, .PNG, etc
Assume https://somewebsite to be invalid for testing purposes and
https://www.google.com to be valid for testing
Assume start and end are interchangable, as long as the area is valid
Assume the picture is a square and will return invalid otherwise
'''


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
	if dimensions_valid(x_start, y_start, x_end, y_end) is 0:
		raise ValueError("Dimensions do not form a rectangle")
	pass
	
'''
Returns 1 if the dimensions are valid i.e form a square within min and max size
Returns 0 if the dimensions are invalid i.e do not form a square or to small or too big
Min size = 200 x 200
Max size = 1000 x 1000
'''
def dimensions_valid(x_start, y_start, x_end, y_end):
	pass

######################## GLOBAL VARIABLES SETUP ######################

userDict = auth_login("person1@gmail.com", "password")
u_token = userDict1['token']

##########################    END SETUP   ########################

# Test an invalid URL
def user_profiles_uploadphoto_1():
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://somewebsite", 0, 0, 200, 200)

# Test an invalid dimensions
def user_profiles_uploadphoto_2():	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://www.google.com", -200, -200, 200, 200)
	
# Test a picture too small
def user_profiles_uploadphoto_3():	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://www.google.com", 0, 0, 100, 100)

# Test a picture too small
def user_profiles_uploadphoto_4():	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://www.google.com", 100, 100, 0, 0)

# Test a picture too large
def user_profiles_uploadphoto_5():	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://www.google.com", 2000, 2000, 0, 0)

# Test a picture too large
def user_profiles_uploadphoto_6():	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://www.google.com", 0, 0, 400, 500)

# Test a picture that is a rectangle
def user_profiles_uploadphoto_7():	
	with pytest.raises(ValueError):
		user_profiles_uploadphoto(u_token, "https://www.google.com", 300, 400, 100, 100)
		
# Test a valid picture
def user_profiles_uploadphoto_8():	
	user_profiles_uploadphoto(u_token, "https://www.google.com", 0, 0, 300, 300)

# Test a valid picture
def user_profiles_uploadphoto_9():	
	user_profiles_uploadphoto(u_token, "https://www.google.com", 400, 400, 0, 0)

# Test a valid picture
def user_profiles_uploadphoto_10():	
	user_profiles_uploadphoto(u_token, "https://www.google.com", 700, 700, 300, 300)

# Test a valid picture
def user_profiles_uploadphoto_11():	
	user_profiles_uploadphoto(u_token, "https://www.google.com", 8500, 700, 8100, 300)
