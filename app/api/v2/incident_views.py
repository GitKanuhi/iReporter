import datetime
from werkzeug.security import generate_password_hash
from flask import jsonify, request, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_identity, create_access_token
from flask_restful.reqparse import RequestParser
import psycopg2
from db_con import init_db
from.incident_models import IncidentModel

class Interventions(Resource):
    def __init__(self):
        self.db = IncidentModel()

        self.parser=RequestParser()
        self.parser.add_argument('createdBy',type=str,required=True,help='Name is Required')
        self.parser.add_argument('type',type=str,required=True,help='Type is Required')
        self.parser.add_argument('location',type=str,required=True,help='Location is Required')
        self.parser.add_argument('comment',type=str, required=True,help='Comment is Required')

    def post(self):
        
        self.parser.parse_args()
        data = request.get_json()
        createdBy = data["createdBy"]
        type = data["type"]
        status = data["status"]
        comment = data["comment"]
        location = data["location"]

        response = None
        if type.isspace() or type == "":
            response = {
                "message": "Field cannot be empty."}
        if comment.isspace() or comment == "":
            response = {
                "message": "Field cannot be empty"}
        if location.isspace() or location == "":
            response = {
                "message": "Field cannot be empty"}
        if response is not None:
            return jsonify(response)

        data=self.db.save_record(createdBy,type, comment, location, status)
        data['createdOn']=data['createdOn'].strftime('%A %d. %B %Y')
        return {
            "status":201,
            "message": "Cheers, intervention record created",
            "data":[data]
        }, 201

    def get(self):
        data = self.db.get_all_records()
        if data == []:
            return {
                "message": "No records found"
            }, 404
        else:
            return jsonify(
                {
                    "message": "All records are successfully returned",
                    "data": data
                }, 200)

class DeleteRecord(Resource):
    def __init__(self):
        self.db = IncidentModel

    def delete(self,id):
        self.db.delete_record(id)
        return {
    "status": 200, 
    "data": {"id":id, "message": "Intervention record has been deleted"}}, 200

class Specific(Resource):
    def __init__(self):
        self.db = IncidentModel()

    def get(self, id):
        data = self.db.get_specific(id)
        data['createdon']=data['createdon'].strftime('%A %d. %B %Y')
        return {
            "status":200,
            "message":  "success",
            "data":data }, 200
            
class Updatecomment(Resource):
    def __init__(self):
        self.db = IncidentModel()

    def patch(self,id):
        output=self.db.get_specific(id)
        if not output:
            return {
                "message":"Please enter a valid ID"
            }
        data = request.get_json()
        comment = data['comment']
        if comment is None or comment is "":
            return {
                "message": "missing data, try again"
                }, 400
        self.db.update_comment(comment,id)
        output=self.db.get_specific(id)
        output['createdon']=output['createdon'].strftime('%A %d. %B %Y')
        return{
            "status": 200, 
            "data":
               [{"data":output, "message": "Updated record's comment"}]}, 200

class UpdateLocation(Resource):

    def __init__(self):
        self.db =IncidentModel()

    def patch(self,id):
        output=self.db.get_specific(id)
        if not output:
            return {
                "message":"Please enter a valid ID"
            }
        data = request.get_json()
        location = data['location']
        if location is None or location is "":
            return {
                "message": "missing data, try again"
                }, 400
        self.db.update_location(location, id)
        output=self.db.get_specific(id)
        output['createdon']=output['createdon'].strftime('%A %d. %B %Y')
        return{
            "status": 200, 
            "data":
               [{ "data":output, "message": "Updated record’s location"}]}, 200
