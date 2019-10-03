**Assumptions**

1. Some input names are taken literally. e.g. validemail@gmail.com is a valid
and unique email address. This assumption was made because at the current stage
we have no way of determining whether an email is already used or not.

2. In channel_messages_test.py, the number of messages in a channel is assume 
to be 80. Again for testing purposes there currently is no way of determining 
the total number of messages in a channel.

3. AttributeError is used as a temporary placeholder for AcessError.

4. In tests where an some 'id' is required for input. In order to generate an 
invalid 'id' special numbers such as 12345 have been used and assume to indicate
a channel or user id that does not exist.

5. For the reset_password function 'invalidresetcode' is assumed to be an 
invalid reset code

6. In general, it is assumed all inputs follow the format and data, type as 
as described.

7. For 'channel_messages_test.py' it is assumed that the 'start' paramater is a 
positive integer.
