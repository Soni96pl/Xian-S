from flask_jwt import jwt_required

import pymongo
import xiandb as db

from xians import permissions
from xians.resource import Resource


class Trip(Resource):
    model = db.Trip
    permissions = {
        'READ': permissions.AUTHORIZED,
        'CREATE': permissions.AUTHORIZED,
        'UPDATE': permissions.AUTHORIZED,
        'DELETE': permissions.AUTHORIZED
    }
    default_fields = ['user_id', 'name', 'transport']
    default_sort = [('date', pymongo.DESCENDING)]
    decorators = [jwt_required()]
