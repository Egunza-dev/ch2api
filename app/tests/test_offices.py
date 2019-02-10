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

    
    def test_api_can_get_all_offices(self):
        """Test endpoint that fetches all offices"""

        res = self.client().get(path='/api/v1/offices/', content_type='application/json')
        self.assertEqual(res.status_code, 200)
        self.assertIn('President', str(res.data))


    def test_api_can_get_office_by_id(self):
        """Test endpoint that fetches a particular office"""

        res = self.client().get('/api/v1/offices/2')
        self.assertEqual(res.status_code, 200)
        self.assertIn('legislative', str(res.data))



if __name__ == "__main__":
    unittest.main()