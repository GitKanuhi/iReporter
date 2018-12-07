"""Version 1 views"""
from flask_restful import Api, Resource 
from flask import jsonify,request, make_response
from flask_restful.reqparse import RequestParser
from.models import RedflagModel
import re
"""used fo string searching and manipulation"""

incident=RedflagModel()

class RedflagsList(Resource):
    """Class for Red-Flags endpoints"""

    def __init__(self):
        """Initialize Class Resource"""

        self.incident_parser=RequestParser()
        self.incident_parser.add_argument('createdBy',type=str,required=True,help='Name is Required')
        self.incident_parser.add_argument('type',type=str,required=True,help='Type is Required')
        self.incident_parser.add_argument('location',type=str,required=True,help='Location is Required')
        self.incident_parser.add_argument('image',type=str,required=True,help='Image is Required')
        self.incident_parser.add_argument('videos',type=str,required=True,help='Videos is Required')
        self.incident_parser.add_argument('comment',type=str, required=True,help='Comment is Required')
    
    def validate_data(self, data):
        """ data validation"""
        if len(data['comment'].strip()) < 1:
            return "Comment should not be empty"
        elif len(data['location'].strip()) < 1:
            return "Location can not be empty!" 
        elif not re.match('\d.*[A-Z]|[A-Z].*\d', data['location'].strip()):
            """checks for a match only at the beginning of the string"""
            return "location should contain capital letter and a digit"
        return 'valid'

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

        if self.validate_data(data) == 'valid':
            """validation conditions"""
            response=incident.create_redflag(createdBy,recordType,location,image,videos,comment)
            return {
                    'message': 'Successfully created incident report',
                    'data':response
                    }, 201  
        return jsonify({"message": self.validate_data(data)}) 

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
    """Class handling editing of a redflag loaction"""
    def __init__(self):
        self

    def validate_data(self, data):
        if len(data['location'].strip()) < 1:
            return "Location can not be empty!" 
        return 'valid'

    def patch(self,incidentId):
        """PATCH redflag location"""
        try:
            data = request.get_json()
            if self.validate_data(data) == 'valid':
                int(incidentId)
                editlocation=incident.edit_location(int(incidentId))
                return editlocation, 200
            return jsonify({"message":self.validate_data(data)})
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
      
class EditComment(Resource):
    def __init__(self):
        self
        """Initialize Class Resource"""

    def validate_data(self, data):
        if len(data['comment'].strip()) < 1:
            return "Comment should not be empty" 
        return 'valid'

    def patch(self,incidentId):
        try:
            data = request.get_json()
            if self.validate_data(data) == 'valid':
                int(incidentId)
                editcomment=incident.edit_comment(int(incidentId), data)
                return editcomment, 200 
            return jsonify({"message":self.validate_data(data)})
        except ValueError:
            return {
                'status': 404,
                'error':'Please enter a valid Incident ID'
            }
    
class Delete(Resource):
    """ class handling deletion of a redflag by incidentID"""
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