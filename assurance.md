# Acceptances
Acceptance criteria is followed to ensure the implementation is correct and as desired.
Combining both these criteria as well as further testing with Pytest and code coverage, allowed us to be sure
that the backend would be working as intended.

## Auth functions
__As a user I want to able to login so that I can access my Slackr account__

*User Acceptance Criteria*
- There are fields for entering username and password on the login page
- Usernames of valid email format are only accepted
- After successfully logging in, the web server will direct me to the home page where I can access Slackr's features
- If logging in is unsuccessful, an appropriate error message will pop up and allow me to try again

*Acceptance Tests*
- You can succesfully login with pre-registered information
- An attempt to login with non-registered information will return an error

__As a user I want to be able to register so that I can access Slackr services__

*User Acceptance Criteria*
- There is a link for registration on the front page
- Navigating to registration link enables user to create a new account
- On the registration page there are fields for email, password, first name, last name
- Name fields will not allow more than 50 characters for registration
- Password fields must have a minimum of 5 characters for registration
- Registered users are logged in once the process is complete

*Acceptance Tests*
- You can succesfully register with non-registered information
- An attempt to register with already-registered information will return an error

__As a user I want to be able to reset my password so that I can access my account if I forget my password__

*User Acceptance Criteria*
- There is a link for forgotten passwords
- Navigating to a forgotten password link enables users to reset their password
- A reset code is generated when valid information is passed into the fields

*Acceptance Tests*
- On success, a link will be sent to the user containing a redirection to reset the password
- The reset link will only be sent if the user has entered a valid details

__As a user I want the ability to logout so that I can keep my account secure when I am not using it__

*User Acceptance Criteria*
- There is an active logout link when logged in.
- The web server will direct me to the log in page
- The main features of Slackr will no longer be able to be accessed/viewed until logged in again

*Acceptance Tests*
- Once logged out, the user cannot use Slackr without logging back in
- You cannot log out twice.

## Channels functions
__As a user I want the ability to create private channels, so that I can maintain confidentiality__

*User Acceptance Criteria*
-	There is a “Private Channel” checkbox that can be selected when creating a channel
-	The user cannot type more than 20 characters for the name of the channel
-	The user will be labelled as the “owner” of the channel and joined automatically
-	The user will able to see this channel as part of a list of channels already joined
-	Other members will not be able to see messages within the channel before joining

*Acceptance Tests*
-  Private channel messages cannot be seen by those not inside the channel
-  Private channels will show up on the channel list

__As a user I want the ability to create public channels, so that I can have open discussions__

*User Acceptance Criteria*
-	There is a “Public Channel” checkbox that can be selected when creating a channel
-	The user cannot type more than 20 characters for the name of the channel
-	The user will be labelled as the “owner” of the channel and joined automatically
-	The user will able to see this channel as part of a list of channels already joined
-	Other members will be able to see messages within the channel before joining

*Acceptance Tests*
-  Public channel messages can be seen by those not inside the channel
-  Public channels will show up on the channel list

__As a user I want to be able to join a channel so I can send and receive messages with a specific group of people already in the channel__

*User Acceptance Criteria*
-	There is a “Join Channel” button located at the top of the interface, next to the Channel Name, if the user is not part of the channel yet
-	When users interact with the button, the user is now part of the channel and can send messages specifically to that channel/perform channel specific features, e.g. invite
-	Users will now see that channel in their list of channels joined

*Acceptance Tests*
- You can join the channel if you are not already part of it
- Joining will show you the current list of messages

__As a user I want to be able to leave a channel so I can no longer see messages or communicate with a specific group if I do not wish to.__

*User Acceptance Criteria*
-	There is a “Leave Channel” button located at the top of the interface, next to the Channel Name if the user is current part of the channel
-	When users interact with the button, the user is removed from the channel and can no longer send messages specifically to that channel/perform channel specific features e.g. invite
-	Users who previously joined that channel will no longer see it in their list of channels joined

*Acceptance Tests*
- You can leave the channel and are removed from the channel dictionary
- You cannot remove another person from the channe
- Once removed, you cannot see that channel anymore

__As a user I want the ability to invite other users to my channel so that I can collaborate with them__

