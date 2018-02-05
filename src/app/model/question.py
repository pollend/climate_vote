from app import db

import hashlib
from app import app

class Question(db.Model):
    __tablename__ = "question"
    award_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    abstract = db.Column(db.Text)

    def __init__(self,title, abstract,award_id):
        self.title = title
        self.abstract = abstract
        self.award_id = award_id

    def __repr__(self):
        return '<question %r>' % self.id

    def serialize(self):
        return {"title": self.title, "award_id": self.award_id, "abstract": self.abstract}