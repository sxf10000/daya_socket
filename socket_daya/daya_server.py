import socket,sys,argparse

host = "localhost"
data_payload = 2048
backlog = 5

def  daya_server(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_host = (host,port)
    print "server on %s port %s"%server_host
    sock.bind(server_host)

    sock.listen(backlog)
    while True:
        print "Waiting to receive from client"
        client,address= sock.accept()
        data = client.recv(2048)
        if data:
            print "Data :%s"%data
            client.send(data)
            print "send %s bytes back  to %s"%(data,address)
        client.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Socket Set:")
    parser.add_argument("--port",dest="port",type=int)
    given_arg = parser.parse_args()
    port  = given_arg.port
    daya_server(port)