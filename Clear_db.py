from couchdb_handler import *


def clear_db():
	couch = connect_to_db()
	try:
		print '[clear_db] clearing inhabitants DB'
		del couch['inhabitants']
	except ResourceNotFound :
		print 'inhabitants not found'
		pass
	try:
		print '[clear_db] clearing house_status DB'
		del couch['house_status']
	except ResourceNotFound :
		print 'house_status not found'
		pass

clear_db()