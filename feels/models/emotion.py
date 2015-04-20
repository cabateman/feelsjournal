from feels.models import db, PrimaryIdBaseModel
from sqlalchemy import select, func, cast
from sqlalchemy.dialects.postgresql import TEXT

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


    @classmethod
    def get_id_by_search_terms(cls,search_emotion, session = None):
        rank = func.similarity(cast(cls.name,TEXT), search_emotion)
        qry = select([cls.id, rank]).order_by(rank.desc()).limit(1)
        if not session:
            session = db.session
            results = session.execute(qry)
            for row in results:
                id, rank = row
                if rank > 0.4:
                    return id
        return False

  
    @classmethod
    def get_all_csv(cls, session = None):
        if not session:
            session = db.session
        results = session.query(cls).all()
        emotions = []
        for result in results:
            emotions.append(result.name)
        return ",".join(emotions)


    @classmethod
    def create(cls, name, session=None):
        Emotion(name).save()
        try:
            return cls.get_by_name(name)
        except:
            return False


    def __repr__(self):
        return "<Emotion(id='{0.id}', name='{0.name}')>".format(self)
