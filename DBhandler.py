import _mysql
import sys

# Handler taking care of the operations on the Database

def connectToDB():
    return _mysql.connect('localhost', 'mdepart_user', 'mdepartRaspberry', 'mDepart')
    
def closeDBConnection( connection ):
    if connection:
            connection.close()

def getHomeFromDB():
    position = Position()
    position.latitude = executeQueryDB("SELECT positions.latitude FROM locations JOIN positions ON locations.position_id=positions.id WHERE locations.name = 'home';", display )
    position.longitude = executeQueryDB("SELECT positions.longitude FROM locations JOIN positions ON locations.position_id=positions.id WHERE locations.name = 'home';", display )
    return position

def display( result_of_query ):
    print result_of_query.fetch_row()[0]

def executeQueryDB( query, treatment_function ):
    try:
        connection = connectToDB()
        
        connection.query( query )
        
        result = connection.use_result()
        treatment_function( result )
        # print "MySQL version: %s" % result.fetch_row()[0]

    except _mysql.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        closeDBConnection( connection )

positionHome = getHomeFromDB()
print "Home is %.2f, %.2f"%(positionHome.latitude, positionHome.longitude)
