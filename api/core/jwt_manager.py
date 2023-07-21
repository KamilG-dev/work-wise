from flask_jwt_extended import JWTManager

from core.models import User
from core.redis import redis_client

jwt = JWTManager()

@jwt.user_identity_loader
def user_identity_loader(user: User):
    return user.id

@jwt.user_lookup_loader
def user_lookup_loader(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).one_or_none()

@jwt.token_in_blocklist_loader
def check_if_token_in_blocklist(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    return redis_client.token_blocked(jti)