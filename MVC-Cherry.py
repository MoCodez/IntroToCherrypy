""" This is a MINIMAL implementation of an MVC using Cherrypy
"""

import cherrypy


class MVC_Cherry(object):
    """Main class for MVC-Cherry application.
    """
    # Controller
    # In this simple example the function name maps to the 
    # path_specification on http://127.0.0.1:8080/Fibopage?fidx=[INTEGER]
    @cherrypy.expose
    def Fibopage(self, fidx=1):
        """ This is our View function and URL Controller for the FibonacciFunction() Model.
        """
        # Viewer
        # This code inplements the view of the Model which is simply its value(fidx).
        fidx = int(fidx) # cast URL string to int...
        if (fidx > 100): return "Error: Use a value < 100"
        if (fidx < 0): return "Error: Input value must be >= 0"
        return str(FibonacciModel(fidx))


# Fibonacci Series: Pythonized sequencer
# Implementation (c) 2016 Brig Young (github.com/Sonophoto)
# License: BSD-2c, i.e. Cite.
def FibonacciModel(N):
    """ This is the Model for our MVC, given any valid input it returns
    the fibonacci number for that input. Returns f(N) per:www.oeis.org/
    """
    if (N < 0): return -1     # Invalid range.
    fibp, fib = 0, 1
    if (N == fibp): return (fibp)
    while(N > 1): 
        N, fibp, fib = (N - 1), fib, (fibp + fib) 
    return (fib)


if __name__ == "__main__":
    cherrypy.quickstart(MVC_Cherry(), '/')
    """ Starts internal httpd and listens at: http://127.0.0.1:8080
    """

