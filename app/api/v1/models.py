import datetime
from flask import jsonify,request, make_response
from flask_restful.reqparse import RequestParser

"""contains models and their methods"""

Redflag_list = []

"""empty list for incidents"""

class RedflagModel:
    """class to handle redflag models"""

    def __init__(self):

        """Initialize redflag Class"""

        self.redflags = Redflag_list
        self.status = 'draft'

    def create_redflag(self, createdBy, recordType, location, image, videos,comment):

        """Method for creating Red-flag"""
        """strftime function is used to format the output of a date in python"""

        redflagData= {
         'incidentId': len(Redflag_list)+ 1, 
         'createOn': datetime.datetime.now().strftime('%I:%M%p %B %d, %Y'),
         'createdBy': createdBy,
         'recordType': recordType,
         'location': location,
         'status': self.status,
         'image': image,
         'videos': videos,
         'comment': comment
        }
        self.redflags.append(redflagData)
        return redflagData

    def view_all(self):
        
        """method for fetching all red-flag records"""

        return self.redflags
    
    def get_specific(self, incidentId):
        """method for fetching a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==incidentId:
                return {
                    "status":200,
                    "data":incident,
                    "message": "Incident fetched successfully!"
                }

        return {
            "status":404,
            "message": "error, Redflag not Found! Please enter a valid Incident ID"
        }
    
    def edit_location(self,incidentId):
        """method for editing the location of a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    incident.update(request.get_json())
                    return {
                        'status':200,
                        'data':incident,
                        'message':'Updated incident location'
                           }
        return {
            "status":404,
            "message": "error, Please enter a valid Incident ID'!"
        }
                
    def edit_comment(self,incidentId, data):
        """method for editing the comment/description of a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    incident.update(data)
                    return {
                        'status':200,
                        'data':incident,
                        'message':'Updated incident comment'
                           }
        return {
            "status":404,
            "message": "error, Please enter a valid Incident ID'!"
        }

    def delete_incident(self,incidentId):
        """method for deleting a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    self.redflags.remove(incident)
                    return {
                        'status':200,
                        'message': 'Successfully deleted, record does not exist'
                           }
        return {
            "status":404,
            "message": "error, Please enter a valid Incident ID for deletion'!"
        }

    