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