import HTMLParser,urllib
from htmlentitydefs import entitydefs

class TitleParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.taglevels = []
        self.handletags = ['a']
        self.processing = None
        self.linkString =''
        self.linkaddr = ''
        HTMLParser.HTMLParser.__init__(self)
    def handle_starttag(self, tag, attrs):
        if tag in self.handletags:
            for name,value in attrs:
                if name=='href':
                    self.linkaddr=value
            self.processing=tag
    def handle_data(self, data):
        if self.processing:
            self.linkString += data

    def handle_endtag(self, tag):
        if tag == self.processing:
            print self.linkString.decode("utf-8")+":"+self.linkaddr
            self.processing = None
            self.linkString=''

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
        return self.linkaddr

tp = TitleParser()
tp.feed(urllib.urlopen('http://www.renren.com/').read())