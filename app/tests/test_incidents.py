from db_con import init_db
import unittest
from app import create_app
import json

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app=create_app()
        self.client=self.app.test_client()
        self.app_content = self.app.app_context()
        self.app_content.push()

        self.test_incident = {
                "type":"Redflag",
                "status":"Draft",
                "comment":"Corruption cases in Mombasa County",
                "location":"Mombasa County"
                }
    def test_create_incident(self):
        response=self.client.post('/api/v2/interventions',
                                    data=json.dumps(self.test_incident),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Cheers, intervention record created')
        self.assertEqual(response.status_code, 201)

    def test_fetch_all_incidents(self):
        response=self.client.get('/api/v2/interventions',
                                    data=json.dumps(self.test_incident),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'All records are successfully returned')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response=self.client.delete('/api/v2/interventions/6')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Intervention record has been deleted')
        self.assertEqual(response.status_code, 200)

    def test_edit_location(self):
        response=self.client.patch('/api/v2/interventions/6/location',
                                    data=json.dumps(self.test_incident),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Updated record’s location')
        self.assertEqual(response.status_code, 200)
    
    def test_edit_comment(self):
        response=self.client.patch('/api/v2/interventions/6/comment',
                                    data=json.dumps(self.test_incident),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Updated record’s comment')
        self.assertEqual(response.status_code, 200)



    
    

        

       