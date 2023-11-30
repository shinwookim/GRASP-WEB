from app.extensions import db
from datetime import datetime

class Result(db.Model):
    id = db.Column(db.Integer, primary_key = True) # Primary key for the result
    filename = db.Column(db.String(64), index = True, unique = True) # Filename of the result
    result = db.Column(db.String(120)) # Result of the experiment
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow) # Timestamp of the result

    def __repr__(self):
        return "<Result {}>".format(self.result)