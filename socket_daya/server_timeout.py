import argparse
import socket
import errno
from time import time as now

DEFAULT_TIMEOUT=120
DEFAULT_SERVER_HOST = "localhost"
DEFAULT_PORT = 80

class ServiceChecker(object):
    def __init__(self,host,port,timeout=DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    def end_wait(self):
        self.sock.close()
    def check(self):
        if self.timeout:
            end_time = now()+self.timeout
            #119002+20 = 119022
        while True:
            try:
                if self.timeout:
                    #119004+20 119024  118
                    next_timeout=end_time-now()
                    if next_timeout<0:
                        return False
                    else:
                        print "setting socket next timeout %s"%round(next_timeout)
                        self.sock.settimeout(next_timeout)
                self.sock.connect((self.host,self.port))
            except socket.timeout,err:
                if self.timeout:
                    return False
            except socket.error,err:
                print "Exception %s" %err
            else:
                self.end_wait()
                return True
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Wait service")
    parser.add_argument("--host",dest="host",default=DEFAULT_SERVER_HOST)
    parser.add_argument("--port",dest="port",type=int,default=DEFAULT_PORT)
    parser.add_argument("--timeout",dest="timeout",type=int,default=DEFAULT_TIMEOUT)
    given_args = parser.parse_args()
    host,port,timeout = given_args.host,given_args.port,given_args.timeout
    service_checker = ServiceChecker(host,port,timeout)
    print "Checking network service %s:%s"%(host,port)
    if service_checker.check():
        print "Service is available again!"