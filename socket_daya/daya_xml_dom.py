import xml.dom.minidom

daya_dom = xml.dom.minidom.parse("book.xml")
daya_root = daya_dom.documentElement
intro = daya_root.getElementsByTagName('intro')[0]
for node in intro.childNodes:
    if node.nodeType  in (node.TEXT_NODE,node.CDATA_SECTION_NODE):
        print node.data