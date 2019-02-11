class Party:
 
    parties = [{
                "id" : 1 ,
                "name" : "Democratic Party" ,
                "hqAddress" : "Washington Dc" ,
                "logoUrl" : ""
                },
                {
                "id" : 2,
                "name": "Republican Party" ,
                "hqAddress" : "New York" ,
                "logoUrl" : ""
                },
                {
                "id": 3 ,
                "name" : "Conservative Party" ,
                "hqAddress" : "Chicago" ,
                "logoUrl" : ""
                },
                {
                "id" : 4 ,
                "name" : "Labour Party" ,
                "hqAddress" : "Illinois" ,
                "logoUrl" : ""
                }

    ]



    @classmethod
    def get_parties(cls):
        return __class__.parties


    @classmethod
    def get_party(cls, party_id):
        for party in __class__.parties:
            if party['id'] == party_id:
                return [party]
        return None