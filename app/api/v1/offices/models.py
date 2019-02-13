offices = []

class Office:   


    def __init__(self):

        self.offices = offices 


    def post_office(self, name, office_type):

        
        office = {
            "id": len(self.offices) + 1,
            "name": name,
            "type": office_type,
                    }
        
        self.offices.append(office)
        return office       
       


    def get_offices(self):
        return self.offices


    
    def get_office(self, office_id):
        for office in self.offices:
            if office['id'] == office_id:
                return [office]
        return None

    
    

    
