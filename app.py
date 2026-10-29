from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(
            b"Hello! My first DevOps application is running in Docker."
        )

server = HTTPServer(("0.0.0.0", 5000), Handler)
print("Application running on port 5000")
server.serve_forever()
