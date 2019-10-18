import ntplib

from time import ctime

def get_time():
    ntpclient = ntplib.NTPClient()
    reponse = ntpclient.request("pool.ntp.org")
    print ctime(reponse.tx_time)

if __name__ == '__main__':
    get_time()