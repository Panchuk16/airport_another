from flask import Blueprint, render_template, redirect, url_for, Flask, jsonify, request
from flight_log_service.extensions import db
from flight_log_service.models import FlightLog
from datetime import datetime

main = Blueprint("main", __name__)


@main.route('/flight_logs', methods=['POST'])
def add_flight_log():
    data = request.get_json()
    new_log = FlightLog(
        flight_id=data['flight_id'],
        airplane_id=data['airplane_id'],
        departure_time=data['departure_time'],
        arrival_time=data['arrival_time'],
        status=data['status']
    )
    db.session.add(new_log)
    db.session.commit()
    return jsonify({'message': 'Log added successfully'}), 201


@main.route('/flight_logs', methods=['GET'])
def get_flight_logs():
    logs = FlightLog.query.all()
    return jsonify([
        {
            'id': log.id,
            'flight_id': log.flight_id,
            'airplane_id': log.airplane_id,
            'departure_time': log.departure_time.isoformat(),
            'arrival_time': log.arrival_time.isoformat(),
            'status': log.status
        }
        for log in logs
    ])


@main.route('/flight_logs/<int:id>', methods=['GET'])
def get_flight_log(id):
    log = FlightLog.query.get_or_404(id)
    return jsonify({
        'id': log.id,
        'flight_id': log.flight_id,
        'airplane_id': log.airplane_id,
        'departure_time': log.departure_time.isoformat(),
        'arrival_time': log.arrival_time.isoformat(),
        'status': log.status
    })


@main.route('/flight_logs/<int:id>', methods=['DELETE'])
def delete_flight_log(id):
    log = FlightLog.query.get_or_404(id)
    db.session.delete(log)
    db.session.commit()
    return jsonify({'message': 'Log deleted successfully'})
