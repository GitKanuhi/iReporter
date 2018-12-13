from app.api.v2.views import UserRegistration, UserLogin, AllUsers, SingleUser 
from app.api.v2.views import Interventions, DeleteRecord, Updatecomment, Specific

from flask_restful import Api, Resource
from flask import Blueprint

version2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version2)
api.add_resource(UserRegistration, '/auth/register',strict_slashes=False)
api.add_resource(AllUsers, '/users',strict_slashes=False)
api.add_resource(SingleUser, '/user/<int:id>',strict_slashes=False)
api.add_resource(UserLogin, '/auth/login',strict_slashes=False)
api.add_resource(Interventions, '/create',strict_slashes=False)
api.add_resource(DeleteRecord, '/create/<int:id>',strict_slashes=False)
api.add_resource(Specific, '/create/<int:id>',strict_slashes=False)
api.add_resource(Updatecomment, '/create/<int:id>',strict_slashes=False)