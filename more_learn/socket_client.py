import socket

HOST = '192.168.1.102'
PORT = 5007
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.connect((HOST,PORT))

while True:
    user_in = raw_input("msg to send").strip()
    so.sendall(user_in)
    data = so.recv(1024)
    print "Received",repr(data)
so.close()