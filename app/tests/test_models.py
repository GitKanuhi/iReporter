import unittest
from app import create_app
import json

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app=create_app()
        self.client=self.app.test_client()
        self.app_context=self.app

        self.incident={
            "createdBy":"Edward Kanuhi", 
            "type":"interventions", 
            "location":"45E, 23N",
            "image":"picture",
            "videos":"videos",
            "comment":"Pot holes on season road"
            }
    def test_create_incident(self):
        response=self.client.post('/api/v1/red-flags',data=json.dumps(self.incident),content_type='application/json')
        result=json.loads(response.data.decode())
        self.assertEqual(result['message'],'Successfully created incident report', msg='incident not crated')
        self.assertEqual(response.status_code,201)
