import socket,sys

def reuse_socket():
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    old_sta= sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)
    print "Old sock:%d"%old_sta

    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    new_sta = sock.getsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR)

    print "New sock:%d"%new_sta

    local_port = 9901
    srv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # srv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    srv.bind(("",local_port))
    srv.listen(2)
    print "port:%s"%local_port

    while True:
        try:
            connect,addr = srv.accept()
            print "Connected by :%s:%s"%(addr[0],addr[1])
        except KeyboardInterrupt:
            break
        except socket.error,msg:
            print "%s"%msg

if __name__ == '__main__':
    reuse_socket()