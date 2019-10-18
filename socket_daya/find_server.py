import socket
def find_server_name():
    l_port = [80,25]

    for port in l_port:
        name = socket.getservbyport(port, "tcp")
        print "Port:%s ===>server name :%s"%(port,name)
    print "Port:%s ===>server name :%s"%(53,socket.getservbyport(53,"udp"))
if __name__ == '__main__':
    find_server_name()