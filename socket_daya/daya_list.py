import xml.dom.minidom
dom1 = xml.dom.minidom.parse('book.xml')
daya_root = dom1.documentElement
book1 = []

booknode = daya_root.getElementsByTagName('list')
for book in booknode:
    booklist = {}
    #做成键值对 id =001
    booklist['id']=book.getAttribute('id')
    booklist['head'] = book.getElementsByTagName('head')[0].childNodes[0].nodeValue
    #head = bookone
    booklist['name'] = book.getElementsByTagName('name')[0].childNodes[0].nodeValue
    booklist['number'] = book.getElementsByTagName('number')[0].childNodes[0].nodeValue
    booklist['page'] = book.getElementsByTagName('page')[0].childNodes[0].nodeValue
    book1.append(booklist)
    #为了防止第二次list覆盖第一次的，所以把字典放在列表中
print book1