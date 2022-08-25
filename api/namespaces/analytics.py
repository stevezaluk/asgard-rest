from flask import g, abort, current_app
from flask_restx import Namespace, Resource

from asgard_sdk.format.print import print_info, print_error

from ..context import get_server

analytics_namespace = Namespace("analytics", "Generate and fetch analytical data based on plex viewing habits")

@analytics_namespace.route("/version", methods=["GET"])
class Version(Resource):

    def get(self):
        config = current_app.config["config"]
        
        ret = {"server_name":config.server_name, "version":1.0}

        return ret