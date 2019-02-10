from flask import  request, jsonify, make_response 
from app.api.v1 import api
from app.api.v1.offices.models import Office


@api.route('/offices', methods=['GET'], strict_slashes=False)
def get_offices():
    """Fetch all political offices records."""
    offices = Office.get_offices()
    return make_response(jsonify({
        "status":200,
        "data":offices
    }), 200)