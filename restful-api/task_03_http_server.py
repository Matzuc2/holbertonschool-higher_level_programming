#!/usr/bin/python3
"""
A simple HTTP server that serves JSON and plain text responses.

This script creates an HTTP server using Python's built-in http.server
module. It defines several endpoints that return either JSON or plain
text responses.

Endpoints:
    - "/": Returns a welcome message.
    - "/data": Returns a JSON object with user details.
    - "/info": Returns version information about the API.
    - "/status": Returns a status message indicating the server is operational.
    - Other: Returns a 404 error for unknown endpoints.
"""

from http.server import BaseHTTPRequestHandler
import json
import socketserver


class MyServer(BaseHTTPRequestHandler):
    """
    Custom HTTP request handler that processes GET requests.

    This class defines the behavior of the server for different endpoints
    and generates appropriate responses based on the request path.
    """

    def do_GET(self):
        """
        Handles GET requests for various endpoints.

        Depending on the requested path, the server responds with:
            - 200 OK and a welcome message for "/".
            - 200 OK and user data for "/data".
            - 200 OK and version info for "/info".
            - 200 OK and a status message for "/status".
            - 404 Not Found for any other endpoint.

        Returns:
            None
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            dict1 = {
                        "name": "John",
                        "age": 30,
                        "city": "New York"
                    }
            self.end_headers()
            self.wfile.write(json.dumps(dict1).encode("utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


PORT = 8000

Handler = MyServer
if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
