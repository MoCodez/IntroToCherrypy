""" This is tutorial code and is meant to illustrate:
    creating a cherrypy class
    creating a cherrypy view for the default URL of /
    creating a test harness for testing the app from a shell CLI
"""

import cherrypy


class Root(object):
    """ This implements our application class
    """
    @cherrypy.expose
    def index(self):
        """ This is a simple MVC view without parameters from a model
        or control from a URL mapping, yet.
        """
        return "Warning!<br/> Core Meltdown Imminent!"



if __name__ == "__main__":
    """ This section is used to test and develop our application by
    simply running it on the command line. Once it is finieshed, the
    goal is to deploy our code as a Python module on a cloud server
    like Heroku.
    """
    cherrypy.quickstart(Root(), '/')
    """ This call starts the internal httpd and attaches our class to the
    server at: http://127.0.0.1:8080/
    """

