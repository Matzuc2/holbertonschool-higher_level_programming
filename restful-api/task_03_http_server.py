#!/usr/bin/python3
"""
A simple HTTP server that handles GET requests and serves JSON/text responses.

This script creates an HTTP server using Python's built-in http.server module.
It defines a few predefined endpoints that return either JSON or plain text
responses.

Endpoints:
    - "/"       : Returns a simple welcome message.
    - "/data"   : Returns a JSON object with sample user details.
    - "/info"   : Returns JSON containing API version information.
    - Other     : Returns a 400 error for unknown endpoints.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Server configuration
hostName = "localhost"
serverPort = 8000

# Sample data for responses
dict1 = {
    "Name": "John",
    "age": "30",
    "city": "New-York"
}

info1 = {
    "version": "1.0",
    "description": "A simple API built with http.server"
}


class MyServer(BaseHTTPRequestHandler):
    """
    A custom HTTP request handler to process GET requests.

    This class defines behavior for various API endpoints and sends
    appropriate responses based on the request path.
    """

    def do_GET(self):
        """
        Handles GET requests and returns appropriate responses.

        Endpoints:
            - "/data": Returns JSON containing sample user details.
            - "/": Returns a simple plain text welcome message.
            - "/info": Returns JSON with API version details.
            - Other: Returns a 400 error for unknown endpoints.

        Returns:
            None
        """
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(dict1), "utf-8"))

        elif self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps(info1), "utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Endpoint not found", "utf-8"))


if __name__ == "__main__":
    """
    Starts the HTTP server and listens for incoming requests.

    The server runs indefinitely until interrupted with a keyboard signal.
    """
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
