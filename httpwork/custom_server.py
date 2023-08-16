#!/usr/bin/python3
"""Alta3 Research | rzfeeser@alta3.com
   Using http.server to create a simple HTTP server."""

# standard library
import http.server
import socketserver

def main():
    """run-time code"""

    ## port to run on
    port = 9021

    ## handler is how to respond to an event
    ## any incoming HTTP message to the root "/"
    ## will provoke a 200+HTML describing files in the directory
    ## the server was launched from        
    handler = http.server.SimpleHTTPRequestHandler

    ## build a server object that listens on all interfaces, described port and event handler        
    httpd = socketserver.TCPServer(("", port), handler)

    print(("serving at port", port))

    ## start the server until it is interrupted
    httpd.serve_forever()

if __name__ == "__main__":
    main()

