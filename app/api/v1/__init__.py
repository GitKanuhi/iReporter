
from app.api.v1.views import RedflagsList, SpecificRedflag, EditComment, EditLocation, Delete

from flask_restful import Api, Resource
from flask import Blueprint

version1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version1)

api.add_resource(RedflagsList, '/red-flags',strict_slashes=False)
api.add_resource(SpecificRedflag, '/red-flags/<incidentId>',strict_slashes=False)
api.add_resource(EditComment, '/red-flags/<incidentId>/comment',strict_slashes=False)
api.add_resource(EditLocation, '/red-flags/<incidentId>/location',strict_slashes=False)
api.add_resource(Delete, '/red-flags/<incidentId>/',strict_slashes=False)

