import urllib
import os

TARGET_URL = "https://www.python.org/ftp/python/3.7.4/"
TARGET_FILE = "python-3.7.4-embed-amd64.zip"

class CustomURLOpener(urllib.FancyURLopener):
    def http_error_206(self, url, fp, errcode, errmsg, headers, data=None):
        pass

def resume_sownload():
    file_exists = False
    CustomURLClass = CustomURLOpener()
    if os.path.exists(TARGET_FILE):
        out_file = open(TARGET_FILE,"ab")
        file_exists = os.path.getsize(TARGET_FILE)
        CustomURLClass.addheader("range","bytes=%s-"%(file_exists))
    else:
        out_file = open(TARGET_FILE,"wb")
        web_page=CustomURLClass.open(TARGET_URL+TARGET_FILE)
    if int(web_page.headers['Content-Length'])==file_exists:
        print "File already download"
    byte_count =0
    while True:
        data = web_page.read(8192)
        if not data:
            break
        out_file.write(data)
        byte_count = byte_count+len(data)
    web_page.close()
    out_file.close()
    for key,value in web_page.headers.items():
        print key,"=",value
        print "File copied",byte_count,"bytes from ",web_page.url

if __name__ == '__main__':
    resume_sownload()