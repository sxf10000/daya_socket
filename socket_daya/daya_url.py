import argparse
import httplib
import re
import urllib
import urlparse

DEFAULT_URL= "http://www.python.org/"
HTTP_RIGHT_CODES=[httplib.OK,httplib.MOVED_PERMANENTLY,httplib.FOUND]

def get_server_status_code(url):
    host ,path =urlparse.urlparse(url)[1:3]
    try:
        conn=httplib.HTTPConnection(host)
        conn.request("HEAD",path)
        return conn.getresponse().status
    except StandardError:
        return None
if __name__ == '__main__':
    parser= argparse.ArgumentParser(description="HEAD check")
    parser.add_argument("--url",dest="url",default=DEFAULT_URL)
    given_args=parser.parse_args()
    url = given_args.url
    if get_server_status_code(url) in HTTP_RIGHT_CODES:
        print "Server : %s is Worked"%url
    else:
        print "Server :%s is Stoped"%url