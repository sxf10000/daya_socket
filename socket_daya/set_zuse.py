import socket
def socket_modes():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setblocking(1)
    sock.settimeout(0.5)
    sock.bind(("127.0.0.1",0))
    socket_address = sock.getsockname()
    print "socket :%s" %str(socket_address)
    while 1:
        sock.listen(2)
if __name__ == '__main__':
    socket_modes()