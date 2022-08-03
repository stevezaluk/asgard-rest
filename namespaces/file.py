from tokenize import Name
from flask import g, abort
from flask_restx import Namespace, Resource

from asgard_sdk.format.print import print_info

file_namespace = Namespace("file", "Metadata retrieval")

@file_namespace.route("/file/<query>", methods=['GET'])
@file_namespace.route("/file/<section_name>/<query>", methods=['GET'])
@file_namespace.route("/file/<section_name>", methods=['POST'])
class File(Resource):
    
    def get(self, query, section_name=None):
        pass

    def post(self, section_name=None):
        pass

@file_namespace.route("/index", methods=['GET'])
@file_namespace.route("/index/<section_name>", methods=['GET'])
class Index(Resource):

    def get(self, section_name=None):
        pass

@file_namespace.route("/search", methods=["GET"])
@file_namespace.route("/search/<section_name>", methods=['GET'])
class Search(Resource):

    def get(self, section_name=None):
        pass