import argparse
import sys
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8800
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
         self.send_response(200)
         self.send_header("Content-Type","text/html")
         self.end_headers()
         self.wfile.write("Hello daya welcome you!!")
         return
class CustomHTTPServer(HTTPServer):
    def __init__(self,host,port):
        server_adress = (host,port)
        HTTPServer.__init__(self,server_adress,RequestHandler)

def run_server(port):
    try:
        server = CustomHTTPServer(DEFAULT_HOST,port)
        print "Custom HTTP started on %s :%s"%(DEFAULT_HOST,port)
        server.serve_forever()
    except Exception,err:
        print "Error:%s" %err
    except KeyboardInterrupt:
        print "shutting dowb"
        server.socket.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HTTP server")
    parser.add_argument("--port",dest="port",type=int ,default=DEFAULT_PORT)
    given_args = parser.parse_args()
    port = given_args.port
    run_server(port)