import socket
import time
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5550))
#向服务器发送1
sock.send(b'1')
print(sock.recv(1024).decode())
#接收服务器返回的消息，打印出来
nickName = input('input your nickname: ')
sock.send(nickName.encode())
#向server注册一个名字
def sendThreadFunc():
    while True:
        try:
            myword = input()
            sock.send(myword.encode())
            #发送数据出去
            # print(sock.recv(1024).decode())
        except ConnectionAbortedError:
            print('Server closed this connection!')
        except ConnectionResetError:
            print('Server is closed!')
def recvThreadFunc():
    while True:
        try:
            otherword = sock.recv(1024)
            #接收其他用户发送的数据
            if otherword:
                print(otherword.decode())
            else:
                pass
        except ConnectionAbortedError:
            print('Server closed this connection!')

        except ConnectionResetError:
            print('Server is closed!')
th1 = threading.Thread(target=sendThreadFunc)
th2 = threading.Thread(target=recvThreadFunc)
threads = [th1, th2]
#开启发送和接收两个线程
for t in threads:
    t.setDaemon(True)
    t.start()
t.join()