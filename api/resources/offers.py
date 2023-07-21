from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource, reqparse

from core.models import Offer, Submission
from core.database import db

class OfferResource(Resource):
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('price', type=float, required=False)

        args = parser.parse_args()

        offer = Offer(title=args['title'], description=args['description'], price=args['price'], author_id=current_user.id)

        db.session.add(offer)
        db.session.commit()

        return {"message": "Offer created successfully"}, 201

    def get(self, id=None):
        if id:
            offer = Offer.query.filter_by(id=id).first()
            if not offer:
                return {'message': 'Offer not found'}, 404
            
            return offer.to_dict(), 200
        else:
            offers = Offer.query.all()
            return [offer.to_dict() for offer in offers], 200
    
class SubmissionsResource(Resource):
    @jwt_required()
    def post(self, offer_id):
        offer = Offer.query.filter_by(id=offer_id).first()
        if not offer:
            return {'message': 'Offer not found'}, 404

        if not current_user.freelancer:
            return {'message': 'You need to create freelancer profile first'}, 403

        submission = Submission.query.filter_by(offer_id=offer_id, freelancer_id=current_user.freelancer.id).first()
        if submission is not None:
            return {'message': 'You have already submitted this offer'}, 409

        parser = reqparse.RequestParser()
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('price', type=float, required=False)

        args = parser.parse_args()

        submission = Submission(description=args['description'], price=args['price'], offer_id=offer_id, freelancer_id=current_user.freelancer.id)
        db.session.add(submission)
        db.session.commit()

        return {"message": "Submission created successfully"}, 201