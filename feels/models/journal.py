from feels.models import db, PrimaryIdBaseModel

class Journal(db.Model, PrimaryIdBaseModel):
    __tablename__ = 'journal'

    id = db.Column(db.Integer, primary_key=True)
    emotion_id = db.Column(db.Integer)
    emotion = db.Column(db.String(256))
    description = db.Column(db.String(1000))

    def __init__(self, emotion_id=None, emotion=None, description=None):
        super(Journal, self).__init__()
        self.emotion_id = emotion_id
        self.emotion = emotion
        self.description = description

    def __repr__(self):
        return "<Journal(id='{0.id}', emotion='{0.emotion}', description='{0.description}')>".format(self)
