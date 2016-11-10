from flask import request
from flask_restful import reqparse, Resource

import xiandb as db


class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help="Name is required!")
        parser.add_argument('password', type=str, required=True,
                            help="Password is required!")
        parser.add_argument('email', type=str, required=True,
                            help="Email is required!")
        user = parser.parse_args()

        headers = {}

        user_id = db.User.add(user)
        success = user_id is not False

        if success:
            headers['Location'] = '%susers/%s' % (request.url_root, user_id)
            message = "Signed up successfully"
            code = 201
        else:
            message = "User with a given name or email already exists"
            code = 409

        return {'success': success, 'message': message}, code, headers
