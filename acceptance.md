As a user, I want to send messages, so that I can communicate with other people on the platform
-   A message bar should exist near the bottom of the chatbox
-   Typed messages are sent by pressing the 'Enter' key
-   The user must type a message at least 1 character long
-   The user must type a message no more than 50 characters long
-   The user can only send messages in a channel they have joined

As an admin, I want to be able to remove messages, so I can filter inappropriate/irrelevant content
-   Remove message button accessed by right-clicking an existing message in the chat log 
-   The message_id to be removed must belong to a valid message

As an admin, I want to be able to edit messages, so I can rectify wrong/irrelevant information
-   Edit message button accessed by right-clicking an existing message in the chat log   
-   The new message should also be at least 1 character long
-   The new message should also be no more than 50 characters long

As a user, I want to be able to react to messages, so I can express my thoughts on a subject
-   React message button accessed by right-clicking an existing message in the chat log   
-   React icons will appear underneath the message
-   The message being reacted to must be in a channel the user has joined
-   The message being reacted to must have a valid message_id
-   The message being reacted to cannot already have the same reaction
-   The reaction being used must exist with a valid react_id

As a user, I want to be able to unreact to messages when I change my mind about something
-   Unreact message button accessed by right-clicking an existing message in the chat log   

As an admin, I want to be able to pin messages to highlight important posts so I can organise my channels
-   Pin message button accessed by right-clicking an existing message in the chat log   
-   Pinned messages can be accessed from a button on the top right of the chatbox labelled "Pinned messages"
-   The message to being pinned must not already be pinned
-   Only admins can pin messages
-   The message being pinned must be in a channel joined by the admin

As an admin, I want to be able to unpin messages for when an important messages is no longer relevant
-   Unpin message button accessed by right-clicking an existing message in the chat log