import datetime
from flask import jsonify,request, make_response
from flask_restful.reqparse import RequestParser

Redflag_list = []
class RedflagModel:
    """Initialize Red-Flag Class"""
    def __init__(self):
        self.redflags = Redflag_list
        self.status = 'draft'

    def create_redflag(self, createdBy, recordType, location, image, videos,comment):
        """Create Red-flag"""
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

        """Fetch all red-flag records"""
        return self.redflags
    
    def get_specific(self, incidentId):
        """Fetch a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==incidentId:
                return {
                    "status":200,
                    "data":incident
                }

        return {
            "status":404,
            "message": "error, Redflag not Found! Please enter a valid Incident ID"
        }
    
    def edit_location(self,incidentId):
        """Edit the location of a specific red-flag record"""
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
        """Edit the comment/description of a specific red-flag record"""
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
        """Delete a specific red-flag record"""
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

    