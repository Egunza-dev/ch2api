
parties=[]

class Party: 


    def __init__(self):
        self.parties=parties

    
    
    def post_party(self, name, hqAddress, logoUrl):

        
        party = {
            "id": len(self.parties) + 1,
            "name": name,
            "hqAddress": hqAddress,
            "logoUrl": logoUrl
        }
        
        self.parties.append(party)
        return party



    
    def get_parties(self):
        return self.parties


    
    def get_party(self, party_id):
        for party in self.parties:
            if party['id'] == party_id:
                return [party]
        return None


    
    
    def edit_name(self, party_id, name):
        
        for party in self.parties:
            if party["id"] == party_id:
                party["name"] = name
                return [party]
        return None  

    
    def delete_party(self, party_id):
        for party in self.parties:
            if party['id'] == party_id:
                 self.parties.remove(party)
                 return True
        return False


    



    