from flask_jwt import current_identity

import pymongo
import xiandb as db

from xians import permissions
from xians.resource import Resource


class Favorites(Resource):
    permissions = {
        'READ': permissions.AUTHORIZED,
        'CREATE': permissions.AUTHORIZED,
        'DELETE': permissions.AUTHORIZED
    }
    default_fields = ['_id', 'name', 'coordinates', 'country', 'population']
    default_sort = [('population', pymongo.DESCENDING)]

    def get(self):
        self.check_permissions('READ')

        fields, sort = self.get_query()

        return db.City.search(_id={'$in': current_identity['favorites']},
                              fields=fields,
                              sort=sort)

    def put(self, city_id):
        self.check_permissions('CREATE')

        success = current_identity.add_favorite(city_id)
        if success:
            message = "Added a favorite successfully"
        else:
            message = "This city is already a favorite"

        current_identity.save()
        return {'success': success, 'message': message}

    def delete(self, city_id):
        self.check_permissions('DELETE')

        success = current_identity.remove_favorite(city_id)
        if success:
            message = "Removed a favorite successfully"
        else:
            message = "This city isn't a favorite"

        current_identity.save()
        return {'success': success, 'message': message}