*User Acceptance Criteria*
- A user within a channel can interact with a button to invite a user that has not joined yet
- The user will be able to input a specific user's ID when activated
- The other user will be automatically joined to the channel
- The other member will not have any owner or admin privileges within the channel unless they are the owner of Slackr
- The other member will be able to interact with the channel as if they joined themselves
- The other member will be included in a list of members

*Acceptance Tests*
- You cannot invite yourself
- You cannot invite another person who is already in the channel
- You can invite users who are not in the channel

__As a user I want the ability to view details on a channel I am part of so that I can get a summary of it__

*User Acceptance Criteria*
- Channel details will be displayed within the channel at the top of the page
- There are two separate lists displayed: Owner and Member lists
- The information will be automatically updated when a new member joins or leaves 

*Acceptance Tests*
- Calling this function will show details of the channel
- You can only call this function if you are in this channel

__As a user I want the ability to see past messages so that I can recollect information__

*User Acceptance Criteria*
- There is a history button that will list a maximum of 50 messages previously sent to the channel
- The list of messages will be ordered from newest to oldest
- If there are less than 50 messages, it will show all of them
- If there are more than 50 messages, it will show only the most recent 50

*Acceptance Tests*
- Calling this function will show at maximum, 50 messages
- You can only call this function if you are in this channel


## Messages functions
__As a user, I want to send messages, so that I can communicate with other people on the platform__

*User Acceptance Criteria*
  - A message bar should exist near the bottom of the chatbox
  - Typed messages are sent by pressing the 'Enter' key
  - The user must type a message at least 1 character long
  - The user must type a message no more than 50 characters long
  - The user can only send messages in a channel they have joined

*Acceptance Tests*
  - The sent messages should be removed added to the channel dictionary
  - You can only send messages to channels you are in

__As an admin, I want to be able to remove messages, so I can filter inappropriate/irrelevant content__

*User Acceptance Criteria*
  - Remove message button accessed by right-clicking an existing message in the chat log
  - The message to be removed must be an existing message
  - The message being removed must be your own message (this does not apply to admins/owners)

*Acceptance Tests*
  - The remove messages should be removed from the channel dictionary
  - It is impossible to remove someone elses message, unless you are authorised

__As an admin, I want to be able to edit messages, so I can rectify wrong/irrelevant information__

*User Acceptance Criteria*
  - Edit message button accessed by right-clicking an existing message in the chat log
  - The new message should also be at least 1 character long
  - The new message should also be no more than 50 characters long
  - The message to be edited must be an existing message
  - The message being edited must be your own message (this does not apply to admins/owners)

*Acceptance Tests*
  - The edited messages should be changed in the channel dictionary
  - It is impossible to edit someone elses message, unless you are authorised

__As a user, I want to be able to react to messages, so I can express my thoughts on a subject__

*User Acceptance Criteria*
  - React message button accessed by right-clicking an existing message in the chat log
  - React icons will appear underneath the message
  - The message being reacted to must be in a channel the user has joined
  - The message being reacted to cannot already have the same reaction

*Acceptance Tests*
  - The reacted message will be changed in the channel dictionary
  - You cannot react to a message you have already reacted to

__As a user, I want to be able to unreact to messages when I change my mind about something__

*User Acceptance Criteria*
  - Unreact message button accessed by right-clicking an existing message in the chat log
  - The message being unreacted to must be in a channel the user has joined
  - The message being unreacted to must have the same reaction

*Acceptance Tests*
  - The unreacted message will be changed in the channel dictionary
  - Only the person who reacted, can unreact

__As an admin, I want to be able to pin messages to highlight important posts so I can organise my channels__

*User Acceptance Criteria*
  - Pinning a message can only be able to be done by admin/owners
  - Pinned messages can be accessed from a button on the top right of the chatbox labelled "Pinned messages"
  - The message to being pinned must not already be pinned
  - The message being pinned must be in a channel joined by the admin

*Acceptance Tests*
 - Pinning a message will remove it from the channel dictionary
 - Only authorised users can pin

__As an admin, I want to be able to unpin messages for when an important messages is no longer relevant__

