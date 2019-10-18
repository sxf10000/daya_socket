import urllib.request
from bs4 import BeautifulSoup
import re
url = r'https://www.jetbrains.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")

soup = BeautifulSoup(html,"html.parser")
head = soup.findAll("head")
head1 = soup.head
html = soup.contents[2]
head = html.contents[1]
body = html.contents[3]
per = body.parent
a = body.findAll("a")
head = body.previousSibling.previousSibling
test = soup.find("nav")
#head 和body
list = ['head','body']
test = soup.findAll(list)
#正则
test = soup.findAll(re.compile("^he"))
test1 = soup.find(class_="header-index",id="js_main_nav")
test1 = soup.find(class_=re.compile("^header"),id="js_main_nav")
#test1 = soup.find(attrs={(property(re.compile("og:title"))),type(' PyCharm: the Python IDE for Professional Developers by JetBrains')})
print(test1)
