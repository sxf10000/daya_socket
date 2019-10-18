import HTMLParser,urllib
from htmlentitydefs import entitydefs

def getimage(addr):
    u = urllib.urlopen(addr)
    data = u.read()
    filename = addr.split("/")[-1]
    f = open(filename,'wb')
    f.write(data)
    f.close()
    print filename +": success"
class TitleParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.taglevels = []
        self.handletags = ['title','body']
        self.processing = None
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag in self.handletags:
            self.data = ''
            self.processing = tag
        if tag =='a':
            for name,value in attrs:
                if name=='href':
                    print "Connnect link:"+value
        if tag == "img":
            for name,value in attrs:
                if name =='src':
                    getimage(value)

    def handle_data(self, data):
        if self.processing:
            self.data += data

    def handle_endtag(self, tag):
        if tag == self.processing:
            print str(tag) + ":" +str(self.gettitle())
            self.processing = None

    def handle_entityref(self, name):
        if entitydefs.has_key(name):
            self.handle_data(entitydefs[name])
        else:
            self.handle_data('&'+name+';')
    def handle_charref(self, name):
        try:
            charnum = int(name)
        except ValueError:
            return
        if charnum<1 or charnum>255:
            return
        self.handle_data(chr(charnum))
    def gettitle(self):
        return self.data

fd = open('daya.html')
tp = TitleParser()
tp.feed(fd.read())