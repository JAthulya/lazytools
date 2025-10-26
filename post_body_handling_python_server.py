from http.server import BaseHTTPRequestHandler, HTTPServer

class WebHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length',0))
        post_body = self.rfile.read(content_length).decode('utf-8')
        print(post_body)
        print("---------------")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8000)
    httpd = HTTPServer(server_address, WebHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()