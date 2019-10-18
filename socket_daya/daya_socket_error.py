import socket,sys,argparse
def main():
    print "--host:is servername,--port:is server port --filename: is send data"
    print "domo --host=www.baidu.com --port=80  --filename=daya_socket_error.py"
    parser = argparse.ArgumentParser(description="socket error Examples")
    parser.add_argument("--host",dest="host")
    parser.add_argument("--port",dest="port",type=int)
    parser.add_argument('--file',dest="file")
    give_args = parser.parse_args()
    host = give_args.host
    port = give_args.port
    filename = give_args.file

    try:
        so = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    except socket.error as e:
        print "Error create socket:%s"%e
        sys.exit(1)
    try:
        so.connect((host,port))
    except socket.gaierror as e:
        print "Adress error connnecting to server:%s"%e
        sys.exit(1)
    except socket.error as e:
        print "Connection error :%s" %e
        sys.exit(1)
    try:
        so.sendall("GET %s HTTP/1.0\r\n\r\n"%filename)
    except socket.error as e:
        print "Error sending data :%s"%e
        sys.exit(1)
    while 1:
        try:
            buf = so.recv(2048)
        except socket.error as e :
            print "Error receiving data :%s"%e
            sys.exit(1)
        if not len(buf):
            break
        sys.stdout.write(buf)


if __name__ == '__main__':
    main()

