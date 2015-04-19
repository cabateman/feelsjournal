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
    def get_id_by_filter(cls, filter_name, filter_value):
        id = None
        try:
            id = mc.get(hashlib.md5(filter_value).hexdigest())
        except:
            pass
        if id is not None:
            return id
        else:
            try:
                qry = db.session.query(cls.id).filter(getattr(cls, filter_name).like("%%%s%%" % filter_value)).limit(1)
                id, = qry.one()
                mc.set(hashlib.md5(filter_value).hexdigest(), id)
                return id
            except sqlalchemy.orm.exc.NoResultFound:
                logging.info("no result found for value: {}".format(filter_value))
                return None



#from metricboard.models.os_version import OsVersion
