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

    def get(self, trip_id=None):
        fields, sort = self.get_query()

        return db.Trip.search(_id=trip_id,
                              fields=fields,
                              sort=sort)

    def post(self, trip_id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help="Name is required!")
        parser.add_argument('date',
                            type=lambda t: datetime.fromtimestamp(int(t)),
                            required=True,
                            help="Date is required!")
        trip = parser.parse_args()
        trip['user_id'] = current_identity['_id']

        headers = {}

        if not trip_id:
            trip_id = db.Trip.add(trip)
            success = trip_id is not False
        else:
            success = db.Trip.update(trip_id, trip)

        if success:
            message = "Trip upserted successfully"
            headers['Location'] = '%strips/%s' % (request.url_root, trip_id)
            code = 201
        else:
            message = "Trip with a given name already exists"
            code = 409

        return {'success': success, 'message': message}, code, headers

    def delete(self, trip_id):
        success = db.Trip.delete(trip_id)
        if success:
            message = "Trip removed successfully"
            code = 200
        else:
            message = "Trip with a given id doesn't exist"
            code = 404

        return {'success': success, 'message': message}, code


class Segment(Resource):
    decorators = [jwt_required()]
    default_fields = ['user_id', 'name', 'segments']
    default_sort = [('date', pymongo.DESCENDING)]

    def post(self, trip_id, segment_id=None):
        parser = reqparse.RequestParser()
        parser.add_argument('origin_id', type=int, required=True,
                            help="Origin is required!")
        parser.add_argument('destination_id', type=int, required=True,
                            help="Destination is required!")
        parser.add_argument('departure',
                            type=lambda t: datetime.fromtimestamp(int(t)))
        parser.add_argument('arrival',
                            type=lambda t: datetime.fromtimestamp(int(t)))
        parser.add_argument('mode', type=int)
        parser.add_argument('carrier', type=int)
        parser.add_argument('price', type=float)
        segment = parser.parse_args()
        headers = {}

        trip = db.Trip.get(trip_id)
        if not trip:
            return {
                'success': False,
                'message': "Trip with a given id doesn't exist"
            }, 404, headers

        if not segment_id:
            segment_id = trip.add_segment(segment)
            success = segment_id is not False
        else:
            success = trip.update_segment(segment_id, segment)

        if success:
            message = "Segment upserted successfully"
            code = 201
            headers['Location'] = '%strips/%d/segments/%d' % (
                request.url_root,
                trip_id,
                segment_id
            )
        else:
            message = "Segment conflicts with another one"
            code = 409

        trip.save()
        return {'success': success, 'message': message}, code, headers

    def delete(self, trip_id, segment_id):
        trip = db.Trip.get(trip_id)
        if not trip:
            return {
                'success': False,
                'message': "Trip with a given id doesn't exist"
            }, 404

        success = trip.remove_segment(segment_id)
        if success:
            message = "Segment removed successfully"
            code = 200
        else:
            message = "Segment with a given id doesn't exist"
            code = 404

        trip.save()

        return {'success': success, 'message': message}, code
