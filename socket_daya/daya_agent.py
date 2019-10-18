import urllib
URL = "https://www.github.com"
AGENT_ADDRESS="165.24.10.8:8080"

if __name__ == '__main__':
    resp = urllib.urlopen(URL,proxies={"http":AGENT_ADDRESS})
    print "Proxy server headers :%s" %resp.headers