*User Acceptance Criteria*
  - Unpinning a message can only be able to be done by admin/owners
  - The message to being unpinned must already be pinned
  - The message being unpinned must be in a channel joined by the admin

*Acceptance Tests*
 - Unpinning a message will remove it from the channel dictionary
 - Only authorised users can unpin

__As a user, I want to be able to send messages at later times so that I can set reminders for myself/other members__

*User Acceptance Criteria*
- The “Send Later” feature is next to the message bar at the bottom of the user’s screen
- The user can give an input of a specific time they would like their message to be sent to the channel
- Users cannot type a very long message
- The message is logged after pressing the “Enter” key, and not immediately sent
- The message is sent at the specific time entered by the user

*Acceptance Tests*
- The "Send Later" feature will successfully take a message and send the message later
- The user is cannot 1000 characters into the message bar
- The message is successfully logged onto the channel when submitted

## User Profile functions
__As a user, I want a profile picture, so I can identify others efficiently on the platform__

*User Acceptance Criteria*
- The profile picture is shown on the user profile
- The profile picture is a square, other sizes must be cropped
- The profile picture by default is a grey silhouette
- The profile picture can be changed by clicking on "Change profile picture"
- The profile picture must be between a minimum and maximum size

*Acceptance Tests*
- The user can find and upload a picture as their profile picture
- The user cannot upload a picture with invalid dimensions e.g too large too small
- The user can upload rectangular pictures, and will then crop to size
- The user can upload photos of the minimum and maximum size

__As a user, I want to change my personal information, such as names and email, so that I can also push my latest contact details to others__
*User Acceptance Criteria*
- The user can change their details by clicking "Change details" button on their profile
- The fields contain the current information that can be changed to non-empty and valid information
- The fields cannot be too long and are limited by length
- Only the user can change their own personal information

*Acceptance Tests*
- The user cannot leave required fields empty
- The user can change a non-required filled field to be empty
- The user cannot enter a too-long field

__As a user, I want a handle, so that I can keep my identity private unless divulged.__

*User Acceptance Criteria*
- The user is prompted to create a handle upon account registration.
- The user must not exceed 20 characters for their new handle
- Special characters are valid
- Empty handle is not valid
- The user can change their handle by clicking "Change details" button on their profile
- The user can only modify their own handle

*Acceptance Tests*
- The user can have a handle of pure special characters, up to and including 20 characters but not more
- Leading and trailing spaces are ignored
- The user cannot have an empty handle
- The user cannot enter a too-long handle

## Miscellaneous functions

__As a admin, I want permission controls , so that I can set different users with different privileges and permissions__

*User Acceptance Criteria*
- An admin or owner can promote or demote others
- The function is not avaliable for members
- The admin or owner will go to a users profile to change permissions
-  A member cannot be demoted further nor a admin or owner promoted further
- The permission controls will feature a drop down box to select the new role of the specified user
- Only owners can promote other users to owner

*Acceptance Tests*
- The admin can promote a user to admin
- The owner can promote au user to admin and owner
- The member cannot access this control
- The admin and owner cannot demote a member
- The admin cannot demote a owner

__As a user, I want dedicated support for standups, so that I can organise asynchronised standups that promote buisness__

*User Acceptance Criteria*
- Standups can be initiated by a "Start standup" button on the channel
- The standup will send a notification to users in the channel to remind them
- During the specified 15 minute window, sent messages will appear highlighted to show they are part of the standup
- At the end of the 15 minute window, highlighted messages will be summarised and avaliable to download on the channel settings
- Another standup cannot start until one is finished.

*Acceptance Tests*
- The resulting summary is downloadable
- If no messages are sent in the standup, no summary is generated

__As a user, I want a search bar function, so that I can access archived messages faster and reduce the time taken to find related messages.__

*User Acceptance Criteria*
- The search field is placed on the top
- Search starts once the user clicks search
- The field contains a placeholder stating "Search a word"
- The aforementioned placeholder dissapears once the user starts typing
- Search is performed by the user as long as the field is not empty
- Search function will only return results from channels the user is in

*Acceptance Tests*
- Search field is clearly visible
- Search function will not run with the placeholder
- Search function will not run on empty strings
- The function will return "No results" if no results are found
- Search function will not return results from channels the user is not in
