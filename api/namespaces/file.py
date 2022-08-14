from flask import g, abort
from flask_restx import Namespace, Resource

from asgard_sdk.format.print import print_info, print_error

from ..context import get_server

file_namespace = Namespace("file", "Metadata retrieval")

@file_namespace.route("/section", methods=["GET", "POST"])
@file_namespace.route("/section/<section_name>", methods=["GET"])
class Section(Resource):
    
    @get_server
    def get(self, section_name=None):
        if section_name is None:
            section = g.server.get_sections(to_dict=True)
            ret = {"sections":section, "total_count":len(section)}

            return ret
        else:
            section = g.server.get_section(section_name, to_dict=True)

            if section is None:
                print_error("Failed to find section: ", section_name)
                abort(404)

            return section

    @get_server
    def post(self):
        pass

@file_namespace.route("/file/<query>", methods=['GET'])
@file_namespace.route("/file/<section_name>/<query>", methods=['GET'])
@file_namespace.route("/file/<section_name>", methods=['POST'])
class File(Resource):
    
    @get_server
    def get(self, query, section_name=None):
        file = g.server.get_file(query, section_name, to_dict=True)

        if file is None: # file or section could not be found
            print_error("Failed to find file: ", query)
            abort(404)

        return file


    def post(self, section_name=None):
        pass

@file_namespace.route("/index", methods=['GET'])
@file_namespace.route("/index/<section_name>", methods=['GET'])
class Index(Resource):

    @get_server
    def get(self, section_name=None):
        index = g.server.index(section_name, to_dict=True)

        if index is None:
            print_error("Failed to find section to index: ", section_name)
            abort(404)

        ret = {"index":index, "total_count":len(index)}
        
        return ret

@file_namespace.route("/search", methods=["GET"])
@file_namespace.route("/search/<section_name>", methods=['GET'])
class Search(Resource):

    def get(self, section_name=None):
        pass