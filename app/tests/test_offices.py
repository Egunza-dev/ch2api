import unittest
import os
import sys
import json
from app import create_app


class TestOfficesEndpoints(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.office = {"type":"State",
                        "name":"Secretary of State"}
        self.office_err = {"type":"",
                        "name":"Secretary of State"}

        self.offices =  [
                            {            
                                "type" : "state" ,
                                "name" : "President"
                            },
                            {            
                                "type" : "legislative" ,
                                "name" : "MP"
                            },
                            {            
                                "type" : "local government" ,
                                "name" : "Senator"
                            },
                            {            
                                "type" : "local government" ,
                                "name" : "Governor"
                            }
                            ]

    
    def test_api_can_get_all_offices(self):
        """Test endpoint that fetches all offices"""

        post_res = [None] * len(self.offices)
        for i in range(len(self.offices)):
            post_res[i] = self.client().post('/api/v1/offices/', json=self.offices[i])
        get_res = self.client().get('/api/v1/offices/')     
        self.assertIn(self.offices[3]["name"], str(get_res.data))
        self.assertEqual(get_res.status_code, 200)
        


    def test_api_can_get_office_by_id(self):
        """Test endpoint that fetches a particular office"""

        post_res = self.client().post('/api/v1/offices/', json=self.office)
        office_id = int(post_res.json['data'][0]["id"])         
        get_res = self.client().get('/api/v1/offices/{}'.format(office_id))
        self.assertEqual(post_res.json["data"][0]["id"], get_res.json["data"][0]["id"])
        self.assertEqual(get_res.json["status"], 200)

    
    def test_api_can_create_office(self):
        """Test endpoint that posts a particular office"""

        post_res = self.client().post('/api/v1/offices/', json=self.office)
        office_id = int(post_res.json['data'][0]["id"])
        get_res = self.client().get('/api/v1/offices/{}'.format(office_id))
        self.assertEqual(post_res.json["data"][0]["name"], get_res.json["data"][0]["name"])
        self.assertEqual(post_res.json["status"], 201)


    
    
    def tearDown(self):
        super(TestOfficesEndpoints, self).tearDown()
        del self.office
        del self.office_err
        del self.offices



if __name__ == "__main__":
    unittest.main()