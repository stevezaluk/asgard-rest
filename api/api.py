import sys

from flask import Flask
from flask_restx import Api

class Rest(object):
    def __init__(self, debug=False):
        self._app = Flask(__name__)
        self._api = Api(app=self._app)

        self.debug = debug