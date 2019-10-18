import argparse,asyncore,socket

LOCAL_SERVER_PORT ="localhost"

RMEOTE_SERVER_HOST="www.baidu.com"
BUFSIZE=4096

class PortForwarder(asyncore.dispatcher):
    def __init__(self,ip,port,rempteip,remoteport,backlog=5):

        asyncore.dispatcher.__init__(self)
        self.rempteip=rempteip
        self.remoteport= remoteport
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((ip,port))
    def handle_accept(self):
        conn,addr=self.accept()
        print "Conneted to:",addr

        Sender(Receiver(conn),self.rempteip,self.remoteport)

class Receiver(asyncore.dispatcher):
    def __init__(self,conn):

        asyncore.dispatcher.__init__(self,conn)

        self.from_remote_buffer=''

        self.to_remote_buffer=''
        self.sender=None
    def handle_connect(self):

        pass
    def handle_read(self):

        read = self.recv(BUFSIZE)
        self.from_remote_buffer+=read
    def writable(self):

        return (len(self.to_remote_buffer)>0)
    def handle_write(self):
        sent = self.send(self.to_remote_buffer)

        self.to_remote_buffer=self.to_remote_buffer[sent:]
    def handle_close(self):
        self.close()

        if self.sender:
            self.sender.close()
class Sender(asyncore.dispatcher):
    def __init__(self,reveiver,remoteip,remoteport):

        asyncore.dispatcher.__init__(self)
        self.reveiver=reveiver

        reveiver.sender= self
        self.create_socket(socket.AF_INET,socket.SOCK_STREAM)

        self.connect((remoteip,remoteport))
    def handle_connect(self):

        pass
    def handle_read(self):

        read = self.recv(BUFSIZE)
        self.reveiver.to_remote_buffer +=read
    def writable(self):

        return (len(self.to_remote_buffer) > 0)
    def handle_write(self):

        sent = self.send(self.reveiver.from_remote_buffer)
        self.reveiver.from_remote_buffer=self.reveiver.from_remote_buffer[sent:]
    def handle_close(self):

        self.close()
        self.reveiver.close()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="SOCKET SERVER")
    parser.add_argument("--local-host",action="store",dest="local_host",default=LOCAL_SERVER_PORT)
    parser.add_argument("--local-port",action="store",dest="local_port",type=int,required=True)
    parser.add_argument("--remote-host",action="store",dest="remote_host",default=RMEOTE_SERVER_HOST)
    parser.add_argument("--remote-port",action="store",dest="remote_port",type=int,default=80)

    given_args=parser.parse_args()
    local_host,remote_host = given_args.local_host,given_args.remote_host
    local_port,remote_port = given_args.local_port,given_args.remote_port
    print "Strating port local %s:%s=>remote %s:%s"%(local_host,local_port,remote_host,remote_port)
    PortForwarder(local_host,local_port,remote_host,remote_port)
    asyncore.loop()
