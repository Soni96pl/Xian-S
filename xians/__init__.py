import os

import yaml
from bson import json_util

from flask import Flask, make_response
from flask_log import Logging
from flask_restful import Api
from flask_jwt import JWT

import xiandb as db


try:
    with open(os.path.expanduser('~') + '/xian/config.yml', 'r') as cfg_file:
        cfg = yaml.load(cfg_file)
except IOError:
    print "Couldn't find a valid configuration file in ~/xian/config.xml"
    print "Please refer to README.rst"
    raise


app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)
flask_log = Logging(app)
app.cfg = cfg


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json_util.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp


def authenticate(name, password):
    user = db.User.authenticate(name, password)
    if user:
        return {'id': user['_id']}


def load_user(payload):
    user_id = payload['identity']
    return db.User.get(user_id)

app.config['SECRET_KEY'] = cfg['app']['jwt_secret']


jwt = JWT(app, authenticate, load_user)


import xians.routing
