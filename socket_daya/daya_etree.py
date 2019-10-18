import xml.etree.ElementTree
root = xml.etree.ElementTree.parse("book.xml")
book_node = root.findall('list')
#查找所有的list
for node in book_node:
    #循环每一个list
    if node.attrib.has_key('id'):
        #在list的内部查找是否有id这个键值对
        print 'id'+":"+node.attrib['id']
        #如果有，把值取出来
    for note in node:
        #在循环中获取list中的所有标签
       print note.tag+':'+note.text

