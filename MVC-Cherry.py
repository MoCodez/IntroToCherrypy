import cherrypy

class MVC_Cherry(object):
    """Main class for MVC-Cherry application.
    """
    @cherrypy.expose
    def index(self):
        """ View function for application root node.
        """
        return "Model View Cherry INDEX!"



if __name__ == "__main__":
    cherrypy.quickstart(MVC_Cherry(), '/')
    """ Starts internal httpd and listens at: http://127.0.0.1:8080/
    """

