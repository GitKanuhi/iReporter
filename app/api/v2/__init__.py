from app.api.v2.user_views import UserRegistration, UserLogin, AllUsers, SingleUser 
from app.api.v2.incident_views import Interventions, DeleteRecord, Updatecomment, Specific, UpdateLocation

from flask_restful import Api, Resource
from flask import Blueprint

version2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version2)
api.add_resource(UserRegistration, '/auth/signup',strict_slashes=False)
api.add_resource(UserLogin, '/auth/login',strict_slashes=False)
api.add_resource(AllUsers, '/users',strict_slashes=False)
api.add_resource(SingleUser, '/user/<int:id>',strict_slashes=False)

api.add_resource(Interventions, ' /interventions',strict_slashes=False)
api.add_resource(DeleteRecord, '/create/<int:id>',strict_slashes=False)
api.add_resource(Specific, 'interventions/<intervention-id>',strict_slashes=False)
api.add_resource(Updatecomment, '/intervention/<intervention-id>/comment',strict_slashes=False)
api.add_resource(UpdateLocation, ' /interventions/<intervention-id>/location',strict_slashes=False)