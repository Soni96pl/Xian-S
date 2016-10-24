from flask import Flask
from flask_log import Logging
from flask_restful import Api

app = Flask(__name__)
app.config.from_pyfile('app.cfg')
api = Api(app)
flask_log = Logging(app)

from xians.controllers import routing
