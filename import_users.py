import yaml, os
from models import User

def get_users():
    script_dir = os.path.dirname(__file__)
    try:
        with open(os.path.join(script_dir, "users.yml"), 'r') as ymlfile:
            users = yaml.load(ymlfile)
            return users
    except Exception as e:
        raise e

users = get_users()
for user in users:
    User(user.name, user.mac_addresses, user.image, user.song)

#Creates a view in CouchDB which allows us to use retrieve_user_for_mac( mac 
# create_view_for_macs( )
# create_view_for_house()
