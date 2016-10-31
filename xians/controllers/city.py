from datetime import datetime

import pymongo
import xiandb as db

from xians.resource import Resource
from xians.crawlers import wikitravel


class City(Resource):
    default_fields = ['_id', 'name', 'coordinates', 'country']
    default_sort = [('population', pymongo.DESCENDING)]

    def process(self, city):
        if 'story' in city.keys():
            if (datetime.today() - city['story']['updated']).days > 7:
                wikitravel.story(city['_id'])
                city['story']['existing'] = True
                city['story']['updating'] = True
            else:
                city['story']['updating'] = False

        return city

    def get(self, _id=None, name=None):
        fields, sort = self.get_query()

        return map(
            self.process,
            db.City.search(_id, name, fields=fields, sort=sort)
        )
