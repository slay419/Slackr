

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


As a user I want to able to login so that I can access my slackr account
1. There are a fields for entering username and password on the login page
2. usernames of valid email format are only accepted

As a user I want to be able to register so that I can access slackr services
1. There is a link for registration on the front page
2. navigating to registration link enables user to create a new account
3. On the registration page there are fields for email, passowrd, first name, last name.
4. Name fields will not allow more than 50 characters for registration
5. Password fields must have a minimum of 5 characters for registration
6. Registered users are logged in once the process is complete

As a user I want to be able to reset my password so that I can access my account if I forget my password
1. There is a link for forgotten passwords
2. navigating to a forgotton password link enables user to reset password
3. A reset code is generated when valid information is passed into the fields

As a user I want the ability to logout so that I can keep my account secure when I am not using itt
1. There is an active logout link when logged in.

As a user I want the ability to invite other users to my channel so that I can collobarate with them
1. Can invite a particular user to a channel created by the current logged in user.

As a user I want the ability to view details on a channel I am part of so that I can get a summary of it
1. Can view details about any channel the user is currently a member of

As a user I want the ability to see past messages so that I can recollect infomration
1. Can view 50 most recent messages from channel user is a member of



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

As a user, I want to be able to send messages at later times so that I can set reminders for myself/other members
-	The “Send Later” feature is next to the message bar at the bottom of the user’s screen
-	The user can give an input of a specific time they would like their message to be sent to the channel
-	Users cannot type more than 1000 characters into the message bar
-	The message is logged after pressing the “Enter” key, and not immediately sent
-	The message is sent at the specific time entered by the user

