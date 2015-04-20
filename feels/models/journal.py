from feels.models import db, PrimaryIdBaseModel
from sqlalchemy import update

class Journal(db.Model, PrimaryIdBaseModel):
    __tablename__ = 'journal'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    emotion_id = db.Column(db.Integer)
    description = db.Column(db.String(1000))

    def __init__(self, user_id=None, emotion_id=None, description=None):
        super(Journal, self).__init__()
        self.user_id = user_id
        self.emotion_id = emotion_id
        self.description = description

    @classmethod
    def get_previous_journal(cls, user, session=None):
        try:
            if not session:
                session = db.session
            return session.query(cls).filter_by(user_id = user.id).order_by(cls.time_created.desc()).first()
        except:
            return False


    @classmethod
    def add_description(cls, journal, new_description, session=None):
        if not session:
            session = db.session
        stmt = update(cls).where(cls.id == journal.id).values(description= new_description)
        session.execute(stmt)
        session.commit()
        return new_description


    @classmethod
    def create(cls, user, emotion_id, session=None):
        Journal(user.id, emotion_id).save()
        try:
            return cls.get_previous_journal(user)
        except:
            return False

        

    def __repr__(self):
        return "<Journal(id='{0.id}', emotion_id='{0.emotion_id}', description='{0.description}')>".format(self)
