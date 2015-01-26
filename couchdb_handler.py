from couchdb import *
from couchdb.design import ViewDefinition

# Creates a connection
def connect_to_db():
	#couch.resource.credentials = ("admin", "admin")
	return Server('http://localhost:5984')

# Creates a DB or loads it
def create_or_load_db( couch, database_name ):
	# Try to get the database 
	try:
		return couch[ database_name ]
	# Or create it if it is not already
	except ResourceNotFound:
		return couch.create( database_name )

def add_user( user, macs ):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	# Let's check if the user exists already by trying to get it, and if it is not here, it means we can add it 
	try:
		#You can then use the object *db* to directly check a document through its _id, remember that we use urls as ids since a url is unique
		doc = db[ user ]
		#The object *doc* contains the document from the users databse which _id is url_rss
		print "[couch-add_user] %s is already a user in the database" % user
	except ResourceNotFound:
		dict_field_values = {
			'_id'  : user,
			'macs'  :macs
		}
		#The object *db* has a create method, and this is how you create a document
		return db.create( dict_field_values )

def create_view_for_macs():
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	rpt_view = ViewDefinition(
			'list',
			'macs',
			'''function(doc) {
				for( i in doc.macs ){
                 		emit( doc.macs[i], doc._id  );}
			}''')
	rpt_view.sync( db )
	
	rpt_view = ViewDefinition(
			'list',
			'last_seen',
			'''function(doc) {
				emit(doc.last_seen_time, doc._id);
			}''')
	rpt_view.sync( db )
	


def retrieve_user_for_mac( mac ):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	for row in db.view( "_design/list/_view/macs" ):
		if mac == row.key:
			print
			print mac, row.id
	return row.id

def update_last_seen_time( user, time ):
	
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	

	doc = db[ user ]
	doc['last_seen_time'] = time

	db.save(doc)
	
	
def display_status():
	couch = connect_to_db()
	db = create_or_load_db(couch, 'inhabitants')
	
	
	all_status=[]
	for row in db.view('_design/list/_view/last_seen'):
		list_user_status =[]
		user = row.id
		last_seen_time = row.key
		
		
		list_user_status.append(user)
		list_user_status.append(last_seen_time)
		
		all_status.append(list_user_status)
		
	return all_status

	








