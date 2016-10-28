from flask_restful import reqparse, Resource
from flask_jwt import jwt_required, current_identity

import xiandb as db


class UserSignup(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True,
                            help="Name is required!")
        parser.add_argument('password', type=str, required=True,
                            help="Password is required!")
        parser.add_argument('email', type=str, required=True,
                            help="Email is required!")
        params = parser.parse_args()

        if not db.User.signup(**params):
            return {
                'success': False,
                'message': "User with a given name or password already exists"
            }
        return {'success': True, 'message': "Signed up successfully"}
