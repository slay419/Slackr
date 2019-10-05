Add assumptions below:
'''
####################### STEVENS' ASSUMPTIONS #####################
All test assume that nothing (users/channels/reacts/messages) exist prior to testing
All test assume that user1 and user2 are normal users and admin1 and admin2 are admins
It is assumed that messages sent must be atleast one character long
It is assumed that the admin is logged in and any other messages are coming from
other users from different locations
Assume reacts_id's exist from 0 -> 50
Assume NONE is returned in handle_str field if no handle has been set
'''


#####################   ASSUMPTIONS FOR ADMINS/OWNERS/USERS   #################  
1) Admins are the very FIRST person to ever sign up to Slackr.  
2) Owners are the very FIRST person to create a channel using `channels_create()`.  
3) Members are other users who can join channels.  
4) Owner privileges exist ONLY within the channel created.  
5) Admin privileges exist THROUGHOUT Slackr, i.e. every channel.  



#########################  ASSUMPTIONS FOR CHANNELS   ########################  
1) The name of channels using `channels_create()` should be at least one character long.  
2) The channel ID number generated when using `channels_create()` will produce ID numbers in ascending order.  
    - i.e. channel_id1 created first will have a lower number than channeld_id2 created later.  
3) The user who created the channel using `channels_create()` will have *Owner* privileges for that channel, and is automatically joined.  
4) Channels must be created first before joining using `channel_join()`, and you cannot join a channel you are already in.  
    - i.e. "ValueError: Channel does not exist" means the channel has not been created yet, OR has already been joined by the user.  
5) Users can only join a channel as a *Member* and can only be promoted by the *Owner* of the channel or and *Admin*.  
6) Similarly, channels must be created and joined first before leaving using `channel_leave()`- you cannot leave a channel you have not joined yet.  
    - i.e. "ValueError: Channel does not exist" means the channel has not been created yet OR has not been joined yet.  
7)
