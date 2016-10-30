from flask_restful import Resource
from flask_jwt import jwt_required, current_identity

import pymongo
import xiandb as db


class Favorites(Resource):
    decorators = [jwt_required()]

    def get(self):
        def process(city):
            return {
                'id': city['_id'],
                'name': city['name'],
                'coordinates': city['coordinates'],
                'country': city['country']
            }

        return map(process, db.City.aggregate([
            {'$match': {'_id': {'$in': current_identity['favorites']}}},
            {'$project': {
                'name': 1,
                'coordinates': 1,
                'country': 1,
                'population': 1
            }},
            {'$sort': {
                'population': pymongo.DESCENDING
            }}
        ]))


class Favorite(Resource):
    decorators = [jwt_required()]

    def put(self, city_id):
        success = current_identity.add_favorite(city_id)
        if success:
            message = "Added a favorite successfully"
        else:
            message = "This city is already a favorite"

        current_identity.save()
        return {'success': success, 'message': message}

    def delete(self, city_id):
        success = current_identity.remove_favorite(city_id)
        if success:
            message = "Removed a favorite successfully"
        else:
            message = "This city isn't a favorite"

        current_identity.save()
        return {'success': success, 'message': message}
