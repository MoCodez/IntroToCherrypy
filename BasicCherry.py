
import cherrypy


class Root(object):
    """Main class for BasicCherry application.
    """
    @cherrypy.expose
    def index(self):
        """ View function for application root node.
        """
        return "Warning!<br/> Core Meltdown Imminent!"

if __name__ == "__main__":
    cherrypy.quickstart(Root(), '/')
    """ Starts internal httpd and listens at: http://127.0.0.1:8080/
    """

