import os
import io
import pathlib
from lxml import etree
rootDir = os.path.dirname(os.path.join(__name__))
    
def save(path,fileName,data):
    '''
    Save file within project directories and/or sub-directories
    '''
    saveDir = os.path.join(rootDir,path)
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)
    pathToFile = os.path.join(saveDir,fileName)    
    with open(pathToFile, "w") as f:
        f.write(data)



def loadXml(path):
    '''
    Load an xml document
    '''
    with open(path,mode="r",encoding="utf-8") as file:
        data = file.read()

    data = bytes(bytearray(data, encoding='utf-8'))
    parser = etree.XMLParser(remove_blank_text=True)
    return etree.fromstring(data, parser)


def formatXml(xmlDoc):
    return etree.tostring(xmlDoc,pretty_print=True)


def _parsXml(xmlString):
    try:
        parser = etree.XMLParser(remove_blank_text=True)
        return etree.fromstring(xmlString,parser)
    except Exception as e:
        print(f"Not a valid xml. {e}")    