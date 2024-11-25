# models.py

from .extensions import db

class FlightLog(db.Model):
    __tablename__ = 'flight_logs_flight_log_service'

    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, nullable=False)
    airplane_id = db.Column(db.Integer, nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<FlightLog id={self.id}, status={self.status}>'
