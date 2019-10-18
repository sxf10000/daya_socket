import os,socket,threading,SocketServer

SERVER_HOST='localhost'
SERVER_PORT = 0
BUFFER_SIZE = 2048

def client(ip,port,message):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((ip,port))
    try:
        sock.sendall(message)
        response = sock.recv(BUFFER_SIZE)
        print "Client recived :%s"%response
    except socket.error,e:
        print "Error:%s"%e
    finally:
        sock.close()
class ThreadTCPRequesetHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(2048)
        current_thread=threading.current_thread().getName()
        response = "%s:%s"%(current_thread,data)
        self.request.sendall(response)

class TreadedTCPServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

if __name__ == '__main__':
    server = TreadedTCPServer((SERVER_HOST,SERVER_PORT),ThreadTCPRequesetHandler)
    ip,port= server.server_address
    server_tread=threading.Thread(target=server.serve_forever)
    server_tread.daemon=True
    server_tread.start()
    print "Thread_name:%s"%server_tread.name
    client(ip,port,"Hello I am client1")
    client(ip,port,"Hello I am client2")
    client(ip,port,"Hello I am client3")
    server.shutdown()