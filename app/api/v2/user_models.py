from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import get_jwt_identity, create_access_token
from psycopg2.extras import RealDictCursor
from flask_restful import request
from datetime import datetime
from db_con import init_db
import re

class UserModel():

    def __init__(self):
        self.db = init_db()
        self.curr = self.db.cursor(cursor_factory=RealDictCursor)

    def save(self,firstname,lastname,email,phonenumber,username,password,isAdmin):
        """ saving user details in the database """
        payload = {
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'phonenumber':phonenumber,
            'username':username,
            'password':password,
            'isAdmin':isAdmin
        }

        query = """INSERT INTO users(firstname,lastname,email,phonenumber,username,password, isAdmin) VALUES
        (%(firstname)s,%(lastname)s,%(email)s,%(phonenumber)s,%(username)s,%(password)s,%(isAdmin)s) RETURNING users.*"""
        self.curr.execute(query,payload)
        self.db.commit()

        return self.curr.fetchone()

    def get_one(self,id):
        """ fetching one from the db """
        self.curr.execute("""SELECT firstname,lastname,email,phonenumber,username, isAdmin FROM users WHERE id = %s""", (id,))
        user_record = self.curr.fetchone()
        return user_record

    def get_email(self, email):
        self.curr.execute("""SELECT email FROM users WHERE email = %s""", (email,))
        mail = self.curr.fetchone()
        if mail:
            return mail
        else:
            return None
    
    def get_username(self, username):
        self.curr.execute("""SELECT username FROM users WHERE username = %s""", (username,))
        sname = self.curr.fetchone()
        if sname:
            return sname
        else:
            return None
    
    def validate_password(self, username, password):
        self.password = self.get_password(username)
        success = check_password_hash(self.password, password)
        return success

    def get_password(self, username):
        self.curr.execute("""SELECT * FROM users WHERE username = %s""", (username,))
        pword = self.curr.fetchall()
        if pword:
            password = pword[0]['password']
            return password
        else:
            return None
    
    def get_user(self, username):
        self.curr.execute("""SELECT * FROM users WHERE username = %s""", (username,))
        user = self.curr.fetchall()
        return user
        
    def get_usr_id(self, username):
        user = self.get_user(username)
        usr_id = user[0]['id']
        return usr_id

    def generate_jwt_token(self, username):
        self.usr_id = self.get_usr_id(username)
        token = create_access_token(identity=self.usr_id)
        return token

    def login(self, username):
        token = self.generate_jwt_token(username)
        return token

    def isadmin(self,id):
         self.curr.execute("""SELECT * FROM users WHERE  id = %s""", (id,))
         user = self.curr.fetchall()
         return user
