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

        self.test_user = {
            
                "firstname":"John",
                "lastname":"Paul",
                "phonenumber":"0718000000",
                "email":"paul@gmail.com",
                "username":"paul",
                "isAdmin":"False",
                "password": "1234567890",
                "repeat_password":"1234567890"
                }

    def test_create_user(self):
        response=self.client.post('/api/v2//auth/signup',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Your have successfully been registered')
        self.assertEqual(response.status_code, 201)

    
    def test_user_login(self):
        response=self.client.post('/api/v2//auth/login',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'You are successfully logged in now')
        self.assertEqual(response.status_code, 200)

    def test_login_unregistered_user(self):
        response=self.client.post('/api/v2//auth/login',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Username Not Found, try again')
        self.assertEqual(response.status_code, 404)

    def test_registration_with_invalid_password(self):
        response=self.client.post('/api/v2//auth/login',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'Invalid Password, try again')
        self.assertEqual(response.status_code, 401)

    
    def test_existingusername(self):
        response=self.client.post('/api/v2//auth/signup',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'This username exists, try a different username')
        self.assertEqual(response.status_code, 400)

    
    def test_existingmail(self):
        response=self.client.post('/api/v2//auth/signup',
                                    data=json.dumps(self.test_user),
                                    content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['Message'], 'This username exists, try a different username')
        self.assertEqual(response.status_code, 400)