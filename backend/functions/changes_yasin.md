1. Used helper function: get_u_id() to check whether email is already registered in auth_register. Code is further abstracted and more clear.

2. Added more comments to improve clarity of functions.

3. Abstracted joining process of user to eliminate redudancy of joining in
channel_invite and channel_join

4. Added helper functions to channel_details to remove redundant code that 
was previously in channel_create. channel_details now grabs all necessary 
information from just u_id through helper funcs.