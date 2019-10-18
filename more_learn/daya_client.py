import select
import socket
import sys
import signal
import cPickle
import struct
import argparse
from daya_server import ChatServer
SERVER_HOST = 'localhost'
CHAT_SERVER_NAME = 'server'
# Some utilities
def send(channel, *args):
   buffer = cPickle.dumps(args)
   value = socket.htonl(len(buffer))
   size = struct.pack("L",value)
   channel.send(size)
   channel.send(buffer)
def receive(channel):
   size = struct.calcsize("L")
   size = channel.recv(size)
   try:
      size = socket.ntohl(struct.unpack("L", size)[0])
   except struct.error, e:
      return ''
   buf = ""
   while len(buf) < size:
      buf = channel.recv(size - len(buf))
   return cPickle.loads(buf)[0]
class ChatClient(object):
    """ A command line chat client using select """
    def __init__(self, name, port, host=SERVER_HOST):
        self.name = name
        self.connected = False
        self.host = host
        self.port = port
        # Initial prompt
        self.prompt='[' + '@'.join((name, socket.gethostname().split('.')[0])) + ']> '
        # Connect to server at port
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((host, self.port))
            print "Now connected to chat server@ port %d" % self.port
            self.connected = True
            # Send my name...
            send(self.sock,'NAME: ' + self.name)
            data = receive(self.sock)
            # Contains client address, set it
            addr = data.split('CLIENT: ')[1]
            self.prompt = '[' + '@'.join((self.name, addr)) + ']> '
        except socket.error, e:
            print "Failed to connect to chat server @ port %d" % self.port
            sys.exit(1)
    def run(self):
        """ Chat client main loop """
        while self.connected:
            try:
                sys.stdout.write(self.prompt)
                sys.stdout.flush()
                # Wait for input from stdin and socket
                readable, writeable,exceptional = select.select([0, self.sock], [],[])
                for sock in readable:
                    if sock == 0:
                        data = sys.stdin.readline().strip()
                        if data: send(self.sock, data)
                    elif sock == self.sock:
                        data = receive(self.sock)
                        if not data:
                            print 'Client shutting down.'
                            self.connected = False
                            break
                        else:
                            sys.stdout.write(data + '\n')
                            sys.stdout.flush()
            except KeyboardInterrupt:
                print " Client interrupted. """
                self.sock.close()
                break
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Socket Server Example with Select')
    parser.add_argument('--name', action="store", dest="name", required=True)
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    name = given_args.name
    if name == CHAT_SERVER_NAME:
        server = ChatServer(port)
        server.run()
    else:
        client = ChatClient(name=name, port=port)
        client.run()