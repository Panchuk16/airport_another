# models.py

from .extensions import db
from .users import User

#AIRPORTS
class Airport(db.Model):
    __tablename__ = 'airports'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<Airport {self.name}>'

#AIRPLANE_TYPE
class AirplaneType(db.Model):
    __tablename__ = 'airplane_type'
    
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    seating_capacity = db.Column(db.Integer, nullable=False)
    range_km = db.Column(db.Integer, nullable=False)
    
    
    def __repr__(self):
        return f'<AirplaneType {self.model}, Manufacturer: {self.manufacturer}, Seating Capacity: {self.seating_capacity}>>'
    

#AIRPLANE
class Airplane(db.Model):
    __tablename__ = 'airplanes'
    
    id = db.Column(db.Integer, primary_key=True)
    registration_number = db.Column(db.String(10), unique=True, nullable=False)
    airplane_type_id = db.Column(db.Integer, db.ForeignKey('airplane_type.id'), nullable=False)
    manufacturing_date = db.Column(db.Date, nullable=False)
    
    airplane_type = db.relationship('AirplaneType', backref=db.backref('airplanes', lazy=True))

    def __repr__(self):
        return f'<Airplane {self.registration_number}>'
    
#AIRLINE
class Airline(db.Model):
    __tablename__ = 'airlines'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'<Airline {self.name}>'

#EMPLOYEE
class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    airline_id = db.Column(db.Integer, db.ForeignKey('airlines.id'), nullable=False)
    hire_date = db.Column(db.Date, nullable=False)
    
    airline = db.relationship('Airline', backref=db.backref('employees', lazy=True))

    def __repr__(self):
        return f'<Employee {self.name}>'

#FLIGHT
class Flight(db.Model):
    __tablename__ = 'flights'
    
    id = db.Column(db.Integer, primary_key=True)
    airline_id = db.Column(db.Integer, db.ForeignKey('airlines.id'), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    scheduled_departure = db.Column(db.DateTime, nullable=False)
    scheduled_arrival = db.Column(db.DateTime, nullable=False)
    
    airline = db.relationship('Airline', backref=db.backref('flights', lazy=True))

    def __repr__(self):
        return f'<Flight {self.id}: from {self.origin} to {self.destination}.>'

#FLIGHT_LOG
class FlightLog(db.Model):
    __tablename__ = 'flight_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)
    airplane_id = db.Column(db.Integer, db.ForeignKey('airplanes.id'), nullable=False)
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    
    flight = db.relationship('Flight', backref=db.backref('flight_logs', lazy=True))
    airplane = db.relationship('Airplane', backref=db.backref('flight_logs', lazy=True))
     
    def __repr__(self):
        return f'<FlightLog {self.flight.origin} -> {self.flight.destination}, ' \
               f'Status: {self.status}, Departure: {self.departure_time}, Arrival: {self.arrival_time}>'
