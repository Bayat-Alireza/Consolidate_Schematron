
from enums import NameSpace
from lxml import etree

def sortSchematronByTagNameAndAttribute(schDoc,parentTagName,childAttribute):
    '''
    Sort Schematron document based on attributes of a parent tag 

    - schDoc: xml - xml parsed document
    - parentTagName: str - element name
    - childAttribute: str - child element attribute that will be used as basis for sort
    '''
    def getkey(elem):
        try:
            tag = etree.QName(None,elem.tag).localname
            if (tag == "let"):
                return f"0{elem.get('name')}"
            if not elem.get(childAttribute):
                return ""
            return elem.get(childAttribute)
        except Exception:
            return ""    
        
    xpath = xpath = f".//sch:{parentTagName}"
    tags = schDoc.findall(xpath,NameSpace.NS_OBJ.value)
    for t in tags:
        container = t
        container[:] = sorted(t,key=getkey)
       
    return schDoc

