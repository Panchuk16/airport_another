# routes/auth.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from airport_service.models import db, User
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Search
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):  # Password check
        # Tworzenie tokena JWT
        access_token = create_access_token(identity={'id': user.id, 'username': user.username})
        return jsonify({'access_token': access_token}), 200

    return jsonify({'error': 'Invalid username or password'}), 401


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if exists
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    # Add new
    new_user = User(username=username)
    new_user.set_password(password)  # Password hashing
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201
