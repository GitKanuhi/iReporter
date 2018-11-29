
from flask_restful import Api, Resource 
from flask import jsonify,request, make_response
from flask_restful.reqparse import RequestParser
from.models import IncidentModel

incident=IncidentModel()

class IncidentList(Resource):
    def __init__(self):
        self.incident_parser=RequestParser()
        self.incident_parser.add_argument('createdBy',type=str,required=True,help='Name is Required')
        self.incident_parser.add_argument('type',type=str,required=True,help='Type is Required')
        self.incident_parser.add_argument('location',type=str,required=True,help='Location is Required')
        self.incident_parser.add_argument('image',type=str,required=True,help='Image is Required')
        self.incident_parser.add_argument('videos',type=str,required=True,help='Videos is Required')
        self.incident_parser.add_argument('comment',type=str,required=True,help='Comment is Required')
    
    def post(self):

        data=self.incident_parser.parse_args()
        data = request.get_json()
        createdBy=data['createdBy']
        type=data['type']
        location=data ['location']
        image=data['image']
        videos=data['videos']
        comment=data['comment']

        incident.create_incident(createdBy,type,location,image,videos,comment)
        return {
            'message': 'Successfully created incident report'
            }, 201
    def get(self):
        allincidences=incident.all()
        return allincidences

class SpecificIncident(Resource):
    
    def get(self,incidentId):
        try:
            int(incidentId)
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
        redflag=incident.get_specific(incidentId)
        return redflag

    def patch(self,incidentId):
        try:
            int(incidentId)
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
        editlocation=incident.edit_location(incidentId)
        return editlocation
        
    def delete(self,incidentId):
        try:
            int(incidentId)
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
        deleteincident=incident.delete_incident(incidentId)
        return deleteincident



class EditComment(Resource):
    def patch(self,incidentId):
        try:
            int(incidentId)
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
        editcomment=incident.edit_comment(incidentId)
        return editcomment