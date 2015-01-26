#You absolutely need these 2 imports at the beginning of your script to be able to use these functions, also you mest be in the same folder
from couchdb_handler import *
import couchdb


#Create a new user
user = "ilyass"
macs = ["8C:3A:E3:3E:56:26"]
#The function add_user checks if the user is already existing in the database
add_user( user, macs )

user = "joe"
macs = ["BC:77:37:E7:0B:49", "34:FC:EF:CB:A1:BB" ]
add_user( user, macs )

user = "lussylver"
macs = ["98:D6:F7:6A:52:13", "80:56:F2:70:85:DB" ]
add_user( user, macs )



#Creates a view in CouchDB which allows us to use retrieve_user_for_mac( mac 
create_view_for_macs( )



# Retrieve the user corresponding to a MAC address
mac = "98:D6:F7:6A:52:13"
retrieve_user_for_mac( mac )


#Update a user's last_seen_time
update_last_seen_time( "ilyass", "now" )
update_last_seen_time( "lussylver", "yesterday" )
update_last_seen_time( "joe", "tomorrow" )

#How to display data
all_status = display_status()
for list_user in all_status:
	print str(list_user[0]), "=", str(list_user[1])
