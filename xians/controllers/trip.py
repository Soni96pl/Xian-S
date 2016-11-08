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

    def get(self, _id=None):
        fields, sort = self.get_query()

        return db.Trip.search(_id=_id,
                              fields=fields,
                              sort=sort)

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
            'message': "Trip with a given name already exists"
        }, 409


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

        trip = db.Trip.get(trip_id)
        if not trip:
            return {
                'success': False,
                'message': "Trip with a given id doesn't exist"
            }, 404

        if not segment_id:
            segment_id = trip.add_segment(segment)

            location = '%strips/%d/segments/%d' % (
                        request.url_root,
                        trip_id,
                        segment_id)

            return {
                'success': True,
                'message': "Segment added successfully"
            }, 201, {'Location': location}
        else:
            segment['_id'] = segment_id
            segment_id = trip.update_segment(segment)

            return {
                'success': True,
                'message': "Segment updated successfully"
            }, 201

    def delete(self, trip_id, segment_id):
        trip = db.Trip.get(trip_id)
        if not trip:
            return {
                'success': False,
                'message': "Trip with a given id doesn't exist"
            }, 404

        if not trip.remove_segment(segment_id):
            return {
                'success': False,
                'message': "Segment with a given id doesn't exist"
            }, 404

        return {
            'success': True,
            'message': "Segment removed successfully"
        }, 201
