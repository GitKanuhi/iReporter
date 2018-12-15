import re
import datetime
import psycopg2
from db_con import init_db
from.user_models import UserModel
from flask_restful import Api, Resource
from flask_restful.reqparse import RequestParser
from flask import jsonify, request, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_identity, create_access_token


class UserRegistration(Resource):

    def __init__(self):
        self.db = UserModel()

    def post(self):
        """ Register a user to the system"""
        
        data = request.get_json(silent=True)
        username = data["username"]
        email = data["email"]
        firstname = data["firstname"]
        lastname = data['lastname']
        phonenumber = data["phonenumber"]
        password =generate_password_hash(data["password"])
        repeat_password = data["repeat_password"]

        response = None
        if username.isspace():
                response = {"message": "Enter the username"}
        if password.isspace() or len(password) >=4 and password.isalnum():
            response = {"message": "Enter a valid password"}
        if firstname.isspace() or firstname == "":
            response = {"message": "Enter the first name"}
        if lastname.isspace() or lastname == "":
            response = {"message": "Enter the last name"}
        if email.isspace() or email == "":
            response = {"message": "Enter a valid email"}
            
        if response is not None:
            return jsonify(response)

        usrname = self.db.get_username(username)
        confirm_mail = self.db.get_email(email)

        if usrname:
            return jsonify({
                "message": "This username exists, try a different username",
                "status":400
            })
        if confirm_mail:
            return jsonify({
                "message": "The email exists, try a different email",
                "status":400
            })
        if not check_password_hash(password, repeat_password):
            return jsonify({
                "message": "The passwords entered don't match",
                "status":401
            })

        data=self.db.save(username, email, firstname, lastname,phonenumber,password)
        return jsonify({
            "message": "Your have successfully been registered",
            "data":data,
            "status":201
        })


class UserLogin(Resource):
    def __init__(self):
        self.db = UserModel()

        self.parser=RequestParser()
        self.parser.add_argument('username',type=str,required=True,help='username is Required')
        self.parser.add_argument('password',type=str,required=True,help='password is Required')
    
    def post(self):
        """ Log in a user to the system """

        self.parser.parse_args()
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        username = request.json.get('username')


        if username.isspace() or password.isspace():
            return jsonify({
                "message": "Whitespace fields not allowed, please enter details again",
                "status":400
            })
        if username == "" or password == "":
            return jsonify({
                "message": "Empty fields not allowed, please enter details again",
                "status":400
            })
        
        user = self.db.get_user(username)
        if not user:
            return jsonify({
                "message": "Username Not Found, try again",
                "status":404
            })
        if not self.db.validate_password(username,password):
            return jsonify({
            "message": "Invalid Password, try again",
            "status":401
            })
        token = create_access_token(identity=user[0])
        return jsonify({
            "message": username + " you are successfully logged in now",
            "token":token,
            "status":200
        })

class AllUsers(Resource):

    def __init__(self):
        self.db = UserModel()

    def get(self):
        """ Fetching all users """
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
        self.db = UserModel()
    def get(self,id):
        """ Fetching a single user """
        userdata = self.db.get_one(id)
        return make_response(jsonify(
            {
                "message": "user record returned successfully",
                "data": userdata,
                "status":200
            }
        ))