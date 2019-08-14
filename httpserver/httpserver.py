from AppPage import *
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = 'localhost'
PORT = 9000


class LocalHandler(BaseHTTPRequestHandler):
    
    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        content = self.page.html()
        return bytes(content, 'UTF-8')

    def respond(self, opts):
        ######################################################
        # here you can add more pages
        ######################################################
        if (self.path) == "/app":
            self.page = AppPage()
        else:
            self.page = WebPage()

        response = self.handle_http(opts["status"], self.path)
        self.wfile.write(response)

    def do_GET(self):
        self.respond({"status": 500})

    

if __name__ == "__main__":
    srv = HTTPServer
    httpd = srv((HOST, PORT), LocalHandler)
    try:
        print("serving at {}:{}".format(HOST, PORT))
        httpd.serve_forever()
    except:
        pass
    httpd.server_close()
