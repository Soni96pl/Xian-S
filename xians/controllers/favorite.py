from flask_jwt import jwt_required, current_identity

import pymongo
import xiandb as db

from xians.resource import Resource


class Favorites(Resource):
    decorators = [jwt_required()]
    default_fields = ['_id', 'name', 'coordinates', 'country', 'population']
    default_sort = [('population', pymongo.DESCENDING)]

    def get(self):
        fields, sort = self.get_query()

        return db.City.search(_id={'$in': current_identity['favorites']},
                              fields=fields,
                              sort=sort)

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
