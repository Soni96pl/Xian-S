from xians import api
from xians.controllers import city, user, favorite, trip

api.add_resource(city.City, '/cities/<int:_id>', endpoint='city_id')
api.add_resource(city.City, '/cities/<string:name>', endpoint='city_name')


api.add_resource(user.User, '/users')


api.add_resource(favorite.Favorites, '/favorites', endpoint='favorites')
api.add_resource(favorite.Favorites,
                 '/favorites/<int:city_id>',
                 endpoint='favorites_city_id')


api.add_resource(trip.Trip, '/trips', endpoint='trips')
