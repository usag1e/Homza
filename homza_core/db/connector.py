#This is the python file containing most of the functions necessary to communicate and manipulate the database
# -*- coding: utf-8 -*-
from couchdbkit import *
from dateutil.relativedelta import *
from dateutil import *
from time import strptime
import calendar, time, json, urllib, os, datetime, hashlib, logging

logger = logging.getLogger(__name__)

# Creates a connection
def connect_to_db():
    COUCHDB_SERVER = os.environ.get('COUCHDB_SERVER')
    if not COUCHDB_SERVER:
        COUCHDB_SERVER = 'http://localhost:5984'
    COUCHDB_USERNAME = os.environ.get('COUCHDB_USERNAME')
    COUCHDB_PASSWORD = os.environ.get('COUCHDB_PASSWORD')

    if COUCHDB_USERNAME and COUCHDB_PASSWORD:
        couch = Server('{}:{}@{}'.format(COUCHDB_USERNAME, COUCHDB_PASSWORD, COUCHDB_SERVER))
    else:
        couch = Server('{}'.format(COUCHDB_SERVER))
    return couch

def get_view(entity, view_name):
    try:
        db = server.get_or_create_db(entity._collection)
        return db.view(view_name)
    except ResourceNotFound:
        logger.debug('View %s of Entity %s doesn\'t exist in %s yet' % (view_name, entity._collection))
        return None

def get_all_of(entity):
    results = []
    db = server.get_or_create_db(entity._collection)
    view_results = get_view(entity, '_all_docs')
    for result in view_results:
        if not '_design' in result['id']:
            doc = db[result['id']]
            if doc['type'] == entity._type:
                results.append(entity(result['id']))
    return results

def get_entity(entity):
    try:
        db = server.get_or_create_db(entity._collection)
        instance = db[entity._id]
        entity.fromCouch(instance)
        return entity
    except AttributeError as e:
        logger.error('Entity has one attribute missing (%s)' % e)
        return None
    except KeyError:
        logger.error('Entity of %s doesn\'t have an id' % entity._collection)
        return None
    except ResourceNotFound:
        logger.debug('Entity %s doesn\'t exist in %s yet' % (entity._id, entity._collection))
        return None

def save_entity(entity):
    db = server.get_or_create_db(entity._collection)
    try:
        if entity._id:
            instance = db[entity._id]
            db.save_doc(entity.toCouch())
    except ResourceNotFound:
        db[entity._id] = entity.toCouch()
    except:
        raise

def remove_entity(entity):
    try:
        db = server.get_or_create_db(entity._collection)
        if entity._id:
            instance = db[entity._id]
            del instance
    except ResourceNotFound:
        logger.info('Entity %s was already deleted from %s' % (entity._id, entity._collection))
    except:
        raise

#                           #
#        Clearing DB        #
#                           #
def clear_db():
    try:
        logger.info('[clear_db] Soft clearing articles')
        del server['articles']
    except ResourceNotFound :
        pass

def hard_clear_db():
    try:
        logger.info('[clear_db] Clearing articles')
        del server['articles']
    except ResourceNotFound :
        pass
#    try:
#        logger.info('[clear_db] Clearing events')
#        del server['events']
#    except ResourceNotFound :
#        pass
    try:
        logger.info('[clear_db] Clearing websites')
        del server['websites']
    except ResourceNotFound :
        pass

server = connect_to_db()
