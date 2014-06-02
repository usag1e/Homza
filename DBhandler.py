import MySQLdb as mdb
import sys
from position import Position
# Handler taking care of the operations on the Database

def connectToDB():
    return mdb.connect('localhost', 'mdepart_user', 'mdepartRaspberry', 'mDepart')
    
def closeDBConnection( connection ):
    if connection:
	connection.close()

def executeOnDB(connection, query ):
    try:
        cursor = connection.cursor(mdb.cursors.DictCursor)
        print( "[DB] %s" % query )
        cursor.execute( query )
    
        rows = cursor.fetchall()
    
        if len( rows ) == 0:
            return None
        elif len( rows ) == 1:
            print "[DB] %s" % rows
            return rows[0]
        else:
            print "[DB] %s" % rows
            return rows
    
    except mdb.Error, e:
        print "[Error] %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    
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
    position.lat = tuple[ "latitude" ]
    position.lon = tuple[ "longitude" ]
    return position

def getHomeFromDB():
    connection = connectToDB()
    with connection:
	 position = translateToPosition( executeOnDB( connection, "SELECT positions.latitude, positions.longitude FROM locations JOIN positions ON locations.position_id=positions.id WHERE locations.name = 'home';" ) )
    closeDBConnection( connection )
    return position

def insertIss( Date, Duration ):
    connection = connectToDB()
    with connection:
	executeOnDB( connection, "INSERT IGNORE INTO iss ( timestamp, date, duration ) VALUES ( NOW(), FROM_UNIXTIME( %s ), '%s' );" % ( Date, Duration ) );
    closeDBConnection( connection )

def getIssDateFromDB():
    connection = connectToDB()
    with connection:
	issInfo = executeOnDB( connection, "SELECT date FROM iss WHERE date < NOW() ORDER BY date DESC LIMIT 1;" );
    closeDBConnection( connection )
    return issInfo

def getIssDurationFromDB( date ):
    connection = connectToDB()
    with connection:
	issInfo = executeOnDB( connection, "SELECT duration FROM iss WHERE date = 'FROM_UNIXTIME( %s )' ORDER BY timestamp DESC LIMIT 1;" % date );
    closeDBConnection( connection )
    return issInfo

def insertTransport( line, direction, time, location_id ):
    connection = connectToDB()
    with connection:
	executeOnDB( connection, "INSERT INTO transportation ( timestamp, line, direction, time_of_arrival, location_id ) VALUES ( NOW(), %s, %s, %s, %d );" % ( line, direction, time, location_id ) )
    closeDBConnection( connection )

def insertInternet( trueOrFalse ):
    connection = connectToDB()
    with connection:
	if trueOrFalse == True:
	    executeOnDB( connection, "INSERT INTO internet (timestamp, connected ) VALUES (NOW(), 1);" )
	else:
	    executeOnDB( connection, "INSERT INTO internet (timestamp, connected ) VALUES (NOW(), 0);" )
    closeDBConnection( connection )

def addLocationByPosition( name, lat, lon, is_transportation ):
    connection = connectToDB()
    with connection:
	executeOnDB( connection, "INSERT IGNORE INTO positions (latitude, longitude) VALUES ('%s', '%s');" % ( lat, lon ) )
	tuple = executeOnDB( connection, "SELECT id FROM positions WHERE latitude = '%s' AND longitude = '%s';" % ( lat, lon ) )
	print tuple
	id = tuple[ 'id' ]
	print id
	executeOnDB( connection, "INSERT INTO locations (name, position_id, is_transportation_stop) VALUES ('%s', %d, '%s');" % (name, id, is_transportation) )
    closeDBConnection( connection )

def getTemperatureFromDB():
    connection = connectToDB()
    with connection:
	temp = executeOnDB( connection, "SELECT temp FROM weather ORDER BY timestamp ASC LIMIT 1;" )
    closeDBConnection( connection )
    return temp

def insertWeather( id_station, name_station, clouds, time, humidity, pressure, temp, temp_max, temp_min, rainPerHour, sunrise, sunset, weather, description, icon, wind_deg, wind_speed ):
    connection = connectToDB()
    with connection:
	executeOnDB( connection, "INSERT INTO weather ( timestamp, id_station, name_station, clouds, time, humidity, pressure, temp, temp_max, temp_min, rain, sunrise, sunset, weather, description, icon, wind_deg, wind_speed ) VALUES ( NOW(), '%s', '%s', '%s', FROM_UNIXTIME( '%s' ), '%s', '%s', '%s', '%s', '%s', '%s', FROM_UNIXTIME( '%s' ), FROM_UNIXTIME( '%s' ), '%s', '%s', '%s', '%s', '%s' );" % ( id_station, name_station, clouds, time, humidity, pressure, temp, temp_max, temp_min, rainPerHour, sunrise, sunset, weather, description, icon, wind_deg, wind_speed ) )
    closeDBConnection( connection )
    

