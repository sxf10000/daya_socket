import  socket
def get_server():
    server_host='www.baidu.com'
    try:
        server_ip = socket.gethostbyname(server_host)
        print("IP :%s"%server_ip)
    except socket.error,e:
        print "%s %s"%(server_host,e)
if __name__ == '__main__':
    get_server()