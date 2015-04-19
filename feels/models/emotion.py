from feels.models import db, PrimaryIdBaseModel

class Emotion(db.Model, PrimaryIdBaseModel):
    __tablename__ = 'emotion'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)

    def __init__(self, name=None):
        super(Emotion, self).__init__()
        self.name = name

    @classmethod
    def get_by_name(cls, query_name, session=None):
        if not session:
            session = db.session
        return session.query(cls).filter_by(name = query_name).one()

    def __repr__(self):
        return "<Emotion(id='{0.id}', name='{0.name}')>".format(self)
