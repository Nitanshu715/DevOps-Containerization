from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Backend Server on Port 3000!")

server = HTTPServer(("127.0.0.1", 3000), Handler)
print("Server running on port 3000...")
server.serve_forever()