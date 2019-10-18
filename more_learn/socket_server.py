import socket

HOST = ''

PORT = 5007

so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
so.setblocking(0)
so.bind((HOST,PORT))
so.listen(1)
while 1:
        conn, addr = so.accept()
        print "Connected by", addr
        conn.setblocking(0)
        data = conn.recv(1024)
        if not data:break
        print "recv:",data
        conn.sendall(data)
conn.close()
