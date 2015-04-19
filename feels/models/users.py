from feels.models import db, PrimaryIdBaseModel

class Users(db.Model, PrimaryIdBaseModel):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(256), unique=True)

    def __init__(self, phone_number=None):
        super(Users, self).__init__()
        self.phone_number = phone_number

    @classmethod
    def get_by_phone_number(cls, pn, session=None):
        if not session:
            session = db.session
        return session.query(cls).filter_by(phone_number = pn).one()
    
    @classmethod
    def create(cls, pn, session=None):
        Users(pn).save()
        if not session:
            session = db.session
        return cls.get_by_phone_number(pn)


    def __repr__(self):
        return "<Users(id='{0.id}', phone_number='{0.phone_number}')>".format(self)


