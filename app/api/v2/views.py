import datetime
from werkzeug.security import generate_password_hash
from flask import jsonify, request, make_response
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_identity, create_access_token
from flask_restful.reqparse import RequestParser
import psycopg2
from db_con import init_db
from.models import UsersModel


class UserRegistration(Resource):
    def __init__(self):
        self.db = UsersModel()

    def post(self):
        data = request.get_json(silent=True)
        username = data["username"]
        email = data["email"]
        firstname = data["firstname"]
        lastname = data['lastname']
        phonenumber = data["phonenumber"]
        password = data["password"]
        repeat_password = data["repeat_password"]

        response = None
        if username.isspace():
                response = {"message": "Enter the username"}
        if password.isspace() or len(password.strip()) < 10:
            response = {"message": "Enter a valid password"}
        if firstname.isspace():
            response = {"message": "Enter the first name"}
        if lastname.isspace():
            response = {"message": "Enter the last name"}
        if email.isspace():
            response = {"message": "Enter a valid email"}

        if response is not None:
            return jsonify(response)

        usrname = self.db.get_username(username)
        confirm_mail = self.db.get_email(email)

        if usrname:
            return jsonify({
                "message": "username exists"
            })
        if confirm_mail:
            return jsonify({
                "message": "email exists"
            })
        if password != repeat_password:
            return jsonify({
                "message": "password's don't match"
            })

        data=self.db.save(firstname, lastname, email,
                     phonenumber, username, password)
        return jsonify({
            "message": "user records successfully saved",
            "data":data,
            "status":201
        })

class AllUsers(Resource):
    def __init__(self):
        self.db = UsersModel()

    def get(self):
        output = self.db.get_all()
        
        return make_response(jsonify(
            {
                "message": "user records were successfully returned",
                "data": output,
                "status":200
            }
        ))

class SingleUser(Resource):
    def __init__(self):
        self.db = UsersModel()

    def get(self,id):
        userdata = self.db.get_one(id)
        return make_response(jsonify(
            {
                "message": "user record returned successfully",
                "data": userdata,
                "status":200
            }
        ))

class UserLogin(Resource):

    def __init__(self):
        self.db = UsersModel()

        self.parser=RequestParser()
        self.parser.add_argument('username',type=str,required=True,help='username is Required')
        self.parser.add_argument('password',type=str,required=True,help='password is Required')


    def post(self):
        self.parser.parse_args()
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        if username.isspace() or password.isspace():
            return jsonify({
                "message": "Please, enter all the credentials"
            })

        if password.isspace() or password is None:
            return jsonify({
                "message": "Please enter a valid password"
            })

        user = self.db.get_user(username)
        if not user:
            return jsonify({
                "message": "We do not have an account with those details"
            })
        
        token = create_access_token(identity=user)

        return jsonify({
            "message": "Successfully,logged in now",
            "token":token,
            "status":200
        })
