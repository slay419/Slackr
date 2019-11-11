## Changes made by Kevin

1. Helper function was created: `remove_from_list()`.
This was done since the same loop was done for multiple functions: `channel_leave()` & `channel_removeowner()`.
The process of removing a user from a specific list in the database was abstracted and made simpler for
the mentioned functions.

2. Helper functions replaced starting code wherever possible for error handling. E.g. When checking
if the channel ID is valid, `is_valid_channel()` would be called. This would keep the code simpler
and easier to read.
