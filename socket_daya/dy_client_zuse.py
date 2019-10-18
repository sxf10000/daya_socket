import socket
HOST = '192.168.1.102'
PORT= 50001

so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((HOST,PORT))

while True:
    user_input= raw_input("msg to server:").strip()
    so.sendall(user_input)
    data = so.recv(1024)
    print "Riceived:",repr(data)
so.close()