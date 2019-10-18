import xml.dom
def create_element(doc,tag,attr):
    # 专注于创建最底层的标签，例如head
    elementNode = doc.createElement(tag)
    #创建一个标签名字，例如<head>
    textNode = doc.createTextNode(attr)
    #创建值，例如bookone
    elementNode.appendChild(textNode)
    #把值放在标签的里边，作为子信息
    return elementNode
    #最后返回标签

dom1 = xml.dom.getDOMImplementation()
# 获取一个创建文档的对象
doc = dom1.createDocument(None,'info',None)
#创建根节点，例如<info>
top_element = doc.documentElement
#把创建好的根节点获取过来
books=[{'head': u'bookone', 'page': u'200', 'number': u'001', 'id': u'001', 'name': u'python check'},
       {'head': u'booktwo', 'page': u'300', 'number': u'002', 'id': u'002', 'name': u'python learn'}]
for book in books:
    #创建info下边的子标签
    lNode = doc.createElement('list')
    #创建list001获取002标签
    lNode.setAttribute('id',book['id'])
    # 在给list添加一个id的值<list id="001">
    headNode = create_element(doc,'head',book['head'])
    #创建 list下边的子标签<head>bookone</head>
    pageNode = create_element(doc, 'page', book['page'])
    numberNode = create_element(doc, 'number', book['number'])
    nameNode = create_element(doc, 'name', book['name'])
    lNode.appendChild(headNode)
    # 把创建好的head标签添加到list标签下边
    lNode.appendChild(pageNode)
    lNode.appendChild(numberNode)
    lNode.appendChild(nameNode)
    top_element.appendChild(lNode)
    #把list标签放在根标签下边，也就是放在info下边
xmldaya = open("dayaxml.xml",'w')
#以可写的方式打开一个文件
doc.writexml(xmldaya,addindent=' '*4,newl='\n',encoding = 'utf-8')
# 使用写xml的方法，写在xmldaya上，addindent每行行首的空格数，newl每行写完之后的操作-换行，
# encoding就是xml支持的格式
xmldaya.close()
#写完关闭