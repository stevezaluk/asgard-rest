from flask import g, abort, request
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
        section = None
        
        if section_name:
            print("Fetching section")
            section = g.server.get_section(section_name)
            
            if section is None:
                print_error("Failed to find section: ", section_name)
                abort(404)
        
        file = g.server.get_file(query, section, to_dict=True)

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
        section = None
        
        if section_name:
            section = g.server.get_section(section_name)
            
            if section is None:
                print_error("Failed to find section: ", section_name)
                abort(404)

        index = g.server.index(section, to_dict=True)

        ret = {"index":index, "total_count":len(index)}
        
        return ret

@file_namespace.route("/search", methods=["GET"])
@file_namespace.route("/search/<section_name>", methods=['GET'])
class Search(Resource):

    @get_server
    def get(self, section_name=None):
        args = request.args

        if "q" not in args:
            print_error("Missing 'q' query string arg")
            abort(400)

        section = None
        
        if section_name:
            section = g.server.get_section(section_name)

            if section is None:
                print_error("Failed to find section: ", section_name)
                abort(404)

        file_name = args.get("q")
        search = g.server.search(file_name=file_name, section=section, to_dict=True)

        ret = {"search":search, "total_count":len(search)}
        return ret
