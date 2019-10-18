import socket
def my_host():
    host_name = socket.gethostname()
    print("Host name %s" % host_name)
    IP = socket.gethostbyname(host_name)
    print("IP address %s" % IP)
if __name__ == '__main__':
    my_host()