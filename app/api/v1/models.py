import datetime
from flask import jsonify,request, make_response

incident_list = []

class IncidentModel:

    def __init__(self):
        self.incidences = incident_list
        self.status = 'draft'

    def create_incident(self, createdBy, type, location, image, videos,comment):

        incidentData= {
         'incidentId': len(incident_list)+ 1, 
         'createOn': datetime.datetime.now().strftime('%I:%M%p %B %d, %Y'),
         'createdBy': createdBy,
         'type': type,
         'location': location,
         'status': self.status,
         'image': image,
         'videos': videos,
         'comment': comment
        }
        self.incidences.append(incidentData)
        return self.incidences

    def all(self):
        return self.incidences
    
    
    def get_specific(self, incidentId):
        for incident in self.incidences:
            if incident['incidentId']==int(incidentId):
                return {
                    "status":200,
                    "data":incident
                }
        return{
            "status":404,
            "error": "Incident not Found!"
        }
    
    def edit_location(self,incidentId):
        for incident in self.incidences:
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
        for incident in self.incidences:
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
        for incident in self.incidences:
            if incident['incidentId']==int(incidentId):
                if incident['status']=='draft':
                    self.incidences.remove(incident)
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