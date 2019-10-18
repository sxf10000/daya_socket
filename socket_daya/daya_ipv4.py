import socket
from binascii import hexlify

def con_ipv4():
    ip_address= ['127.0.0.1','192.168.1.102']
    for ip in ip_address:
        ip_addr= socket.inet_aton(ip)
        un_up_addr = socket.inet_ntoa(ip_addr)
        print "IP Addres:%s =====>Packed:%s,Unpaked:%s"\
              %(ip,hexlify(ip_addr),un_up_addr)
        print ip_addr
if __name__ == '__main__':
    con_ipv4()