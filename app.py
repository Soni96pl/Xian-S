from datetime import datetime

from flask import Flask
from flask_restful import Api, Resource

import pymongo
import xiandb as db
import xianc as c

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)


wikitravel = c.Wikitravel()


class City(Resource):
    def get(self, name=None, _id=None):
        if _id:
            params = {
                '$match': {'_id': _id},
                'isPerfect': 1
            }
        elif name:
            params = {
                '$match': {'$or': [
                    {'name': name}, {'alternate_names': name.lower()}
                ]},
                'isPerfect': {'$eq': ['$name', name]}
            }

        return map(self.process, db.City.aggregate([
            {'$match': params['$match']},
            {'$project': {
                'name': 1,
                'coordinates': 1,
                'country': 1,
                'population': 1,
                'isPerfect': params['isPerfect']
            }},
            {'$sort': {
                'isPerfect': pymongo.DESCENDING,
                'population': pymongo.DESCENDING
            }}
        ]))

    def process(self, city):
        return {
            'id': city['_id'],
            'name': city['name'],
            'coordinates': city['coordinates'],
            'country': city['country']
        }


class CityDetails(Resource):
    def get(self, _id):
        return map(self.process, db.City.aggregate([
            {'$match': {'_id': _id}},
            {'$project': {
                'name': 1,
                'coordinates': 1,
                'country': 1,
                'population': 1,
                'story': 1
            }},
            {'$limit': 1}
        ]))

    def process(self, city):
        if (datetime.today() - city['story']['updated']).days > 7:
            story = {'status': 'updating', 'content': city['story']['content']}
            wikitravel.story(city['_id'])
        elif city['story']['existing']:
            story = {'status': 'existing', 'content': city['story']['content']}
        else:
            story = {'status': 'nonexisting'}

        return {
            'id': city['_id'],
            'name': city['name'],
            'coordinates': city['coordinates'],
            'country': city['country'],
            'story': story
        }


api.add_resource(City, '/city/<int:_id>', endpoint='city_id')
api.add_resource(City, '/city/<string:name>', endpoint='city_name')
api.add_resource(CityDetails, '/city/<int:_id>/details')
