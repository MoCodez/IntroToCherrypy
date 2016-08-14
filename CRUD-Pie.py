""" Tutorial on setting up a CRUD interface to a Cherrypy web server
"""
import os
import cherrypy

class CRUD(object):
    @cherrypy.expose
    def index(self):
        return open("index.html")

    @cherrypy.expose
    def about(self):
        return open("about.html")


class CRUD_WebService(object):
    exposed = True

    def GET(self):
        return "GET Method"

    def POST(self, length):
        return "POST Method"

    def PUT(self):
        return "PUT Method"

    def DELETE(self):
        return "DELETE Method"

if __name__ == "__main__":
    server_config = {
        '/' : {
            "tools.staticdir.root": True
            },
        "/static" : {
            "tools.staticdir.on": True,
            "tools.staticdir": "./static_pages"
            }
        }
    webapp = CRUD()
    webapp.generator = CRUD_WebService()
    cherrypy.quickstart(webapp, '/', server_config)
