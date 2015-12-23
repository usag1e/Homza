#!/usr/bin/python
"""
This file contains all the views that are used in couchdb
"""
import logging, os
from couchdb.design import ViewDefinition
from couchdb import Server, ResourceNotFound

logger = logging.getLogger(__name__)

# In this file, we use the python package "couchdb" and not couchdbkit
# The latter doesn't have the same logic for creating the views
COUCHDB_SERVER = os.environ.get('COUCHDB_SERVER')
if not COUCHDB_SERVER:
    COUCHDB_SERVER = 'http://localhost:5984'
COUCHDB_USERNAME = os.environ.get('COUCHDB_USERNAME')
COUCHDB_PASSWORD = os.environ.get('COUCHDB_PASSWORD')

server = Server(COUCHDB_SERVER)
if COUCHDB_USERNAME and COUCHDB_PASSWORD:
    server.resource.credentials = (COUCHDB_USERNAME, COUCHDB_PASSWORD)

# Creates a DB or loads it
def create_or_load_db( couch, database_name ):
    # Try to get the database
    try:
        return couch[ database_name ]
    # Or create it if it is not already
    except ResourceNotFound:
        return couch.create( database_name )

# Initiates the DB by creating the views we are interested in
def initiate_views():
    logger.info("Initiating core CouchDB views")

    db = create_or_load_db(server, 'homza')
    create_views_users(db)

def create_views_users(db):
    rpt_view = ViewDefinition(
        'users',
        'by_name',
        '''function(doc) {
            if(doc.type === 'user')
               emit(doc._id, doc);
        }''')
    rpt_view.sync(db)

initiate_views()

