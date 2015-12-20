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

    db_websites = create_or_load_db(server, 'websites')
    create_views_in_db_websites(db_websites)

    db_articles = create_or_load_db(server, 'articles')
    create_views_in_db_articles(db_articles)

    db_events = create_or_load_db(server, 'events')
    create_views_in_db_events(db_events)

def create_views_in_db_websites(db):
    rpt_view = ViewDefinition(
        'list',
        'websites_list_by_rss_url',
        '''function(doc) {
            emit(doc._id, [doc.name, doc.url, doc.icon, doc.hash]);
        }''')
    rpt_view.sync(db)
    rpt_view2 = ViewDefinition(
        'list',
        'by_url',
        '''function(doc) {
               emit(doc.url, doc);
        }''')
    rpt_view2.sync(db)

def create_views_in_db_articles(db):
    create_views_in_db_articles_general(db)
    create_views_in_db_articles_for_words(db)

# Defines and adds the views used in all the projects
def create_views_in_db_articles_general(db):
    rpt_view3 = ViewDefinition(
            'list',
            'articles_list_by_date',
            '''function(doc) {
    emit(doc.date, doc);
}''')
    rpt_view3.sync(db)

    rpt_view3_5 = ViewDefinition(
            'list',
            'articles_list_by_date_and_origin',
            '''function(doc) {
    emit([doc.origin, doc.date], [doc._id, doc.origin, doc.title, doc.author, doc.category]);
}''')
    rpt_view3_5.sync(db)
    
    rpt_view = ViewDefinition(
            'php',
            'picarticles_bydate',
            '''function(doc) {
         if(doc.image != null){
        for(i in doc.words){
                     emit([i, doc.date], [doc._id, doc.image, doc. title, doc.origin, doc.author]);
        }
    }
}''')
    rpt_view.sync(db)
    
def create_views_in_db_events(db_events):
    rpt_view = ViewDefinition(
        'clusters',
        'bundles',
        '''function( doc ) {
    var words = doc.common_words;
    emit( words, doc );
}''')
    rpt_view.sync( db_events )
    
    rpt_view = ViewDefinition(
        'single',
        'words',
        '''function( doc ) {
    var words=doc.common_words;
    for( word in words ){
         emit( [words[word], doc._id], doc );
    }
}''')
    rpt_view.sync( db_events )
    
    rpt_view = ViewDefinition(
            'list',
            'events_list_by_date',
            '''function( doc ) {
    emit( doc._id, doc );
}''')
    rpt_view.sync( db_events )

def create_views_in_db_articles_for_words( db ):
    #You can also create views with a mapping function which is going to perform some basic operation on your data before sending it back
    #rpt_view = ViewDefinition(
        #'words',
        #'words_list_occurences',
        #'''function( doc ) {
    #var words=doc.words;
    #for( word in words ){
        #var occurences = words[ word ];
            #emit( word, occurences );
    #}
#}''', '''function(keys, values, rereduce) {
    #if (rereduce) {
        #return sum(values);
    #} else {
        #return values.length;
        #}
    #}''' )
        #rpt_view.sync( db )

    rpt_view3 = ViewDefinition(
        'words',
        'most_used_words',
        '''function( doc ) {
    var words=doc.words;
    for( word in words ){
        var occurences = words[ word ];
        emit( [occurences, word], doc._id );
    }
}''')
    rpt_view3.sync( db )

    rpt_view4 = ViewDefinition(
        'words',
        'words_by_date',
        '''function( doc ) {
    var words=doc.words;
    for( word in words ){
        var occurences = words[ word ];
        emit( [word, doc.date], occurences, doc._id );
    }
}''')
    rpt_view4.sync( db )

    rpt_view5 = ViewDefinition(
        'words',
        'words_vs_all',
        '''function( doc ) {
    var words=doc.words;
    for( word in words ){
        var occurences = words[ word ];
        emit( doc.date, [ word, occurences, doc._id, doc.title, doc.author, doc.origin ] );
    }
}''')
    rpt_view5.sync( db )

    rpt_view6 = ViewDefinition(
        'words',
        'all_occurrences',
        '''function( doc ) {
    var words=doc.words;
    for( word in words ){
        var occurences = words[ word ];
        emit( word, occurences );
    }
}''',
    reduce_fun = '''function(keys, values, rereduce) {
    return sum(values);
}''')
    rpt_view6.sync( db )

    rpt_view7 = ViewDefinition(
        'words',
        'word_by_article',
        '''function( doc ) {
    var words=doc.words;
    for( word in words ){
        var occurences = words[ word ];
         emit( word, [ doc._id, doc.title, doc.author ] );
    }
}''')
    rpt_view7.sync( db )

    rpt_view8 = ViewDefinition(
        'words',
        'unread_articles_by_category',
        '''function( doc ) {
    if( doc.is_treated == false || doc.is_treated == False )
        emit( doc.category, doc );
}''')
    rpt_view8.sync( db )

    rpt_view9 = ViewDefinition(
        'words',
        'unread_articles',
        '''function( doc ) {
    if( doc.is_treated == false || doc.is_treated == False )
        emit( doc._id, doc );
}''')
    rpt_view9.sync( db )

    rpt_view10 = ViewDefinition(
        'words',
        'all_occurrences2',
        '''function( doc ) {
    var words=doc.words;
    for( word in words ){
         emit( [word, doc.date], doc.title  );
    }
}''')
    rpt_view10.sync( db )
