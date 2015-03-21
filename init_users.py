#You absolutely need these 2 imports at the beginning of your script to be able to use these functions, also you must be in the same folder
from couchdb_handler import *
import couchdb


#Create a new user
user = "Ilyass"
macs = ["8C:3A:E3:3E:56:26"]
url_img = 'https://lh6.googleusercontent.com/-wE_smH6tICw/ThTE50L4KNI/AAAAAAAASVI/M8LjNWA7dNs/w1051-h701-no/IMG_3687.JPG'
#The function add_user checks if the user is already existing in the database
add_user( user, macs ,url_img)

user = "Joe"
macs = ["BC:77:37:E7:0B:49", "34:FC:EF:CB:A1:BB" ]
url_img = 'https://lh6.googleusercontent.com/kY8GSNBoURvFIXX2ox55AmN1QF7p-RbZsOhw_QyRsw=w717-h701-no'
add_user( user, macs ,url_img)

user = "Yahya"
macs = ["98:D6:F7:6A:52:13", "80:56:F2:70:85:DB" ]
url_img = 'https://lh4.googleusercontent.com/-yGbpROABGlw/UHFTVY4qQ9I/AAAAAAAAAKg/AiluU0GSaIE/w601-h602-no/IMG_3361.JPG'
add_user( user, macs ,url_img)

user = "Gael"
macs = ["40:78:6A:C2:1C:06","80:56:F2:08:AE:45"]
url_img = 'https://fbcdn-sphotos-h-a.akamaihd.net/hphotos-ak-xpf1/v/t1.0-9/p206x206/10464400_10152450938589754_9088480680765082395_n.jpg?oh=1ed8fd4b01afeebf28866ce098fb02c6&oe=55827C27&__gda__=1435651377_3946885bf0ad47479018f6c1b361c95e'
add_user( user, macs ,url_img)

#Creates a view in CouchDB which allows us to use retrieve_user_for_mac( mac 
create_view_for_macs( )
create_view_for_house()
# Retrieve the user corresponding to a MAC address
#mac = "98:D6:F7:6A:52:13"
#retrieve_user_for_mac( mac )


#Update a user's last_seen_time

#update_last_seen_time( "ilyass", "now" )
#update_last_seen_time( "lussylver", "yesterday" )
#update_last_seen_time( "joe", "tomorrow" )

#How to display data
all_status = display_status()
for list_user in all_status:
	print str(list_user[0]), "=", str(list_user[1])
