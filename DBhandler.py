import MySQLdb as mdb
import sys
from position import Position
# Handler taking care of the operations on the Database

def connectToDB():
    return mdb.connect('localhost', 'mdepart_user', 'mdepartRaspberry', 'mDepart')
    
def closeDBConnection( connection ):
    if connection:
            connection.close()

def executeOnDB( query ):
    try:
        connection = connectToDB()
        
	cursor = connection.cursor(mdb.cursors.DictCursor)
	cursor.execute( query )

	rows = cursor.fetchall()

    except _mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        closeDBConnection( connection )
	if len( rows ) > 1:
	    return rows 
	else:
	    return rows[0]

def display( result_of_query ):
    if type( result_of_query ) is list:
	print len( result_of_query )+" results in query"
	for result in result_of_query:
	    print result
    else:
	print result_of_query

# Treatment functions
def translateToPosition( tuple ):
    position = Position()
    position.lat = tuple["latitude"]
    position.lon = tuple["longitude"]
    return position

def getHomeFromDB():
    return translateToPosition( executeOnDB( "SELECT positions.latitude, positions.longitude FROM locations JOIN positions ON locations.position_id=positions.id WHERE locations.name = 'home';" ) )

