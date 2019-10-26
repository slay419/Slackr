
## Users functions
As a user, I want a profile picture, so I can identify others effeciently on the platform 
*User Acceptance Criteria*
- The profile picture is shown on the user profile
- The profile picture is a square, other sizes must be cropped
- The profile picture by default is a grey silhouette
- The profile picture can be changed by clicking on "Change profile picture"
- The profile picture must be between a minimum and maximum size
*Acceptance Tests*
-The user can find and upload a picture as their profile picture
-The user cannot upload a picture with invalid dimensions e.g too large too small
-The user can upload rectangular pictures, and will then crop to size
-The user can upload photos of the minimum and maximum size

As a user, I want to change my personal information, so that I can also push my latest contact details to others
*User Acceptance Criteria*
- The user can change their details by clicking "Change details" button on their profile
- The fields contain the current information that can be changed to non-empty and valid information
- The fields cannot be too long and are limited by length
- Only the user can change their own personal information
*Acceptance Tests*
- The user cannot leave required fields empty
- The user can change a non-required filled field to be empty
- The user cannot enter a too-long field

As a user, I want a handle, so that I can keep my identity private unless divulged.
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

## Channels functions
As a user, I want to send messages, so that I can communicate with other people on the platform
  - A message bar should exist near the bottom of the chatbox
  - Typed messages are sent by pressing the 'Enter' key
  - The user must type a message at least 1 character long
  - The user must type a message no more than 50 characters long
  - The user can only send messages in a channel they have joined

As a user I want the ability to invite other users to my channel so that I can collobarate with them
- Can invite a particular user to a channel created by the current logged in user.

As a user I want the ability to view details on a channel I am part of so that I can get a summary of it
- Can view details about any channel the user is currently a member of

As a user I want the ability to see past messages so that I can recollect infomration
- Can view 50 most recent messages from channel user is a member of



As a user I want the ability to create private channels, so that I can maintain confidentiality
-	There is a “Private Channel” checkbox that can be selected when creating a channel
-	The user cannot type more than 20 characters for the name of the channel
-	The user will be labelled as the “owner” of the channel and joined automatically
-	The user will able to see this channel as part of a list of channels already joined
-	Other members will not be able to see messages within the channel before joining

As a user I want the ability to create public channels, so that I can have open discussions
-	There is a “Public Channel” checkbox that can be selected when creating a channel
-	The user cannot type more than 20 characters for the name of the channel
-	The user will be labelled as the “owner” of the channel and joined automatically
-	The user will able to see this channel as part of a list of channels already joined
-	Other members will be able to see messages within the channel before joining

As a user I want to be able to join a channel so I can send and receive messages with a specific group of people already in the channel
-	There is a “Join Channel” button located at the top of the interface, next to the Channel Name, if the user is not part of the channel yet
-	When users interact with the button, the user is now part of the channel and can send messages specifically to that channel/perform channel specific features, e.g. invite
-	Users will now see that channel in their list of channels joined

As a user I want to be able to leave a channel so I can no longer see messages or communicate with a specific group if I do not wish to.
-	There is a “Leave Channel” button located at the top of the interface, next to the Channel Name if the user is current part of the channel
-	When users interact with the button, the user is removed from the channel and can no longer send messages specifically to that channel/perform channel specific features e.g. invite
-	Users who previously joined that channel will no longer see it in their list of channels joined
## Auth functions
As a user I want to able to login so that I can access my slackr account
- There are a fields for entering username and password on the login page
- usernames of valid email format are only accepted

As a user I want to be able to register so that I can access slackr services
- There is a link for registration on the front page
- navigating to registration link enables user to create a new account
- On the registration page there are fields for email, passowrd, first name, last name.
- Name fields will not allow more than 50 characters for registration
- Password fields must have a minimum of 5 characters for registration
- Registered users are logged in once the process is complete

As a user I want to be able to reset my password so that I can access my account if I forget my password
- There is a link for forgotten passwords
- navigating to a forgotton password link enables user to reset password
- A reset code is generated when valid information is passed into the fields

As a user I want the ability to logout so that I can keep my account secure when I am not using it
- There is an active logout link when logged in.

## Messages functions
As a user, I want to send messages, so that I can communicate with other people on the platform
  - A message bar should exist near the bottom of the chatbox
  - Typed messages are sent by pressing the 'Enter' key
  - The user must type a message at least 1 character long
  - The user must type a message no more than 50 characters long
  - The user can only send messages in a channel they have joined

As an admin, I want to be able to remove messages, so I can filter inappropriate/irrelevant content
  - Remove message button accessed by right-clicking an existing message in the chat log 
  - The message to be removed must be an existing message
  - The message being removed must be your own message (this does not apply to admins/owners)

As an admin, I want to be able to edit messages, so I can rectify wrong/irrelevant information
  - Edit message button accessed by right-clicking an existing message in the chat log
  - The new message should also be at least 1 character long
  - The new message should also be no more than 50 characters long
  - The message to be edited must be an existing message
  - The message being edited must be your own message (this does not apply to admins/owners)

As a user, I want to be able to react to messages, so I can express my thoughts on a subject
  - React message button accessed by right-clicking an existing message in the chat log
  - React icons will appear underneath the message
  - The message being reacted to must be in a channel the user has joined
  - The message being reacted to cannot already have the same reaction

As a user, I want to be able to unreact to messages when I change my mind about something
  - Unreact message button accessed by right-clicking an existing message in the chat log
  - The message being unreacted to must be in a channel the user has joined
  - The message being unreacted to must have the same reaction

As an admin, I want to be able to pin messages to highlight important posts so I can organise my channels
  - Pinning a message can only be able to be done by admin/owners
  - Pinned messages can be accessed from a button on the top right of the chatbox labelled "Pinned messages"
  - The message to being pinned must not already be pinned
  - The message being pinned must be in a channel joined by the admin

As an admin, I want to be able to unpin messages for when an important messages is no longer relevant
  - Unpinning a message can only be able to be done by admin/owners
  - The message to being unpinned must already be pinned
  - The message being unpinned must be in a channel joined by the admin

As a user, I want to be able to send messages at later times so that I can set reminders for myself/other members
-	The “Send Later” feature is next to the message bar at the bottom of the user’s screen
-	The user can give an input of a specific time they would like their message to be sent to the channel
-	Users cannot type more than 1000 characters into the message bar
-	The message is logged after pressing the “Enter” key, and not immediately sent
-	The message is sent at the specific time entered by the user


## Miscellaneous functions

As a admin, I want permission controls , so that I can set different users with different privileges and permissions 
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

As a user, I want dedicated support for standups, so that I can organise asynchronised standups that promote buisness
*User Acceptance Criteria*
- Standups can be initiated by a "Start standup" button on the channel
- The standup will send a notification to users in the channel to remind them
- During the specified 15 minute window, sent messages will appear highlighted to show they are part of the standup
- At the end of the 15 minute window, highlighted messages will be summarised and avaliable to download on the channel settings
- Another standup cannot start until one is finished.
*Acceptance Tests*
- The resulting summary is downloadable
- If no messages are sent in the standup, no summary is generated

As a user, I want a search bar function, so that I can access archived messages faster and reduce the time taken to find related messages.
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








