import sys

from flask import Flask
from flask_restx import Api

from asgard_sdk.models.config import Config

class Rest(object):
    def __init__(self, config_path:str, debug=False):
        self.config_path = config_path
        self.debug = debug

        self.endpoint_prefix = "/v1/api"

        self._config = self.load_config()
        self._app = Flask(__name__)
        self._api = Api(app=self._app)

    def get_config(self):
        return self._config

    def load_config(self):
        config = Config(self.config_path)
        config.validate_structure()
        
        values = config.values
        for key in values:
            value = values[key]
            self._app.config[key] = value

        return config

    def _register_teardowns(self):
        pass

    def _build_namespaces(self):
        pass
    
    def run(self):
        self._app.run(debug=self.debug)