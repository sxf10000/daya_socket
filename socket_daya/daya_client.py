import socket
import sys
import argparse
host = "localhost"

def daya_clietn(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server_address=(host,port)
    print "Connecting to %s port %s"%server_address

    sock.connect(server_address)

    try:
        message = "Test message.This will to server"
        print "Sending %s"%message
        sock.sendall(message)
        amount_recived = 0
        amount_expected = len(message)
        while amount_recived < amount_expected:
            data = sock.recv(32)
            amount_recived += len(data)
            print "Received :%s"%data
    except socket.error,e:
        print "Socket error :%s"%str(e)
    except Exception,e:
        print "Other exception:%s" %str(e)
    finally:
        print "Over seccuss!!!"
        sock.close()

if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="Socket client")
    parse.add_argument("--port",dest="port",type=int)
    give_args= parse.parse_args()
    port = give_args.port
    daya_clietn(port)