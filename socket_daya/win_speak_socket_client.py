import socket,time
import threading

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(("localhost",9901))
#一连接成功就发送2数据过去
sock.send(b'2')
print(sock.recv(2048).decode())
#输出服务器返回的信息

nickName= input("input your nickname:")
sock.send(nickName.encode())
#发送一个自己定义的名字

def sendThreadFunc():
    while True:
        try:
            #从客户端的键盘输入内容
            myword = input()
            #把键盘的内容发送到服务器
            sock.send(myword.encode())
        except ConnectionAbortedError:
            print("Server closed this connectiion")
        except ConnectionResetError:
            print("Error")

def recvThreadFunc():
    while True:
        try:
            #获取其他用户发送给服务器的数据
            otherword = sock.recv(2048)
            if otherword:
                #输出到本地
                print(otherword.decode())
            else:
                pass
        except ConnectionResetError:
            print("server colsed")
        except ConnectionAbortedError as e:
            print("error :%s"%e)

th1 = threading.Thread(target=sendThreadFunc)
th2 = threading.Thread(target=recvThreadFunc)
#使用两个线程开启数据的接收和发送
threads = [th1,th2]
for th in threads:
    th.setDaemon(True)
    th.start()
th.join()