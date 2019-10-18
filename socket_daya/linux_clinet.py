import socket
import sys
SERVER_PATH="/tmp/python_linux_server"
def run_linux_socket_client():
    sock = socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)
    server_adress = SERVER_PATH
    print "connecting to %s"%server_adress
    try:
        sock.connect(server_adress)
    except socket.error,msg:
        print "error :%s" % msg
        sys.exit(1)
    try:
        message = "This is linux socket client"
        print "%s"%message
        sock.sendall(message)
        amount_received = 0
        amount_excepted = len(message)
        while amount_received<amount_excepted:
              data = sock.recv(512)
              amount_received +=len(data)
              print "Received [%s]"%data
    finally:
        print "Closeing client"
        sock.close()
if __name__ == '__main__':
    run_linux_socket_client()