from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, get_jwt, jwt_required, current_user

import bcrypt

from core.models import User
from core.database import db
from core.redis import redis_client

class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        special_chars = '!@#$%^&*()-=_+[]{}|;:,.<>?`~'
        for char in special_chars:
            if char in args['username']:
                return {'message': 'Username contains disallowed characters'}, 400

        # Check if the username or email already exists in the database
        existing_user = User.query.filter(
            (User.username == args['username']) | (User.email == args['email'])
        ).first()
        if existing_user:
            return {'message': 'Username or email already exists'}, 400

        # Create a new user and save it to the database
        hashed_password = bcrypt.hashpw(args['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(
            username=args['username'],
            email=args['email'],
            password_hash=hashed_password.decode('utf-8'),
            display_name=args['username']
        )
        db.session.add(user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201

class UserLogin(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('login', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        # Check if the username exists in the database
        user = User.query.filter(
            (User.username == args['login']) | (User.email == args['login'])
        ).first()
        if not user:
            return {'message': 'Invalid login or password'}, 401

        # Check if the password is correct
        if not bcrypt.checkpw(args['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
            return {'message': 'Invalid username or password'}, 401

        # Generate an access token for the user
        access_token = create_access_token(identity=user)

        return {'access_token': access_token, 'user': user.to_dict() }, 200
    
    @jwt_required()
    def delete(self, user_id):
        print(user_id)
        print(current_user.id)
        if current_user.id != user_id:
            return {'message': 'You are not authorized to log out this user'}, 401
        jti = get_jwt()['jti']
        redis_client.block_token(jti)
        return {'message': 'User logged out successfully'}, 200