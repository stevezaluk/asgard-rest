from flask import g, current_app
from flask import render_template, make_response
from flask_restx import Namespace, Resource

from asgard_sdk.format.print import print_info, print_error

from ..context import get_server

ux_namespace = Namespace("ux", "Holds all UX/UI related endpoints used for rendering templates")

@ux_namespace.route("/dashboard", methods=["GET"])
class Home(Resource):
    
    @get_server
    def get(self):
        recently_uploaded = g.server.get_recently_uploaded()
        sections = g.server.get_sections()
        return make_response(render_template("dashboard.html", sections=sections, recently_uploaded=recently_uploaded))

@ux_namespace.route("/view_file/<hash>", methods=["GET"])
class ViewFile(Resource):

    @get_server
    def get(self, hash):
        file = g.server.get_file(hash)
        return make_response(render_template("pages/view_file.html", file=file))

@ux_namespace.route("/sections", methods=["GET"])
class Sections(Resource):
    
    @get_server
    def get(self):
        sections = g.server.get_sections() # to_dict=True
        return make_response(render_template("pages/sections.html", sections=sections))

@ux_namespace.route("/view_section/<section_name>", methods=["GET"])
class ViewSection(Resource):
    @get_server
    def get(self, section_name):
        section = g.server.get_section(section_name)
        return make_response(render_template("pages/view_section.html", section=section))

