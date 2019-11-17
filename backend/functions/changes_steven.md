1. Created get_channel_id helper function for obtaining a channel_id from a message_id. This is used in message_pin/unpin

2. Created remove_channel_message_dict helper function for removing channel specific message dicts. This is used in message_remove

3. Abstracted some code by using helper functions

4. Created more tests for conditions not met in coverage

5. Cleaned up all code in accordance to pylint

6. Fixed up reacts from iteration 2 to constantly update and check in channel messages
