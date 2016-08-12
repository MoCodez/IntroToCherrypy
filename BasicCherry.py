import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "Greetings from the Cherrypy application"

if __name__ == "__main__":
    cherrypy.quickstart(Root(), '/')
