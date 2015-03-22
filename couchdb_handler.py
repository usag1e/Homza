from couchdb import *
import time
from couchdb.design import ViewDefinition
import urllib2

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

def add_user( user, macs , url_img , music):
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
			'macs'  :macs,
			'url_img' : url_img,
			'last_played_music' : retrieve_time(),
			'last_arrived_home:': retrieve_time(),
			'music' : music
		}
		#The object *db* has a create method, and this is how you create a document

		return db.create( dict_field_values )

def retrieve_music(user):
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )	
	for row in db.view( "_design/list/_view/music_name" ):
		if user==row.value:
			music=row.key
	return music
	

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
				emit(doc.presence[doc.presence.length - 1], doc._id);
			}''')
	rpt_view.sync( db )
	rpt_view = ViewDefinition(
			'list',
			'name_url_last_seen',
			'''function(doc) {
  				emit(doc.presence[doc.presence.length - 1], [doc._id, doc.url_img]);
			}''')
	rpt_view.sync( db )
	rpt_view = ViewDefinition(
			'list',
			'url_img',
			'''function(doc) {
				emit(doc.url_img, doc._id);
			}''')
	rpt_view.sync( db )
	rpt_view = ViewDefinition(
			'list',
			'music_name',
			'''function(doc) {
				emit(doc.music, doc._id);
			}''')
	rpt_view.sync( db )
def create_view_for_house():
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'house_status' )	
	rpt_view = ViewDefinition(
			'list',
			'printer',
			'''function(doc) {
			emit(doc._id, doc);
			}''')
	rpt_view.sync( db )


def retrieve_user_for_mac( mac ):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	
	for row in db.view( "_design/list/_view/macs" ):
		if mac == row.key:
			row_id = row.id
	return row_id

def check_users( address_mac, user_mac, unknown_mac ):
#user_mac is a list of the people already registred in our DB
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )
	for row in db.view( "_design/list/_view/macs" ):
		if address_mac == row.key:
			user_mac.append(address_mac)
			break
		else:
			unknown_mac.append(address_mac)
			break

#Returns a list containing all known MAC addresses
def retrieve_known_macs():
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )
	known_macs = []

	for row in db.view( "_design/list/_view/macs" ):
		known_macs.append( row.key )

	return known_macs
			
def update_last_seen_time( user, time ):
	
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	

	doc = db[ user ]
	try:
		presence = doc['presence']
		if len(presence) < 100:
			presence.append( time )
			doc['presence'] = presence
		else:
			new_presence = []
			for i in range(0, 50):
				new_presence.append( presence[len(presence)-20 + i] )
			new_presence.append( time )
			doc['presence'] = new_presence
	except:
		presence = []
		presence.append( time )
		doc['presence'] = presence
	db.save(doc)
	db.compact()
	
def display_status():
	couch = connect_to_db()
	db = create_or_load_db(couch, 'inhabitants')
	
	all_status=[]
	for row in db.view('_design/list/_view/last_seen'):
		list_user_status =[]
		user = row.id
		presence = row.key
		
		list_user_status.append(user)
		list_user_status.append(presence)
		
		all_status.append(list_user_status)
		
	return all_status

	

def retrieve_time():
	localtime=time.localtime()
	timeString =time.strftime("%Y%m%d%H%M%S",localtime)
	human_time=time.strftime("%Y/%m/%d  %H:%M:%S",localtime)
	return timeString

def internet_on():
    try:
        response=urllib2.urlopen('http://74.125.228.100',timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False

def compare_list(list1, list2):
	list_common_macs=[]
    	for i in range (0,len(list1)):
		for j in range(0, len(list2)):
			if list1[i]==list2[j]:
				list_common_macs.append(list1[i])
	return list_common_macs

def url_img( user, url_img ):
	
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'inhabitants' )	

	doc = db[ user ]
	doc['url_img'] = url_img

	db.save(doc)
	db.compact()


def update_printer_status(printer_status):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'house_status' )	
	try:
		#You can then use the object *db* to directly check a document through its _id, remember that we use urls as ids since a url is unique
		doc = db[ '3dprinter' ]
		doc['printer_status'] = printer_status.get('printer_status')
		doc['bed_temperature'] = printer_status.get('bed_temperature')
		doc['head_temperature'] = printer_status.get('head_temperature')
		doc['job_name'] = printer_status.get('job_name')
		doc['completion'] = printer_status.get('completion')
		doc['elapsed_print_time'] = printer_status.get('elapsed_print_time')
		doc['remaining_print_time'] = printer_status.get('remaining_print_time')
		db.save(doc)
		db.compact()
	except ResourceNotFound:
		dict_field_values = {
			'_id'  : '3dprinter',
			'printer_status' : printer_status.get('printer_status')
		}
		#The object *db* has a create method, and this is how you create a document
		return db.create( dict_field_values )

def update_internet_status(connection_status):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'house_status' )	
	try:
		#You can then use the object *db* to directly check a document through its _id, remember that we use urls as ids since a url is unique
		doc = db[ 'internet' ]
		doc['status'] = connection_status
		db.save(doc)
		db.compact()
	except ResourceNotFound:
		dict_field_values = {
			'_id'  : 'internet',
			'status' : connection_status
		}
		#The object *db* has a create method, and this is how you create a document
		return db.create( dict_field_values )

def update_internet_weather(internet_weather):
	#First you need to connect to CouchDB server
	couch = connect_to_db()
	#Then load a databse in the object *db*
	db = create_or_load_db( couch, 'house_status' )	
	try:
		#You can then use the object *db* to directly check a document through its _id, remember that we use urls as ids since a url is unique
		doc = db[ 'Weather' ]
		doc['temperature'] = internet_weather.get('temperature')
		doc['pressure'] = internet_weather.get('pressure')
		doc['state'] = internet_weather.get('state')
		doc['ID'] = internet_weather.get('ID')
		doc['sunrise'] = internet_weather.get('sunrise')
		doc['sunset'] = internet_weather.get('sunset')
		#print "Type wind:", type(internet_weather.get('wind'))
		doc['wind'] = internet_weather.get('wind')
		
		#doc['status'] = internet_weather
		db.save(doc)
		db.compact()
	except ResourceNotFound:
		dict_field_values = {
			'_id'  : 'Weather',
			
		}
		#The object *db* has a create method, and this is how you create a document
		return db.create( dict_field_values )

def check_last_played_music_time(user):
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )	
	doc = db[ user ]
	last_played_music = doc['last_played_music']
	return last_played_music

def update_last_played_music_time(user):
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )	
	doc = db[ user ]
	doc['last_played_music'] = retrieve_time()
	db.save(doc)
	db.compact()
	return last_played_music

def update_last_arrived_home(user):
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )	
	doc = db[ user ]
	doc['last_arrived_home'] = retrieve_time()
	db.save(doc)
	db.compact()
	return True


def inhabitant_just_arrived( user ):
	couch = connect_to_db()
	db = create_or_load_db( couch, 'inhabitants' )	
	doc = db[ user ]
	presence = doc['presence']
	seconds_since_last_seen = time.mktime(time.localtime()) - time.mktime(time.strptime(presence[len(presence)-1], "%Y%m%d%H%M%S"))
	if seconds_since_last_seen < 30:
		#print seconds_since_last_seen
		seconds_since_last_last_seen = time.mktime(time.localtime())-time.mktime(time.strptime(presence[len(presence)-2], "%Y%m%d%H%M%S"))
		if seconds_since_last_last_seen > 1800 :
			update_last_arrived_home( user )
			print "[inhabitant_just_arrived] Welcome back", user, " !"
			return True
		else:
			return False
	else:
		return False

	
