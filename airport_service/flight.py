
from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify
from airport_service.models import Flight

flight_bp = Blueprint('flight', __name__)

@flight_bp.route('/flights', methods=['GET'])
@jwt_required()
def get_flights():
    flights = Flight.query.all()
    return jsonify([{'id': flight.id, 'origin': flight.origin, 'destination': flight.destination} for flight in flights])
