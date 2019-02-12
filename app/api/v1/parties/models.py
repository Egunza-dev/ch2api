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


    def __init__(self, name, hqAddress, logoUrl):

        
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl
        self.id = __class__.parties[-1]["id"] + 1
        __class__.parties.append(self.__repr__())



    @classmethod
    def get_parties(cls):
        return __class__.parties


    @classmethod
    def get_party(cls, party_id):
        for party in __class__.parties:
            if party['id'] == party_id:
                return [party]
        return None

    @classmethod
    def edit_name(cls, party_id, name):

        
        for party in __class__.parties:
            if party["id"] == party_id:
                party["name"] = name
                return [party]
        return None  

    @classmethod
    def delete_party(cls, party_id):
        for party in __class__.parties:
            if party['id'] == party_id:
                 __class__.parties.remove(party)
                 return True
        return False



    def __repr__(self):
        return {"id":self.id,
                "hqAddress":self.hqAddress,
                "name":self.name,
                "logoUrl":self.logoUrl
                }