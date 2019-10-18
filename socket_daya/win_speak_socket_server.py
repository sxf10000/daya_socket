#windows聊天室


import socket
import threading

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("localhost",9901))

sock.listen(2)
print("Server",socket.gethostbyname("localhost"),"Running")

#关于客户端信息的字典
mydict = dict()
#所有的client的socket。
mylist =list()

#写数据的函数,有客户端进入聊天--其他客户端发送出来的聊天数据
def tellOthers(exceptNum,whatTosay):
    #exceptNum 标志除了自己，whatTosay--要发送的信息
    for dy in mylist:
        if dy.fileno() !=exceptNum:
            try:
                dy.send(whatTosay.encode())
            except:
                pass
#myconnection 客户端的socket，connNumber=fileno
def subThreadIn(myconnection,connNumber): #这是一个转发器
    #有可能是客户端的聊天，如果新客户端，客户端自己定义的名字
    nickname = myconnection.recv(2048).decode()
    mydict[myconnection.fileno()] = nickname
    # socket-->张三
    #把这个client放入服务器的client列表
    mylist.append(myconnection)
    print("connetion",connNumber,"has sucsess",nickname)
    #告诉服务器client连接正常
    tellOthers(connNumber,"【提示："+mydict[connNumber]+"进入聊天室】")
    #通知所有的client，有新人进来了
    while True:
        try:
            recvMSG=myconnection.recv(2048).decode()
            #尝试获取客户端发送的信息
            if recvMSG:
                #有正常的聊天数据
                print(mydict[connNumber],":",recvMSG)
                #在服务器显示
                tellOthers(connNumber,mydict[myconnection.fileno()]+":"+recvMSG)
                #发送给所有用户
        except(OSError,ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(mydict[myconnection.fileno()],"exit",len(mylist),"left")
            #告诉服务器有人离开
            tellOthers(connNumber,"【提示："+mydict[connNumber]+"离开】")
            #告诉所有人有人离开
            myconnection.close()
            #关闭client的socket
            return

while True:
    connection,addr =sock.accept()
    # 获取和客户端的连接
    print("Accept a new Connnection",connection.getsockname(),connection.fileno())
    try:
        buf =connection.recv(2048).decode()
        #接收客户端的数据
        if buf=="2":
            connection.send(b"welcome you to my server")
            # 发送给客户端连接正确信息
            mythread = threading.Thread(target=subThreadIn,args=(connection,connection.fileno()))
            #用来开启转发的程序
            mythread.setDaemon(True)
            #设置为守护线程
            mythread.start()
        else:
            connection.send(b"please go out")
            #连接异常，关闭socket
            connection.close()
    except:
        pass





































