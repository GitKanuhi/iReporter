"""Version 1 views"""
from flask_restful import Api, Resource 
from flask import jsonify,request, make_response
from flask_restful.reqparse import RequestParser
from.models import RedflagModel

incident=RedflagModel()

class RedflagsList(Resource):
    """Class for Red-Flags endpoints"""
    def __init__(self):
        self.incident_parser=RequestParser()
        self.incident_parser.add_argument('createdBy',type=str,required=True,help='Name is Required')
        self.incident_parser.add_argument('type',type=str,required=True,help='Type is Required')
        self.incident_parser.add_argument('location',type=str,required=True,help='Location is Required')
        self.incident_parser.add_argument('image',type=str,required=True,help='Image is Required')
        self.incident_parser.add_argument('videos',type=str,required=True,help='Videos is Required')
        self.incident_parser.add_argument('comment',type=str,required=True,help='Comment is Required')
    
    def post(self):
        """Create Red-Flag endpoint"""

        data=self.incident_parser.parse_args()
        data = request.get_json()
        createdBy=data['createdBy']
        recordType=data['type']
        location=data ['location']
        image=data['image']
        videos=data['videos']
        comment=data['comment']

        response=incident.create_redflag(createdBy,recordType,location,image,videos,comment)

        return {
            'message': 'Successfully created incident report',
            'data':response
            }, 201
            
    def get(self):
        """Get all Redflags"""
        resp = incident.view_all()
        if resp:
            return make_response(jsonify({
                "status":200,
                "message": "all redflags available",
                "all incidents": resp
            }), 200)
        return make_response(jsonify({"message": "No redflag found"}), 200)

class SpecificRedflag(Resource):
    """Specific Redflag endpoints"""

    def get(self,incidentId):
        """GET specific redflag"""
        try:
            int(incidentId)
            redflag=incident.get_specific(int(incidentId))
            return redflag, 200
        except ValueError:
            return {
                'status': 404,
                "message": "error, Redflag not Found! Please enter a valid Incident ID"
            }
        
class EditLocation(Resource):
    def patch(self,incidentId):
        """PATCH redflag location"""
        try:
            int(incidentId)
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
        editlocation=incident.edit_location(int(incidentId))
        return editlocation, 200
      
class EditComment(Resource):
    def patch(self,incidentId):
        try:
            int(incidentId)
            editcomment=incident.edit_comment(int(incidentId))
            return editcomment, 200
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
    
class Delete(Resource):

    def delete(self,incidentId):
        
        try:
            int(incidentId)
            deleteredflag=incident.delete_incident(int(incidentId))
            return deleteredflag, 200
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid redflag ID for deletion'
            }