#!/usr/bin/python3
"""
Task 03 - Simple HTTP Server using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Handle GET requests with basic routing."""

        # Root endpoint: simple message
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
            return

        # /data endpoint: return JSON
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
            return

        # /status endpoint
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
            return

        # /info endpoint (optional per expected output)
        elif self.path == "/info":
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(info).encode("utf-8"))
            return

        # If endpoint is undefined → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_msg = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_msg).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """Start the HTTP server"""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server at http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
