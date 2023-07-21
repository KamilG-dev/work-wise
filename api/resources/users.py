from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from core.models import User, Freelancer
from core.database import db

class UserResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_ids', action='split', type=int)
        args = parser.parse_args()
        user_ids = args['user_ids']
        
        if user_ids:
            return User.query.filter(User.id.in_(user_ids)).all()
        else:
            return User.query.all()
        

class FreelancerResource(Resource):
    @jwt_required()
    def post(self, user_id):
        if get_jwt_identity() != user_id: 
            return jsonify({'message': 'Unauthorized access'}), 401
        
        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('skills', type=str, required=True)

        args = parser.parse_args()

        freelancer = Freelancer.query.filter_by(user_id=user_id).first()

        if freelancer is None:
            freelancer = Freelancer(user_id=user_id, description=args['description'],
                                    skills=args['skills'])
            db.session.add(freelancer)
            db.session.commit()
            db.session.refresh(freelancer)

            return {'message': 'Freelancer created'}, 201
        else:
            freelancer.description = args['description']
            freelancer.skills = args['skills']
            db.session.commit()
            db.session.refresh(freelancer)

            return {'message': 'Freelancer updated'}, 200
        
    def get(self, user_id=None):
        if user_id:
            freelancer = Freelancer.query.filter_by(user_id=user_id).first()
            if freelancer is None:
                return {'message': 'Freelancer not found'}, 404
            return freelancer.to_dict(), 200
        else:
            freelancers = Freelancer.query.all()
            
            return [f.to_dict() for f in freelancers], 200
    
    @jwt_required()
    def delete(self, user_id):
        if get_jwt_identity().id!= user_id:
            return jsonify({'message': 'Unauthorized access'}), 401
        
        freelancer = Freelancer.query.filter_by(user_id=user_id).first().delete()
        db.session.commit()

        return {'message': 'Freelancer deleted'}, 200
    
    
