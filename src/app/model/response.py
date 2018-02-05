from app import db

import hashlib
from app import app


class Response(db.Model):
    __tablename__ = "response"
    id = db.Column(db.Integer, primary_key=True)
    award_id = db.Column(db.Integer)
    ip = db.Column(db.String(64))
    email = db.Column(db.String(64))
    score = db.Column(db.Float)

    def __init__(self,ip,award_id,email,score):
        self.email =email
        self.score = score
        self.ip = ip
        self.award_id = award_id
