from os import getcwd

from flask import Flask
from flask_restx import Api

from asgard_sdk.models.config import Config

from .namespaces.file import file_namespace
from .namespaces.analytics import analytics_namespace
from .namespaces.ux import ux_namespace

from .context import teardown_server

HTML_PATH = "{}/web-assets/www".format(getcwd())

class Rest(object):
    def __init__(self, config_path:str, debug=False):
        self.config_path = config_path
        self.debug = debug

        self.api_prefix = "/api/v1"
        self.stats_prefix = "/api/analytics"
        self.ux_prefix = "/dashboard"

        self._app = Flask(__name__, template_folder=HTML_PATH)
        self._api = Api(app=self._app, doc=self.ux_prefix + "/docs")
        self._config = self.load_config()

    def get_config(self):
        return self._config

    def load_config(self):
        config = Config(self.config_path)
        config.validate_structure()
        
        self._app.config["config"] = config

        return config

    def _register_teardowns(self):
        self._app.teardown_appcontext(teardown_server)

    def _build_namespaces(self):
        self._api.add_namespace(file_namespace, path=self.api_prefix)
        self._api.add_namespace(analytics_namespace, path=self.stats_prefix)
        self._api.add_namespace(ux_namespace, path=self.ux_prefix)

    def run(self):
        self._register_teardowns()
        self._build_namespaces()
        self._app.run(debug=self.debug, port=8080)