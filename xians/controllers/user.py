from flask import make_response, request
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
        params = parser.parse_args()

        user = db.User.add(**params)

        if user:
            location = '%susers/%s' % (request.url_root, user.inserted_id)
            headers = {
                'Location': location
            }

            return {
                'success': True,
                'message': "Signed up successfully"
            }, 201, headers

        return {
            'success': False,
            'message': "User with a given name or email already exists"
        }, 409
