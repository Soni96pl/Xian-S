from datetime import datetime

from flask import request
from flask_jwt import jwt_required, current_identity
from flask_restful import reqparse

import pymongo
import xiandb as db

from xians.resource import Resource


class Trip(Resource):
    decorators = [jwt_required()]
    default_fields = ['user_id', 'name', 'segments']
    default_sort = [('date', pymongo.DESCENDING)]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help="Name is required!")
        parser.add_argument('date',
                            type=lambda t: datetime.fromtimestamp(int(t)),
                            required=True,
                            help="Date is required!")
        params = parser.parse_args()

        trip = db.Trip.add(current_identity['_id'], **params)

        if trip:
            location = '%strips/%s' % (request.url_root, trip.inserted_id)

            return {
                'success': True,
                'message': "Trip added successfully"
            }, 201, {'Location': location}

        return {
            'success': False,
            'message': "Trip with a given name"
        }, 409
