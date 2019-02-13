import unittest
import os
import json
from app import create_app


class TestPartiesEndpoints(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""

        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        
        self.party_edit = {                
                        "name" : "SAP" ,
                        "hqAddress" : "Pennsylnvania" ,
                        "logoUrl" : "Bing.png"
                        }
        self.party_del = {                
                        "name" : "Zeus Party" ,
                        "hqAddress" : "Alabama" ,
                        "logoUrl" : "rel.png"
                        }
        self.party_get = {                
                        "name" : "Pitty Party" ,
                        "hqAddress" : "Belfos" ,
                        "logoUrl" : "giga.png"
                        }

        self.party_name = {"name":"Liberal Party"}
        
        self.parties = [{
                
                "name" : "Democratic Party" ,
                "hqAddress" : "Washington Dc" ,
                "logoUrl" : "buf.jpeg"
                },
                {
                
                "name": "Republican Party" ,
                "hqAddress" : "New York" ,
                "logoUrl" : "rudolf.jpg"
                },
                {
                
                "name" : "Conservative Party" ,
                "hqAddress" : "Chicago" ,
                "logoUrl" : "zing.jpg"
                },
                {
                
                "name" : "Labour Party" ,
                "hqAddress" : "Illinois" ,
                "logoUrl" : "hur.png"
                }]

        self.party = {                
                        "name" : "UCL Party" ,
                        "hqAddress" : "Pennsylnvania" ,
                        "logoUrl" : "Zen.png"
                        }

    


    def test_api_can_get_all_parties(self):
        """Test endpoint that fetches all parties"""

        post_res = [None] * len(self.parties)
        for i in range(len(self.parties)):
            post_res[i] = self.client().post('/api/v1/parties/', json=self.parties[i])
        get_res = self.client().get('/api/v1/parties/')     
        self.assertIn(self.parties[3]["name"], str(get_res.data))
        self.assertEqual(get_res.status_code, 200)
            
        

    def test_api_can_get_party_by_id(self):
        """Test endpoint that fetches a particular party"""

        post_res = self.client().post('/api/v1/parties/', json=self.party_get)
        party_id = int(post_res.json['data'][0]["id"])
        get_res = self.client().get('/api/v1/parties/{}'.format(party_id))
        self.assertEqual(post_res.json["data"][0]["name"], get_res.json["data"][0]["name"])
        self.assertEqual(get_res.json["status"], 200)


    def test_api_can_create_party(self):
        """Test endpoint that posts a particular party"""

        post_res = self.client().post('/api/v1/parties/', json=self.party)
        party_id = int(post_res.json['data'][0]["id"])
        get_res = self.client().get('/api/v1/parties/{}'.format(party_id))
        self.assertEqual(post_res.json["data"][0]["name"], get_res.json["data"][0]["name"])
        self.assertEqual(post_res.json["status"], 201)
        

    def test_api_can_edit_party(self):
        """Test endpoint that edits a particular party"""

        post_res = self.client().post('/api/v1/parties/', json=self.party_edit)
        party_id = int(post_res.json['data'][0]["id"])
        patch_res = self.client().patch('/api/v1/parties/{}/name'.format(party_id), json=self.party_name)
        get_res = self.client().get('/api/v1/parties/{}'.format(party_id))
        self.assertEqual(patch_res.json["data"][0]["name"], get_res.json["data"][0]["name"])
        self.assertEqual(patch_res.status_code, 200) 



    def test_party_deletion(self):
        """Test endpoint that deletes a particular party"""

        post_res = self.client().post('/api/v1/parties/', json=self.party_del)
        party_id = int(post_res.json['data'][0]["id"])
        del_res = self.client().delete('/api/v1/parties/{}'.format(party_id))
        get_res = self.client().get('/api/v1/parties/{}'.format(party_id))    
        self.assertEqual(del_res.json["status"], 200)
        self.assertEqual(get_res.json["status"], 404) 


    


    def tearDown(self):
        super(TestPartiesEndpoints, self).tearDown()
        del self.party
        del self.party_del
        del self.parties 
        del self.party_get     
        del self.party_edit
        del self.party_name



if __name__ == "__main__":
    unittest.main()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        

    

