import unittest
import os
import json
from app import create_app


class TestPartiesEndpoints(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.party = {                
                        "name" : "UCL Party" ,
                        "hqAddress" : "Pennsylnvania" ,
                        "logoUrl" : "Zen.png"
                        }
        self.party_err = {                
                        "name" : "" ,
                        "hqAddress" : "Pennsylnvania" ,
                        "logoUrl" : "Zen.png"
                        }

        self.party_name = {"name":"Liberal Party"}
        self.party_edit_err = {"name":""}


    def test_api_can_get_all_parties(self):
        """Test endpoint that fetches all parties"""

        res = self.client().get(path='/api/v1/parties/', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Democratic Party', str(res.data))


    def test_api_can_get_party_by_id(self):
        """Test endpoint that fetches a particular party"""

        res = self.client().get('/api/v1/parties/1')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Democratic Party', str(res.data))


    def test_api_can_create_party(self):
        """Test endpoint that posts a particular party"""
        
        res = self.client().post('/api/v1/parties/', json=self.party)
        self.assertEqual(res.status_code, 201)
        self.assertIn('UCL Party', str(res.data))

