from datetime import datetime

import pymongo
import xiandb as db

from xians import permissions
from xians.resource import Resource
from xians.crawlers import wikitravel


class City(Resource):
    model = db.City
    permissions = {
        'READ': permissions.ANY
    }
    default_fields = ['_id', 'name', 'coordinates', 'country']
    default_sort = [('population', pymongo.DESCENDING)]

    def get(self, path=None, **match):
        fields, sort = self.get_query()
        ret = super(City, self).get(path, **match)

        if '_id' in match and 'story' in ret:
            if (datetime.today() - ret['story']['updated']).days > 7:
                wikitravel.story(ret['_id'])
                ret['story']['updating'] = True
            else:
                ret['story']['updating'] = False

        return ret
