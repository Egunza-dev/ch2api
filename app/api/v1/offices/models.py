class Office:

    offices = [
        {
            "id" : 1,
            "type" : "state" ,
            "name" : "President"
        },
        {
            "id" : 2 ,
            "type" : "legislative" ,
            "name" : "MP"
        },
        {
            "id" : 3 ,
            "type" : "federal" ,
            "name" : "Senator"
        },
        {
            "id" : 4 ,
            "type" : "local government" ,
            "name" : "Governor"
        }
    ]


    @classmethod
    def get_offices(cls):
        return __class__.offices


    @classmethod
    def get_office(cls, office_id):
        for office in __class__.offices:
            if office['id'] == office_id:
                return [office]
        return None