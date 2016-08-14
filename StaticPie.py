""" Tutorial on setting up a CRUD interface to a Cherrypy web server
"""
""" Serving a GD static page with this system is IDIOTICALLY COMPLEX WTF!"""

import os
import cherrypy

class StaticPages(object):
    """ This class implements our static page service
    """
    @cherrypy.expose
    def index(self):
        """ This class maps the root of the server to our static_pages/index.html
        """
        return open("index.html")

    @cherrypy.expose
    def about(self):
        """ This function maps /about to static_pages/about.html
        """
        return open("about.html")



if __name__ == "__main__":
    server_config = {
        '/': {
            "tools.staticdir.root": os.path.abspath(os.getcwd())
        },
        "/static": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": "./static_pages"
            }
        }
    cherrypy.quickstart(StaticPages(), '/', server_config)
