from flask import g, current_app

from asgard_sdk.format.print import print_info
from asgard_sdk.server.server import AsgardServer

def get_server(func):
    def inner(*args, **kwargs):
        if "server" not in g:
            config = current_app.config["config"]
            g.server = AsgardServer(config)
            g.server.connect()
            
            print_info("Connected to database")
            ret = func(*args, **kwargs)
        return ret
    return inner

def teardown_server(exception):
    server = g.pop("server", None)

    if server is not None:
        print_info("Disconnecting from database")
        server.disconnect()