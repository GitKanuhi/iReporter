import unittest
from app import create_app
import json

class TestModels(unittest.TestCase):
    def setUp(self):
        self.app=create_app()
        self.client=self.app.test_client()
       

        self.incident={
   "status":"draft",
   "type":"redflag",
   "createdBy":"Edward G. Kanuhi", 
   "location":"23e,40s",
   "image":"picture",
   "videos":"videos",
   "comment":"Today is the presentation day",
   "incidentId": 4
}
    
    def test_create_redflag(self):
        response=self.client.post('/api/v1/red-flags',data=json.dumps(self.incident),content_type='application/json')
        result=json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code,201)

    def test_fetch_all(self):
        response=self.client.get('/api/v1/red-flags',data=json.dumps(self.incident),content_type='application/json')
        result=json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code, 200)
        {
        
            "createdBy":"Edward Kanuhi",
            "type":"interventions", 
            "location":"45E, 23N",
            "image":"picture",
            "videos":"videos",
            "comment":"Pot holes on season road"
    
            }

    def test_get_specific(self):
        response=self.client.get('/api/v1/red-flags/1')
        result=json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        print(result)
        self.assertEqual(result['data']['status'],'draft')


    def test_delete(self):
        response=self.client.delete('/api/v1/red-flags/4')
        result=json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code, 200)

    def test_edit_comment(self):
        response=self.client.patch('/api/v1/red-flags/4/comment',data=json.dumps(self.incident),content_type='application/json')
        result=json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code, 200)

    def test_edit_location(self):
        response=self.client.patch('/api/v1/red-flags/4/location',data=json.dumps(self.incident),content_type='application/json')
        result=json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code, 200)   

    def test_validate_data_empty(self):
        response=self.client.post('/api/v1/red-flags',data=json.dumps(self.incident),content_type='application/json')
        result=json.loads(response.data.decode())
        print(result)
        self.assertEqual(response.status_code,201)

if __name__ == "__main__":
    unittest.main()
 


       