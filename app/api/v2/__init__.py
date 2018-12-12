from app.api.v2.views import UserRegistration, UserLogin, AllUsers, SingleUser

from flask_restful import Api, Resource
from flask import Blueprint

version2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version2)
api.add_resource(UserRegistration, '/register',strict_slashes=False)
api.add_resource(AllUsers, '/users',strict_slashes=False)
api.add_resource(SingleUser, '/user/<int:id>',strict_slashes=False)
api.add_resource(UserLogin, '/login',strict_slashes=False)