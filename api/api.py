import sys

from flask import Flask
from flask_restx import Api

from asgard_sdk.models.config import Config

class Rest(object):
    def __init__(self, config_path:str, debug=False):
        self._app = Flask(__name__)
        self._api = Api(app=self._app)

        self.debug = debug
        self.config_path = config_path

        self.config = None

    def load_config(self):
        pass

    def _register_teardowns(self):
        pass

    def _build_namespaces(self):
        pass

    def start(self):
        self._app.run(debug=self.debug)