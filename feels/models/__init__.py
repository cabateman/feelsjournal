import datetime
import logging
import sys

import sqlalchemy

from feels import db

class BaseModel(object):
    """
    @purpose:
        BaseModel class handles the lowest level model ORM layer,
        including caching.
    """
    time_created = db.Column(db.DateTime(), default=datetime.datetime.now())

    _hash_columns = ['id']
    _base_db_columns = ['time_created']
    _db_columns = []

    def __init__(self):
        self.time_created = datetime.datetime.now()
        
    @classmethod
    def get_all(cls, session=None):
        if not session:
            session = db.session
        return session.query(cls).all()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception, e:
            db.session.rollback()
            raise e

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception, e:
            db.session.rollback()
            raise e


class PrimaryIdBaseModel(BaseModel):
    """This class is used for tables that have a primary key id field.
    """
    @classmethod
    def get_all_ids(cls, session=None):
        """
        @type   session:    session
        @param  session:    The database session
        @rtype:             list
        @return:            The list of all ids in the database.
        """
        if not session:
            session = db.session
        results = session.query(cls.id).all()

        return [identification for (identification, ) in results]

    @classmethod
    def get_by_id(cls, id, session=None):
        if not session:
            session = db.session
        return session.query(cls).get(id)

    @classmethod
    def get_by_id(cls, id, session=None):
        if not session:
            session = db.session
        return session.query(cls).get(id)



from feels.models.emotion import Emotion
from feels.models.journal import Journal
from feels.models.users import Users
