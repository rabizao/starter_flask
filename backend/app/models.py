from app import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
