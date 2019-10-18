import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5550))
sock.listen(5)
print('Server', socket.gethostbyname('localhost'), 'listening ...')
#存放编号和主机的键值对
mydict = dict()
#存放所有的用户列表
mylist = list()
# 把whatToSay传给除了exceptNum的所有人
def tellOthers(exceptNum, whatToSay):
    for c in mylist:
        #如果发送除了自己之外的所有人
        if c.fileno() != exceptNum:
            try:
                c.send(whatToSay.encode())
            except:
                pass
def subThreadIn(myconnection, connNumber):
    #接收发送过来的数据
    nickname = myconnection.recv(1024).decode()
    #获取client主机、编号和数据对应
    mydict[myconnection.fileno()] = nickname
    #把这个client加入到client列表
    mylist.append(myconnection)
    print('connection', connNumber, ' has nickname :', nickname)
    tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 进入聊天室】')
    #发送消息告知所有人有人进聊天室
    while True:
        try:
            recvedMsg = myconnection.recv(1024).decode()
            #接收客户端的消息
            if recvedMsg:
                print(mydict[connNumber], ':', recvedMsg)
                tellOthers(connNumber, mydict[connNumber] + ' :' + recvedMsg)
                #把接收过来的消息发送给所有人
        except (OSError, ConnectionResetError):
            try:
                mylist.remove(myconnection)
            except:
                pass
            print(mydict[connNumber], 'exit, ', len(mylist), ' person left')
            tellOthers(connNumber, '【系统提示：' + mydict[connNumber] + ' 离开聊天室】')
            myconnection.close()
            #接收不到证明客户不能再聊天室正常聊天，移除这个client
            return
while True:
    connection, addr = sock.accept()
    #获取客户端连接
    print('Accept a new connection', connection.getsockname(), connection.fileno())
    #输出有client进来获取主机名和端口，以及编号
    try:
        # connection.settimeout(5)
        buf = connection.recv(1024).decode()
        if buf == '1':
            #规定每个客户端进来会先发送1，然后向客户端发送欢迎
            connection.send(b'welcome to server!')
            # 为当前连接开辟一个新的线程
            mythread = threading.Thread(target=subThreadIn, args=(connection, connection.fileno()))
            mythread.setDaemon(True)
            mythread.start()
            #开启server服务器
        else:
            connection.send(b'please go out!')
            connection.close()
    except:
        pass