import cherrypy

class Root(object):
    """Main class for BasicCherry application.
    """
    @cherrypy.expose
    def index(self):
<<<<<<< HEAD
        """ View function for application root node.
        """
        return "Warning!<br/> Core Meltdown Imminent!"

=======
        return "Greetings from the Cherrypy application"
>>>>>>> bb753a316a00bb5ff3ca2f2af9d07045b68ef1a6

if __name__ == "__main__":
    cherrypy.quickstart(Root(), '/')
    """ Starts internal httpd and listens at: http://127.0.0.1:8080/
    """

