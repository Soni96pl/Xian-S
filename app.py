from flask import Flask
from flask_restful import Api, Resource

import pymongo
from database import connection

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)


class CityAPI(Resource):
    def get(self, name):
        return list(connection.City.find({'name': name},
                                         sort=[('population',
                                                pymongo.DESCENDING)]))


api.add_resource(CityAPI, '/city/<string:name>', endpoint='city')
