import socket
def convert():
    data = 12
    print ":%s===> %s   net:%s"%(data,socket.ntohl(data),socket.htonl(data)) #---32bite
    print ":%s===> %s   net:%s" % (data, socket.ntohs(data), socket.htons(data)) #---16--bit
if __name__ == '__main__':
    convert()