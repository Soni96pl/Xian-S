from flask_restful import reqparse, Resource
from flask_jwt import jwt_required, current_identity


class FavoriteAdd(Resource):
    decorators = [jwt_required()]

    def put(self, city_id):
        success = current_identity.add_favorite(city_id)
        if success:
            message = "Added a favorite successfully"
        else:
            message = "This city is already a favorite"

        current_identity.save()
        return {'success': success, 'message': message}
