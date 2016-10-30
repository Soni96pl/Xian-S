from xians import api
from xians.controllers import city, user

api.add_resource(city.City, '/city/<int:_id>', endpoint='city_id')
api.add_resource(city.City, '/city/<string:name>', endpoint='city_name')
api.add_resource(city.CityDetails, '/city/<int:_id>/details')

api.add_resource(user.User, '/users')
