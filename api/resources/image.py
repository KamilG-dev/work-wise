import datetime
import os
from flask import request, send_file
from flask_jwt_extended import current_user, jwt_required
from flask_restful import Resource, reqparse
import werkzeug
import uuid

from core.models import Image
from core.database import db

class ImageResource(Resource):
    def __init__(self) -> None:
        UPLOAD_FOLDER = 'uploads'
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
            
    def get(self, image_id=None):
        if image_id is None:
            return send_file(f'uploads/default.png', mimetype='image/jpeg')

        image = Image.query.filter_by(id=image_id).first()
        if not image:
            return {'message': 'Image not found'}, 404
        
        return send_file(f'uploads/{image.path}', mimetype='image/jpeg')

    @jwt_required()
    def post(self):
        if 'file' not in request.files:
            return {'message': 'No file part in the request'}, 400

        image_file = request.files['file']
        
        name = f'{current_user.id}-{uuid.uuid4()}.jpg'

        image_file.save(f'uploads/{name}')
        image = Image(path=name, user_id=current_user.id)
        db.session.add(image)
        db.session.commit()
        
        return {'message': 'Image uploaded'}, 201
    
    @jwt_required()
    def delete(self, image_id):
        image = Image.query.filter_by(id=image_id).first()

        if image.user_id != current_user.id:
            return {'message': 'Unauthorized'}, 401
        
        if not image:
            return {'message': 'Image not found'}, 404
        
        os.remove(f'uploads/{image.path}')
        
        db.session.delete(image)
        db.session.commit()

class UserImagesResource(Resource):
    @jwt_required()
    def get(self, user_id):
        if current_user.id != user_id:
            return {'message': 'Unauthorized'}, 401
        
        images = Image.query.filter_by(user_id=user_id).all()

        return [image.to_dict() for image in images], 200