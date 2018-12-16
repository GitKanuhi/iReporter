from app.api.v2.user_views import UserRegistration, UserLogin,SingleUser 
from app.api.v2.incident_views import Interventions, DeleteRecord
from app.api.v2.incident_views import Updatecomment, Specific, UpdateLocation
from flask_restful import Api, Resource
from flask import Blueprint

version2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version2)
api.add_resource(UserRegistration, '/auth/signup',strict_slashes=False)
api.add_resource(UserLogin, '/auth/login',strict_slashes=False)
api.add_resource(SingleUser, '/users/<int:id>',strict_slashes=False)

api.add_resource(Interventions, '/interventions',strict_slashes=False)
api.add_resource(DeleteRecord, '/interventions/<int:id>',strict_slashes=False)
api.add_resource(Specific, '/interventions/<int:id>',strict_slashes=False)
api.add_resource(Updatecomment, '/interventions/<int:id>/comment',strict_slashes=False)
api.add_resource(UpdateLocation, '/interventions/<int:id>/location',strict_slashes=False)