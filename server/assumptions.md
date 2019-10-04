Add assumptions below:

Globally we assumed
-All users are registered successfully, as there is no way to use these functions
if the user is not registered
-AttributeError is used as a temporary placeholder for AcessError.

25. user_profile_setname:
In this function, we assume
-Assume first name and last name is not empty
-Assume first name and last name does not contain symbols i.e &,%,$,#
We assume this because at the current stage there is no way to determine a valid 
name
-Assume input is entered respectivly to the order specified

26. user_profile_setemail:
In this function, we assume email is not empty because at the current stage 
there is no way to determine a valid email

27. user_profile_sethandle:
In this function, we assume handle is not empty because at the current stage 
there is no way to determine a valid handle

28. user_profiles_uploadphoto:
In this function, we assume
-Assume token is valid
-Assume photo is not empty
-Assume photo dimensions are not negative
-Assume photo fits between a maximum and minimum size
We assume this because at the current stage there is no way to determine if the 
photo fits the screen or not, as well as if the dimensions are possible

29. standup_start:
In this function, we assume
-Assume channel_id is greater than 0 because at the current stage there is no 
way to determine if the channel_id is valid
-As the time_finish type is not specified, it was assumed to be of the "time"
data type
-We also assume the function returns a valid time of 15 minutes consistently

30. standup_send:
In this function, we assume
-Assume the message is not more than 1000 characters as there is not a way to
test the number of characters

31. search:
In this function, we assume
-Assume the search is not empty as it should not continue

32. admin_userpermission_change:
- Assume that the owner and all admin can call this function, 
but anyone else cannot
