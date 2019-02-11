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