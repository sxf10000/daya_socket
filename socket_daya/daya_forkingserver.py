import os,socket,threading,SocketServer

SERVER_HOST='localhost'
SERVER_PORT = 0
BUFFER_SIZE = 2048
MSG ="Hello server!"

class ForkingClient():
    def __init__(self,ip,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.connect((ip,port))

    def run(self):
        current_id = os.getpid()
        print "PID %s send message to server:%s"%(current_id,MSG)
        send_data = self.sock.send(MSG)
        print "Send:%d char"%send_data
        reponse = self.sock.recv(BUFFER_SIZE)
        print "PID %s recived:%s"%(current_id,reponse[5:])
    def shutdowd(self):
        self.sock.close()

class ForkingServerRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(BUFFER_SIZE)
        current_id = os.getpid()
        response = "%s:%s"%(current_id,data)
        print "Sver sending [current_id:data]:%s"%response
        self.request.send(response)
        return
class ForkingServer(SocketServer.ForkingMixIn,SocketServer.TCPServer,):
    pass

def main():
    server = ForkingServer((SERVER_HOST,SERVER_PORT),ForkingServerRequestHandler)
    ip,port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print "server loop PID:%s"%os.getpid()
    client1 = ForkingClient(ip,port)
    client1.run()
    client2 = ForkingClient(ip,port)
    client2.run()
    server.shutdown()
    client1.shutdowd()
    client2.shutdowd()
    server.socket.close()

if __name__ == '__main__':
    main()