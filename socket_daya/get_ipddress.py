import  argparse
import  sys
import socket
import fcntl
import  struct
import array


def get_ip_adress(ifname):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        sock.fileno(),0x8915,struct.pack("256s",ifname[:15])
    )[20:24])

if __name__ == '__main__':
    parsre = argparse.ArgumentParser(description="Python IPaddr")
    parsre.add_argument("--ifname",dest="ifname")
    give_args= parsre.parse_args()
    ifname =  give_args.ifname
    print "IterFace[%s] --> IP:%s"%(ifname,get_ip_adress(ifname))