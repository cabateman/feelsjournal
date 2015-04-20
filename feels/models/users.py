from feels.models import db, PrimaryIdBaseModel
from sqlalchemy import update

class Users(db.Model, PrimaryIdBaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(256), unique=True)
    num_daily_checkup = db.Column(db.Integer)

    def __init__(self, phone_number=None):
        super(Users, self).__init__()
        self.phone_number = phone_number

    @classmethod
    def get_by_phone_number(cls, pn, session=None):
        try:
            if not session:
                session = db.session
            return session.query(cls).filter_by(phone_number = pn).one()
        except:
            return False
    
    @classmethod
    def create(cls, pn, session=None):
        Users(pn).save()
        try:
            return cls.get_by_phone_number(pn)
        except:
            return False


    @classmethod
    def decrease_daily_checkup(cls, user, session=None):
        num_checkup = user.num_daily_checkup
        if (num_checkup > 1):
            num_checkup -= 1
            if not session:
                session = db.session
            stmt = update(cls).where(cls.id == user.id).values(num_daily_checkup= num_checkup)
            session.execute(stmt)
            session.commit()
        return num_checkup

    @classmethod
    def increase_daily_checkup(cls, user, session=None):
        num_checkup = user.num_daily_checkup
        if (num_checkup < 10):
            num_checkup += 1
            if not session:
                session = db.session
            stmt = update(cls).where(cls.id == user.id).values(num_daily_checkup= num_checkup)
            session.execute(stmt)
            session.commit()
        return num_checkup

    @classmethod
    def stop_daily_checkup(cls, user, session=None):
        num_checkup = user.num_daily_checkup
        if not session:
            session = db.session
        stmt = update(cls).where(cls.id == user.id).values(num_daily_checkup= 0)
        session.execute(stmt)
        session.commit()
        return num_checkup



    def __repr__(self):
        return "<Users(id='{0.id}', phone_number='{0.phone_number}')>".format(self)


