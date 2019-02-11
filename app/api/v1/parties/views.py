from flask import  request, jsonify, make_response 
from app.api.v1 import api
from app.api.v1.parties.models import Party


@api.route('/parties', methods=['GET'], strict_slashes=False)
def get_parties():
    """Fetch all political parties records."""
    parties = Party.get_parties()
    return make_response(jsonify({
        "status":200,
        "data":parties
    }), 200)


@api.route('/parties/<int:party_id>', methods=['GET'], strict_slashes=False)
def get_party(party_id):
    """Fetch a specific political party record."""
    party = Party.get_party(party_id)
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
        party = Party(name, hqAddress, logoUrl)
        
        return make_response(jsonify({
            "status":201,
            "data": [{"id":party.id,
                    "name":party.name }]
        }), 201)
    except AssertionError as exception_message:
        return make_response(jsonify({
                                        "status":400,
                                        "error": "{}".format(exception_message)
                                        }), 400)