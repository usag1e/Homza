from DBhandler import *

connection = connectToDB()
with connection:
	executeOnDB( connection, "UPDATE positions as p JOIN locations as l ON p.id = l.position_id SET p.latitude='48.8588384', p.longitude='2.2169790000000376' WHERE l.name = 'home' ;" )
closeDBConnection( connection )
