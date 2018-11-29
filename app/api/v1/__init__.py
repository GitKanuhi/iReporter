
from app.api.v1.views import IncidentList, SpecificIncident, EditComment

from flask_restful import Api, Resource
from flask import Blueprint

version1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

api = Api(version1)

api.add_resource(IncidentList, '/red-flags',strict_slashes=False)
api.add_resource(SpecificIncident, '/red-flags/<string:incidentId>',strict_slashes=False)
api.add_resource(EditComment, '/red-flags/<string:incidentId>/comment',strict_slashes=False)


