# app.py
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from sqlalchemy_utils.functions import create_database, database_exists

from config import Config

from resources.auth import UserLogin, UserRegister
from resources.users import UserResource, FreelancerResource
from resources.offers import OfferResource, SubmissionsResource
from resources.image import ImageResource, UserImagesResource

from core.database import db
from core.jwt_manager import jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    with app.app_context():
        if not database_exists(db.engine.url):
            create_database(db.engine.url)
        db.create_all()
    
    jwt.init_app(app)

    api = Api(app)
    api.add_resource(UserLogin, '/login', '/login/<int:user_id>')
    api.add_resource(UserRegister, '/register') 
    api.add_resource(UserResource, '/user')
    api.add_resource(FreelancerResource, '/freelancer', '/freelancer/<int:user_id>')
    api.add_resource(OfferResource, '/offer', '/offer/<int:id>')
    api.add_resource(SubmissionsResource, '/submission/<int:offer_id>')
    api.add_resource(ImageResource, '/image', '/image/<int:image_id>')
    api.add_resource(UserImagesResource, '/user/<int:user_id>/images' )


    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        return response
    
    CORS(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
