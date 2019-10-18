import argparse
import string
import os
import sys
import cStringIO
import gzip
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 9901
HTML_CONTENT = """<html><body><h1>Great China Go To Great Up</h1></body></html>"""

class RequestHander(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.send_header("Content-Encoding","gzip")
        zbuf=self.compress_buffer(HTML_CONTENT)
        sys.stdout.write("Content-Ecoding :gzip\r\n")
        sys.stdout.flush()
        self.send_header("Content-Length",len(zbuf))
        self.end_headers()
        zbuf = self.compress_buffer(HTML_CONTENT)
        sys.stdout.write("Content-Ecoding:gzip \r\n")
        sys.stdout.write("Content-Length :%d"%(len(zbuf)))
        sys.stdout.write('\r\n')

        self.wfile.write(zbuf)
        return
    def compress_buffer(self,buf):
        zbuf = cStringIO.StringIO()
        zfile=gzip.GzipFile(mode="wb",fileobj=zbuf,compresslevel=5)
        zfile.write(buf)
        zfile.close()
        return zbuf.getvalue()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HTTPP SERVER")
    parser.add_argument("--port",dest="port",type=int,default=DEFAULT_PORT)
    given_args=parser.parse_args()
    port = given_args.port
    server_address=(DEFAULT_HOST,port)
    server = HTTPServer(server_address,RequestHander)
    server.serve_forever()