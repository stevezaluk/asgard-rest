from flask import g, current_app
from flask import render_template, make_response
from flask_restx import Namespace, Resource

from asgard_sdk.format.print import print_info, print_error

from ..context import get_server

ux_namespace = Namespace("ux", "Holds all UX/UI related endpoints used for rendering templates")

@ux_namespace.route("/home", methods=["GET"])
class Home(Resource):
    
    # @get_server
    def get(self):
        return make_response(render_template("home.html"))

@ux_namespace.route("/sections", methods=["GET"])
class Sections(Resource):
    
    @get_server
    def get(self):
        sections = g.server.get_sections() # to_dict=True
        return make_response(render_template("sections.html", sections=sections))

@ux_namespace.route("/files", methods=["GET"])
class Files(Resource):
    
    def get(self):
        return make_response(render_template("files.html"))

@ux_namespace.route("/upload", methods=["GET"])
class Upload(Resource):
    
    def get(self):
        return make_response(render_template("upload.html"))

@ux_namespace.route("/search", methods=["GET"])
class Search(Resource):
    
    def get(self):
        return make_response(render_template("search.html"))

@ux_namespace.route("/analytics", methods=["GET"])
class Analytics(Resource):
    
    def get(self):
        return make_response(render_template("analytics.html"))

@ux_namespace.route("/docs", methods=["GET"])
class Docs(Resource):
    
    def get(self):
        return make_response(render_template("docs.html"))
