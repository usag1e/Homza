import _mysql
import sys

# Handler taking care of the operations on the Database

def connectToDB():
    return _mysql.connect('localhost', 'mdepart_user', 'mdepartRaspberry', 'mDepart')
    
def closeDBConnection( connection ):
    if connection:
            connection.close()

def getHomeFromDB():
    pass

def display( result_of_query ):
    print result_of_query

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


executeQueryDB("SELECT VERSION()", display)