from flask import  request, jsonify, make_response 
from app.api.v1 import api
from app.api.v1.offices.models import Office, offices


@api.route('/offices', methods=['GET'], strict_slashes=False)
def get_offices():
    """Fetch all political offices records."""
    offices = Office().get_offices()
    if not offices:
            return make_response(jsonify({
                "status": 404,
                "error": "There exists no office on the Politico platform",
        }), 404)
    return make_response(jsonify({
        "status":200,
        "data":offices
    }), 200)


@api.route('/offices/<int:office_id>', methods=['GET'], strict_slashes=False)
def get_office(office_id):
    """Fetch a specific political office record."""
    office = Office().get_office(office_id)
    if office == None:
        return make_response(jsonify({
        "status":404,
        "error":"The office does not exist on the Politico platform."
        }), 404)
    return make_response(jsonify({
        "status":200,
        "data":office
    }), 200)



@api.route('/offices', methods=['POST'], strict_slashes=False)
def create_office():
    """Create a political office ."""
    data =request.get_json(force=True)
    office_type = data["type"]
    name = data["name"]
    try: 
        validate_post(office_type, name)   
        office = Office().post_office(office_type, name)    

        return make_response(jsonify({
            "status":201,
            "data": [{"id":office["id"],
                    "name":office["name"] }]
        }), 201)
    except AssertionError as exception_message:
        return make_response(jsonify({
                                        "status":400,
                                        "error": "{}".format(exception_message)
                                        }), 400)



def validate_post(office_type, name):
        if not office_type:
            raise AssertionError("Office type should be provided!")
        elif not name:
            raise AssertionError("Office name should be provided!")
        elif not isinstance(name, str):
            raise AssertionError("Office name should be a string!")
        elif not isinstance(office_type, str):
            raise AssertionError("Office type should be a string!")
        elif any(office['name'] == name for office in offices):
            raise AssertionError("That office already exists!")
        
        
        