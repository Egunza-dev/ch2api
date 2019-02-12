from flask import  request, jsonify, make_response 
from app.api.v1 import api
from app.api.v1.parties.models import Party, parties


@api.route('/parties', methods=['GET'], strict_slashes=False)
def get_parties():
    """Fetch all political parties records."""
    parties = Party().parties
    if not parties:
            return make_response(jsonify({
                "status": 404,
                "error": "There exists no party on the Politico platform",
        }), 404)
    return make_response(jsonify({
        "status":200,
        "data":parties
    }), 200)


@api.route('/parties/<int:party_id>', methods=['GET'], strict_slashes=False)
def get_party(party_id):
    """Fetch a specific political party record."""
    party = Party().get_party(party_id)
    if party == None:
        return make_response(jsonify({
        "status":404,
        "error":"The party does not exist on the Politico platform."
    }), 404)
    return make_response(jsonify({
        "status":200,
        "data":party
    }), 200)



@api.route('/parties', methods=['POST'], strict_slashes=False)
def create_party():
    """Create a political party."""
    data =request.get_json(force=True)
    name = data["name"]
    hqAddress = data["hqAddress"]
    logoUrl = data["logoUrl"]
    try: 

        validate_post(name, hqAddress, logoUrl)
        party = Party().post_party(name, hqAddress, logoUrl)
        
        return make_response(jsonify({
            "status":201,
            "data": [{"id":party["id"],
                    "name":party["name"] }]
        }), 201)
    except AssertionError as exception_message:
        return make_response(jsonify({
                                        "status":400,
                                        "error": "{}".format(exception_message)
                                        }), 400)


@api.route('/parties/<int:party_id>/name', methods=['PATCH'], strict_slashes=False)
def edit_party(party_id):
    """Edit the name of a specific political party."""
    data =request.get_json(force=True)

    try:

        validate_edit(data["name"])
        party = Party().edit_name(party_id, data["name"])
        
        if party != None:        
            return make_response(jsonify({
                "status":200,
                "data": [{"id":party[0]["id"],
                        "name":party[0]["name"] }]
                }), 200)

        return make_response(jsonify({
        "status":404,
        "error":"The party does not exist on the Politico platform."
        }), 404)
    except AssertionError as exception_message:
        return make_response(jsonify({
                                        "status":400,
                                        "error": "{}".format(exception_message)
                                        }), 400)
                                        

@api.route('/parties/<int:party_id>/', methods=['DELETE'], strict_slashes=False)
def delete_party(party_id):
    """Delete a specific political party."""
    
    if Party().delete_party(party_id) == False:
        return make_response(jsonify({
        "status":404,
        "error":"The party does not exist on the Politico platform."
    }), 404)

   
    return make_response(jsonify({
        "status":200,
        "data":[{"message":"The political party was successfully deleted from the platform."}]
    }), 200)


def validate_edit(name):
        if not name:
            raise AssertionError("New Party name should be provided!")
        elif not isinstance(name, str):
            raise AssertionError("Party name should be a string!")

def validate_post(name, hqAddress, logoUrl):
        if not name:
            raise AssertionError("Party name should be provided!")
        elif not hqAddress:
            raise AssertionError("Party hqAddress should be provided!")
        elif not logoUrl:
            raise AssertionError("Party logoUrl should be provided!")
        elif not isinstance(name, str):
            raise AssertionError("Party name should be a string!")
        elif not isinstance(hqAddress, str):
            raise AssertionError("Party hqAddress should be a string!")
        elif not isinstance(logoUrl, str):
            raise AssertionError("Party logoUrl should be a string!")        
        elif any(party['name'] == name for party in parties):
            raise AssertionError("That party already exists!")