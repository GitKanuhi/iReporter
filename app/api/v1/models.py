import datetime
from flask import jsonify,request, make_response

Redflag_list = []
users=[]

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
        return self.redflags

    def all(self):
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
            "message": "error, Incident not Found!"
        }
    
    def edit_location(self,incidentId):
        """Edit the location of a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    incident.update(request.get_json())
                    return {
                        'status':200,
                        'data':[{
                            'id':incidentId,
                            'message':'Updated incident location'
                        }]
                           }
                elif incident['status']=='under investigation':
                    return {
                        'status':404,
                        'error': 'incident under investigation'
                    }
                elif incident['status']=='resolved':
                    return {
                        'status':404,
                        'error': 'incident resolved'
                    }
                elif incident['status']=='rejected':
                    return {
                        'status':404,
                        'error': 'incident rejected'
                    }

    def edit_comment(self,incidentId):
        """Edit the comment/description of a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    incident.update(request.get_json())
                    return {
                        'status':200,
                        'data':[{
                            'id':incidentId,
                            'message':'Updated incident comment'
                        }]
                           }
                elif incident['status']=='under investigation':
                    return {
                        'status':404,
                        'error': 'incident under investigation'
                    }
                elif incident['status']=='resolved':
                    return {
                        'status':404,
                        'error': 'incident resolved'
                    }
                elif incident['status']=='rejected':
                    return {
                        'status':404,
                        'error': 'incident rejected'
                    }
                
    def delete_incident(self,incidentId):
        """Delete a specific red-flag record"""
        for incident in self.redflags:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    self.redflags.remove(incident)
                    return {
                        'status':204,
                        'data':[{
                            'id':incidentId,
                            'message':'red-flag record deleted'
                        }]
                           }
                elif incident['status']=='under investigation':
                    return {
                        'status':404,
                        'error': 'incident under investigation'
                    }
                elif incident['status']=='resolved':
                    return {
                        'status':404,
                        'error': 'incident resolved'
                    }
                elif incident['status']=='rejected':
                    return {
                        'status':404,
                        'error': 'incident rejected'
                    }

class UserModel:
    """class user model"""
    def __init__(self):
        """ Initialize the user model class"""
        self.users = users
    
    def all(self):
        """Returning all users"""
        return self.users
    
    def save(self,data):
        data['id']= self.__generate_id()
        self.users.append(data)

    def find(self, id):
        """Find users"""
        for user in self.users:
            if user['id']==id:
                return user
            else:
                return None

    def __generate_id(self):
        if len(self.users):
            return self.users[-1]['id'] + 1
        else:
            return 1
    