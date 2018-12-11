from db_con import init_db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import get_jwt_identity, create_access_token
from flask_restful import request
import re


class Users():

    def __init__(self):
        self.db = init_db()

    def save(self,firstname,lastname,email,phonenumber,username,password):
        """ saving user details in the database """
        payload = {
            'firstname':firstname,
            'lastname':lastname,
            'email':email,
            'phonenumber':phonenumber,
            'username':username,
            'password':password
        }

        query = """INSERT INTO users(firstname,lastname,email,phonenumber,username,password) VALUES
        (%(firstname)s,%(lastname)s,%(email)s,%(phonenumber)s,%(username)s,%(password)s)"""
        curr=self.db.cursor()
        curr.execute(query,payload)
        self.db.commit()

    def get_all(self):
        """ fetching all from the db """
        dbconn = self.db
        curr = dbconn.cursor
        curr.execute("SELECT * FROM users")
        user_records = curr.fetchall()
        return user_records

    def get_email(self, email):
        dbconn = self.db
        curr = dbconn.cursor
        curr.execute("""SELECT email FROM users WHERE email = %s""", (email,))
        mail = curr.fetchone()
        if mail:
            return mail
        else:
            return None
    
    def get_username(self, username):
        dbconn = self.db
        curr = dbconn.cursor
        curr.execute("""SELECT username FROM users WHERE username = %s""", (username,))
        sname = curr.fetchone()
        if sname:
            return sname
        else:
            return None

    def get_pass_word(self, password):
        dbconn = self.db
        curr =dbconn.cursor
        curr.execute("""SELECT password FROM users WHERE username = %s""", (password,))
        pword = curr.fetchone()
        if not check_password_hash(pword['password'], password):
            return False
        return True
    
    def generate_jwt_token(self, username):
        self.usr_id = self.get_id(username)
        token = create_access_token(identity=self.usr_id)
        return token

    def login(self, username):
        token = self.generate_jwt_token(username)
        return token








    






    


    
