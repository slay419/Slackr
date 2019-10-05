
**ASSUMPTIONS FOR ADMINS/OWNERS/USERS**  
1. Admins are the very FIRST person to ever sign up to Slackr.  
2. Owners are the very FIRST person to create a channel.
3. Members are other users who join channels.  
4. Owner privileges exist ONLY within the channel created.  
5. Admin privileges exist THROUGHOUT Slackr, i.e. every channel.


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
1. It is assumed that messages sent must be at least one character long.  
2. It is assumed that the admin is logged in and any other messages are coming from other users from different locations.  
3. Assume react ID's exist from 0 to 50.  
4. Assume `NONE` is returned in `handle_str` field if no handle has been set.  


**ASSUMPTIONS FOR TESTS**  
1. All tests assume that nothing (users/channels/reacts/messages) exist prior to testing
2. All test assume that user1 and user2 are normal users and admin1 and admin2 are admins
3. Some input names are taken literally. e.g. *validemail@gmail.com* is a valid
and unique email address. This assumption was made because at the current stage
we have no way of determining whether an email is already used or not.  
4. AttributeError is used as a temporary placeholder for AcessError.  
5. For tests where an 'id' is required for input: in order to generate an
invalid 'id', special numbers such as '12345' have been used and assumed to indicate
a channel or user id that has not been created yet.  
6. For the `reset_password()` function 'invalidresetcode' is assumed to be an
invalid reset code.  
7. In general, it is assumed all inputs follow the format and data, type as
as described.
8. In `channel_messages_test()`, the number of messages in a channel is assumed
to be 80. For testing purposes there currently is no way of determining
the total number of messages in a channel.
