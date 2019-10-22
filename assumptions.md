**ASSUMPTIONS FOR ADMINS/OWNERS/USERS**  
1. Admins are the very FIRST person to ever sign up to Slackr.  
2. Owners are the very FIRST person to create a channel.
3. Members are other users who join channels.  
4. Owner privileges exist ONLY within the channel created.  
5. Admin privileges exist THROUGHOUT Slackr, i.e. every channel.
6. Users successfully calling `admin_userpermission_change()` can only be an admin or owner.


**ASSUMPTIONS FOR CHANNELS**  
1. The name of channels using `channels_create()` should be at least one character long.  
2. The channel ID number generated when using `channels_create()` will produce ID numbers in ascending order.  
    - i.e. channel_id1 created first will have a lower number than channeld_id2 created later.
3. The user who created the channel using `channels_create()` will have *Owner* privileges for that channel, and is automatically joined.  
4. Channels must be created first before joining using `channel_join()`, and you cannot join a channel you are already in.  
    - i.e. "ValueError: Channel does not exist" means the channel has not been created yet, OR has already been joined by the user.  
5. Users can only join a channel as a *Member* and can only be promoted by the *Owner* of the channel or and *Admin*.  
6. Similarly, channels must be created and joined first before leaving using `channel_leave()`- you cannot leave a channel you have not joined yet.  
    - i.e. "ValueError: Channel does not exist" means the channel has not been created yet OR has not been joined yet.  
7. Members can only be promoted by Owners or Admins using `channel_addowner()`.  
8. An owner of a channel cannot be removed with `channel_removeowner()` if they are the only *Owner* left in the channel.  
9. The order of the lists returned by `channel_list()` and `channel_listall()` is determined by ascending order of channel ID.  
    - i.e. The order of the lists are in order of when the channels were created, NOT joined by a user.
10. The `start` index paramater used in `channel_messages()` is assumed to be a positive integer.  


**ASSUMPTIONS FOR MESSAGES**  
1. Messages sent using `message_send()` & `message_sendlater()` must be at least one character long.  
2. It is assumed that the admin is logged in and any other messages are coming from other users from different locations.  
3. Assume react ID's exist from 0 to 50.  
4. Assume `NONE` is returned in `handle_str` field if no handle has been set.  
5. The function `message_sendlater()` will analyse time accurate to one second, and 'time in the past' means any time before the current time on the user's system.  
6. If the `time_sent` parameter given to `message_sendlater()` is the current time, then it will behave exactly as `message_send()` and send the message immediately.   
7. When conducting standup meetings using `standup_start()`, there are no permissions required, and there cannot be two running simultaneously on the same channel.  
8. Messages sent using `standup_send()` can only be done after successfully starting `standup_start()` first. Messages sent this way must also be at least 1 character long.  
9. Messages found using `search()` must be at least one character long.  
10. Searching will be 'find-in-word' and NOT case-sensitive.  
    - i.e searching for 'a' will result in 'example' because the letter 'a' is present.  


**ASSUMPTIONS FOR PROFILES**
1. Names and handles used in `user_profile_setname()` & `user_profile_sethandle()` are allowed to have special characters and numbers e.g. 'Name123!@#'.  
2. Names and handles must be at least one character long - a ValueError will occur when 0 characters are entered in `user_profile_setname()` & `user_profile_setname()`.  
3. Two people may have the same name or handle.
4. Users can only set their own name and cannot access another user's name.
5. Users can only change their own handles if they wish, but not others. Admins or owners are the only ones able to do so.
6. Users can only set their own email addresses in their profile using `user_profile_setemail()`.  
7. Email addresses must be at least one character long and must be valid.  
    - i.e. must have text and an address e.g. "text@address.com".  
8. When uploading a photo using `user_profiles_uploadphoto()`, the only valid URL code is 200, and its status is accessible and not blocked by third party security.  
9. The image will be non-empty, square size with a minimum size of 200x200 and maximum of 1000x1000, and also be of a compatible type, e.g. .JPEG, .PNG, etc.  
10. Assume start and end are interchangable, as long as the area is valid.   


**ASSUMPTIONS FOR TESTS**  
1. All tests assume that nothing (users/channels/reacts/messages) exist prior to testing
2. All test assume that user1 and user2 are normal users and admin1 and admin2 are admins
3. For tests where an 'id' is required for input: in order to generate an
invalid 'id', special numbers such as '12345' have been used and assumed to indicate
a channel or user id that has not been created yet.  
4. For the `reset_password()` function 'invalidresetcode' is assumed to be an
invalid reset code.
5. In `channel_messages_test()`, the number of messages in a channel is assumed
to be 80. For testing purposes there currently is no way of determining
the total number of messages in a channel.
6. In `admin_userpermission_change()`, the `permission_id` parameter is either 1, 2, or 3 as specified by the data table. This function will also not produce an error if the permission change is the same.  
7. Assume all time variables are returned as a `datetime` object in `standup_start()` & `standup_send()`.
