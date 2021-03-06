from db_con import init_db
from datetime import datetime
from flask_restful import request
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash,check_password_hash

class IncidentModel():
    def __init__(self):
        self.db = init_db()
        self.curr = self.db.cursor(cursor_factory=RealDictCursor)
 
    def save_record(self, createdBy, type,comment, location, status = None):
        payload ={

            'createdOn':datetime.utcnow(),
            'createdBy':createdBy,
            'type':type,
            'status':"draft" if status is None else status,
            'comment':comment,
            'location':location
        }
        query = """INSERT INTO incidences(createdOn, createdBy,type, status,comment, 
                                            location)VALUES(%(createdOn)s, 
                                            %(createdBy)s,%(type)s, 
                                            %(status)s,%(comment)s, 
                                            %(location)s) RETURNING incidences.*"""
        self.curr.execute(query,payload)
        self.db.commit()
        return payload

    @staticmethod
    def get_all_records(records):
        result = []
        if not records:
            return result

        for record in records:
            record["createdon"] = record["createdon"].strftime('%A %d. %B %Y')
            result.append(record)
        return result

    def fetch_records(self):
        self.curr.execute("""SELECT * FROM incidences""")
        get_list = self.curr.fetchall()
        return get_list

    def get_specific(self,id):
        self.curr.execute("""SELECT * FROM incidences WHERE id = %s""", (id,))
        get_one = self.curr.fetchone()
        return get_one

    def delete_record(self,id):
        """Deleting a specific intervention record"""
        self.curr.execute("""DELETE FROM incidences WHERE id = %s""", (id,))   
        self.db.commit()

    def update_comment(self, comment, id):
        self.curr.execute( """UPDATE incidences SET comment = %s WHERE id = %s""", (comment,id)) 
        self.db.commit()

    def update_location(self, location,id):
        self.curr.execute( """UPDATE incidences SET location = %s WHERE id = %s""", (location,id)) 
        self.db.commit()

    def update_status(self, status,id):
        self.curr.execute( """UPDATE incidences SET status = %s WHERE id = %s""", (status,id)) 
        self.db.commit()