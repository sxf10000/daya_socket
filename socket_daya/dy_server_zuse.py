import socket

POST=''
PORT = 50001
so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
so.bind((POST,PORT))
so.listen(2)
so.setblocking(1)
con,addr = so.accept()

print "Conneted by:",addr

while 1:
    data = con.recv(1024)
    if not data:break
    print "Recv ",data

    con.sendall(data)
con.close()