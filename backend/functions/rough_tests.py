from auth_functions import *
from channel_functions import *
#from .data import *



dict = auth_register('yasin@gmail.com', 'testpass1', 'Yasin', 'Khan')

dict10 = auth_register('kevin@gmail.com', 'testpass3', 'Kevin', 'Chau')
dict11 = auth_register('steven@gmail.com', 'testpass2', 'Steven', 'Lay')
dict12 = auth_register('peter@gmail.com', 'testpass4', 'Peter', 'Chen')
u_id10 = dict10['u_id']
u_id11 = dict11['u_id']
u_id12 = dict12['u_id']

token =  dict['token']

#print(auth_register('steven@gmail.com', 'testpass2', 'Steven', 'Lay'))
#print(auth_register('kevin@gmail.com', 'testpass3', 'Kevin', 'Chau'))
#print(auth_register('peter@gmail.com', 'testpass4', 'Peter', 'Chen'))
#print(auth_register('yasin@gmail.com', 'testpass1', 'Yasin', 'Khan'))
#print(auth_login('yasin@gmail.com', 'testpass1'))



dict2 = channels_create(token, 'yasinschannel', 1)
channel_id = dict2['channel_id']
#print(data)
channel_invite(token, channel_id, u_id10)
#print(data)
channel_invite(token, channel_id, u_id11)
channel_invite(token, channel_id, u_id12)
print(channel_details(token, channel_id))