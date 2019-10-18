import socket
import os
import  time

SERVER_PATH="/tmp/python_linux_server"
def run_linux_socket_server():
    if os.path.exists(SERVER_PATH):
        os.remove(SERVER_PATH)
    print "Starting linux socket server"
    server = socket.socket(socket.AF_UNIX,socket.SOCK_DGRAM)
    server.bind(SERVER_PATH)
    print "litening on path %s"%SERVER_PATH
    while True:
        datagram = server.recv(2048)
        if not datagram:
            break
        else:
            print "~~"*20
            print datagram

        if "ESC" == datagram:
            break
    print "~~"*20
    print "Server is shutting down"
    server.close()
    os.remove(SERVER_PATH)
if __name__ == '__main__':
    run_linux_socket_server()