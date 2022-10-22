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

@analytics_namespace.route("/popular", methods=["GET"])
class Popular(Resource):

    @get_server
    def get(self):
        popular = g.server.get_popular(to_dict=True)

        if popular is None:
            print_error("Failed to find popular files")
            abort(404)

        return popular

@analytics_namespace.route("/feature", methods=["GET"])
class FeatureFile(Resource):
    def get(self):
        feature = g.server.get_feature_file(to_dict=True)

        if feature is None:
            print_error("Server has no feature file")
            abort(404)

        return feature

@analytics_namespace.route("/favorites", methods=["GET"])
class Favorites(Resource):

    def get(self):
        favorites = g.server.get_favorites(to_dict=True)

        if favorites is None:
            print_error("Server has no favorite files")
            abort(404)

        return favorites

@analytics_namespace.route("/recently_uploaded", methods=["GET"])
class RecentlyUploaded(Resource):

    def get(self):
        recently_uploaded = g.server.get_recently_uploaded(to_dict=True)

        if recently_uploaded is None:
            print_error("Failed to find recently uploaded files")
            abort(404)

        return recently_uploaded

@analytics_namespace.route("/recently_downloaded", methods=["GET"])
class RecentlyDownloaded(Resource):

    def get(self):
        recently_downloaded = g.server.get_recently_uploaded(to_dict=True)

        if recently_downloaded is None:
            print_error("Failed to find recently uploaded files")
            abort(404)

        return recently_downloaded