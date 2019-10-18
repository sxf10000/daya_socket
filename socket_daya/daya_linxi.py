from bs4 import BeautifulSoup
import re
import urllib.request
url = r'https://ke.qq.com/?tuin=a8b024d7'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
req = urllib.request.Request(url=url,headers=headers)
res = urllib.request.urlopen(req)
html = res.read().decode("utf-8")
soup = BeautifulSoup(html,"html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)
# print(soup.a)
# print(soup.a['href'])
#print(soup.header.contents)
# print(soup.find(id="js_main_nav").get_text())
# print(soup.a.attrs)
# for s_value in soup.findAll("a"):
#     print(s_value.get_text())for tag in soup.findAll(title="IT·互联网",target="_blank"):
# #     print(tag.name)
#
li = []
for tag in soup.findAll(id="js_main_nav"):
    for child in tag.children:

        li.append(child)
print(li[1].get_text())