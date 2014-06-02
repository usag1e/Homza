from DBhandler import *

connection = connectToDB()
with connection:
	executeOnDB( connection, "UPDATE positions as p JOIN locations as l ON p.id = l.position_id SET p.latitude='45.4967991', p.longitude='-73.6393846' WHERE l.name = 'home' ;" )
closeDBConnection( connection )
