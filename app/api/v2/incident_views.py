import datetime
import psycopg2
from db_con import init_db
from psycopg2.extras import RealDictCursor
from flask_restful import Api, Resource
from.incident_models import IncidentModel
from.user_models import UserModel
from flask_restful.reqparse import RequestParser
from flask import jsonify, request, make_response
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_identity

class Interventions(Resource):
    def __init__(self):
        self.db = IncidentModel()

        self.parser=RequestParser()
        self.parser.add_argument('type',type=str,required=True,help='Type is Required')
        self.parser.add_argument('location',type=str,required=True,help='Location is Required')
        self.parser.add_argument('comment',type=str, required=True,help='Comment is Required')

    @jwt_required
    def post(self):
        
        self.parser.parse_args()
        data = request.get_json()

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

        user = get_jwt_identity()
        createdby = user.get('id')
        data=self.db.save_record(createdby,type, comment, location, status)
        data['createdOn']=data['createdOn'].strftime('%A %d. %B %Y')
        return {
            "status":201,
            "message": "Cheers, intervention record created",
            "data":[data]
        }, 201

    @jwt_required
    def get(self):
        data = self.db.fetch_records()
        data = self.db.get_all_records(data)
        if not data:
            return {
                "message": "No records found",
                "status":404
            }, 404

        return {
            "message": "All records are successfully returned",
            "data": data
            }

class DeleteRecord(Resource):
    def __init__(self):
        self.db = IncidentModel()
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity().get('id')
        record=self.db.get_specific(id)
        if not record:
            return {
                "message":"Record not Found",
                "status":404
                }
        createdby = record["createdby"]
        if user_id != createdby:
            return {
                "message": "Can not edit another users' record",
                "status":400
            }
        self.db.delete_record(id)
        return {"status": 200,
        "data": {
            "id":id, 
            "message": "Intervention record has been deleted"}}, 200

class Specific(Resource):
    def __init__(self):
        self.db = IncidentModel()
    @jwt_required
    def get(self, id):
        data = self.db.get_specific(id)
        if not data:
            return {
                "message":"Record doesn't exist,Please enter a valid ID"}
        data['createdon']=data['createdon'].strftime('%A %d. %B %Y')
        return {
            "status":200,
            "message":  "success",
            "data":data }, 200
            
class Updatecomment(Resource):
    def __init__(self):
        self.db = IncidentModel()
    @jwt_required
    def patch(self,id):
        user_id = get_jwt_identity().get('id')
        output=self.db.get_specific(id)
        if not output:
            return {
                "message":"Please enter a valid ID",
                "status":400
            }
        
        data = request.get_json()
        comment = data['comment']
        if comment is None or comment is "":
            return {
                "message": "missing data, try again"
                }, 400
        createdby = output["createdby"]
        if user_id != createdby:
            return {
                "message": "Can not edit another users' record",
                "status":400
            }
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
    @jwt_required
    def patch(self,id):
        user_id = get_jwt_identity().get('id')
        output=self.db.get_specific(id)
        if not output:
            return {
                "message":"Please enter a valid ID",
                "status":400
            }
        data = request.get_json()
        location = data['location']
        if location is None or location is "":
            return {
                "message": "missing data, try again"
                }, 400
        createdby = output["createdby"]
        if user_id != createdby:
            return {
                "message": "Can not edit another users' record",
                "status":400
            }
        self.db.update_location(location, id)
        output=self.db.get_specific(id)
        output['createdon']=output['createdon'].strftime('%A %d. %B %Y')
        return{
            "status": 200, 
            "data":
               [{ "data":output, "message": "Updated record’s location"}]}, 200

class AdminRole(Resource):
    def __init__(self):
        self.db = IncidentModel()
        self.db2 = UserModel()
   
    @jwt_required
    def patch (self,id):
        output = self.db.get_specific(id)
        userId = get_jwt_identity().get('id') 
        data = self.db2.isadmin(int(userId))
        if not data:
            return {
                "message": "You are not an admin"
            }
        if not output:
            return {
                "message":"Enter a valid record ID",
                "status":400
            }
        data = request.get_json()
        status = data['status']
        self.db.update_status(status,id)
        output = self.db.get_specific(id)
        output['createdon']=output['createdon'].strftime('%A %d. %B %Y')
        return jsonify({
            "status":200,
            "data":[{"id": id, 
            "message": "Updated intervention record status"}]
        }, 200)


