"""Version 1 views"""
from flask_restful import Api, Resource 
from flask import jsonify,request, make_response
from flask_restful.reqparse import RequestParser
from.models import RedflagModel, UserModel

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

        incident.create_redflag(createdBy,recordType,location,image,videos,comment)
        return {
            'message': 'Successfully created incident report'
            }, 201
            
    def get(self):
        allredflags=incident.all()
        return allredflags

class SpecificRedflag(Resource):
    """Specific Redflag endpoints"""

    def get(self,incidentId):
        """GET specific redflag"""
        try:
            int(incidentId)
        except ValueError:
            return {
                'status': 404,
                'message':'error, Please enter a valid Incident ID'
            }
        redflag=incident.get_specific(incidentId)

        return redflag

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
        editlocation=incident.edit_location(incidentId)
        return editlocation

class Delete(Resource):

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

class User(Resource):
    """Class for single user operations"""
    def __init__(self):
        self.db = UserModel()
    
    def notFound(self):
        return{
            'message':'Record not Found!',
            'status':404
        }
    
    def get(self, user_id):
        user=self.db.find(user_id)

        if not user:
            return self.notFound()

        return user, 200

class Users(Resource):
    """class for users"""
    def __init__(self):
        self.db=UserModel()

    def get(self):
        """GET users"""
        return{
            'data':self.db.all(),
            'status':200
        }

    def post(self):
        """create user"""
        data=request.get_json()

        user={

            'firstname' : data['firstname'],
            'lastname' : data['lasttname'],
            'othernames' : data['othernames'],
            'email' : data['email'],
            'phoneNumber' : data['phoneNumber'],
            'username' : data['username'], 
            'registered' : data['registered'],
            'isAdmin' : None,
        }

        self.db.save(user)
        return{
            'message':'user is saved successfully!'
        }, 201