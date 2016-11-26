import xiandb as db

from xians import permissions
from xians.resource import Resource


class User(Resource):
    model = db.User
    permissions = {
        'CREATE': permissions.ANY,
        'UPDATE': permissions.AUTHORIZED
    }
