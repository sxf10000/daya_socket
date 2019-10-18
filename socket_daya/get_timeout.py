import socket

def get_timeout():
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #socket.AF_INET表示IPV4     socket.SOCK_STREAM--TCP协议
    print "defult socket timeout:%s"%soc.gettimeout()
    soc.settimeout(20)
    print "current socket timeout:%s"%soc.gettimeout()
if __name__ == '__main__':
    get_timeout()