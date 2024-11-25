from flask import Blueprint, render_template, redirect, url_for, Flask, jsonify, request
from airport_service.extensions import db
from airport_service.models import Airport, AirplaneType, Airplane, Flight, FlightLog
from datetime import datetime

main = Blueprint("main", __name__)

# Trasa do pobierania listy lotnisk
@main.route('/airports', methods=['GET'])
def get_airports():
    airports = Airport.query.all()
    return jsonify([{
        'id': airport.id,
        'name': airport.name,
        'city': airport.city,
        'country': airport.country,
        'code': airport.code
    } for airport in airports])

# Trasa do dodawania nowego lotniska
@main.route('/airports', methods=['POST'])
def add_airport():
    data = request.get_json()
    new_airport = Airport(
        name=data['name'],
        city=data['city'],
        country=data['country'],
        code=data['code']
    )
    db.session.add(new_airport)
    db.session.commit()
    return jsonify({'message': 'Airport added successfully'}), 201

# Trasa do pobierania konkretnego lotniska po ID
@main.route('/airports/<int:id>', methods=['GET'])
def get_airport(id):
    airport = Airport.query.get_or_404(id)
    return jsonify({
        'id': airport.id,
        'name': airport.name,
        'city': airport.city,
        'country': airport.country,
        'code': airport.code
    })

#NOWE TRASY:

# AIRPLANE_TYPE
@main.route('/airplane_types', methods=['GET'])
def get_airplane_types():
    airplane_types = AirplaneType.query.all()
    return jsonify([{
        'id': airplane_type.id,
        'model': airplane_type.model,
        'manufacturer': airplane_type.manufacturer,
        'seating_capacity': airplane_type.seating_capacity,
        'range_km': airplane_type.range_km
    } for airplane_type in airplane_types])

@main.route('/airplane_types', methods=['POST'])
def add_airplane_type():
    data = request.get_json()
    new_airplane_type = AirplaneType(
        model=data['model'],
        manufacturer=data['manufacturer'],
        seating_capacity=data['seating_capacity'],
        range_km=data['range_km']
    )
    db.session.add(new_airplane_type)
    db.session.commit()
    return jsonify({'message': 'Airplane type added successfully'}), 201

# AIRPLANE
@main.route('/airplanes', methods=['GET'])
def get_airplanes():
    airplanes = Airplane.query.all()
    return jsonify([{
        'id': airplane.id,
        'registration_number': airplane.registration_number,
        'airplane_type_id': airplane.airplane_type_id,
        'manufacturing_date': airplane.manufacturing_date.strftime('%Y-%m-%d')
    } for airplane in airplanes])

@main.route('/airplanes', methods=['POST'])
def add_airplane():
    data = request.get_json()

    manufacturing_date = datetime.strptime(data['manufacturing_date'], '%Y-%m-%d').date()
    
    new_airplane = Airplane(
        registration_number=data['registration_number'],
        airplane_type_id=data['airplane_type_id'],
        manufacturing_date=manufacturing_date
    )
    db.session.add(new_airplane)
    db.session.commit()
    return jsonify({'message': 'Airplane added successfully'}), 201

@main.route('/airplanes/<int:id>', methods=['GET'])
def get_airplane(id):
    airplane = Airplane.query.get_or_404(id)
    return jsonify({
        'id': airplane.id,
        'registration_number': airplane.registration_number,
        'airplane_type_id': airplane.airplane_type_id,
        'manufacturing_date': airplane.manufacturing_date
    })

# FLIGHT
@main.route('/flights', methods=['GET'])
def get_flights():
    flights = Flight.query.all()
    return jsonify([{
        'id': flight.id,
        'airline_id': flight.airline_id,
        'origin': flight.origin,
        'destination': flight.destination,
        'scheduled_departure': flight.scheduled_departure.strftime('%Y-%m-%d'),
        'scheduled_arrival': flight.scheduled_arrival.strftime('%Y-%m-%d')
    } for flight in flights])

@main.route('/flights', methods=['POST'])
def add_flight():
    data = request.get_json()
    scheduled_departure = datetime.strptime(data['scheduled_departure'], '%Y-%m-%d').date()
    scheduled_arrival = datetime.strptime(data['scheduled_arrival'], '%Y-%m-%d').date()
    
    new_flight = Flight(
        airline_id=data['airline_id'],
        origin=data['origin'],
        destination=data['destination'],
        scheduled_departure=scheduled_departure,
        scheduled_arrival=scheduled_arrival
    )
    db.session.add(new_flight)
    db.session.commit()
    return jsonify({'message': 'Flight added successfully'}), 201

# FLIGHT_LOG
@main.route('/flight_logs', methods=['POST'])
def add_flight_log():
    data = request.get_json()
    departure_time = datetime.strptime(data['departure_time'], '%Y-%m-%d %H:%M:%S')
    arrival_time = datetime.strptime(data['arrival_time'], '%Y-%m-%d %H:%M:%S')
    
    new_flight_log = FlightLog(
        flight_id=data['flight_id'],
        airplane_id=data['airplane_id'],
        departure_time=departure_time,
        arrival_time=arrival_time,
        status=data['status']
    )
    db.session.add(new_flight_log)
    db.session.commit()
    return jsonify({'message': 'Flight log added successfully'}), 201


@main.route('/flight_logs', methods=['GET'])
def get_flight_logs():
    flight_logs = FlightLog.query.all()
    return jsonify([{
        'id': flight_log.id,
        'flight_id': flight_log.flight_id,
        'airplane_id': flight_log.airplane_id,
        'departure_time': flight_log.departure_time.strftime('%Y-%m-%d %H:%M:%S'),
        'arrival_time': flight_log.arrival_time.strftime('%Y-%m-%d %H:%M:%S'),
        'status': flight_log.status
    } for flight_log in flight_logs])