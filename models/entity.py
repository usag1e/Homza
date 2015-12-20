from db import connector
import logging

logger = logging.getLogger(__name__)

class ArgumentMissingException(Exception):
    def __init__(self, argument, message=''):
        exception_message = 'Argument %s is missing' % argument
        if message is not '':
            exception_message += '\nAdditional message: %s' % message
        logger.error(exception_message)

class Entity(object):
    def get(self):
        instance = connector.get_entity(self)
        return instance

    @classmethod
    def get_all(klass):
        results = connector.get_all_of(klass)
        return results

    @classmethod
    def get_all_in_view(klass, view_name):
        results = connector.get_view(klass, view_name)
        return results

    def create(self):
        connector.save_entity(self)

    def update(self):
        connector.save_entity(self)

    def remove(self):
        connector.remove_entity(self)

    def toCouch(self):
        try:
            return self.__dict__
        except:
            raise NotImplementedError( "This method needs to be implemented for this entity to be saved in CouchDB" )

    def fromCouch(self, couch_self):
        for (key, value) in couch_self.iteritems():
            setattr(self, key, value)
