import  socket

SEND_SIZE= 2048
RECV_SIZE= 2048

def modify_buf():
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    bufsize = sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print "Buffer size [NO CHENGE]:%d"%bufsize

    sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY,1)
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_SNDBUF,
        SEND_SIZE
    )
    sock.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_RCVBUF,
        RECV_SIZE
    )
    bufsize=sock.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print "Buffer size [after]:%d"%bufsize
if __name__ == '__main__':
    modify_buf()