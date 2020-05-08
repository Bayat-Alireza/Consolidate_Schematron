import copy
import re
from io import StringIO

from lxml import etree

from enums import EnhancementSections as sections
from enums import IssueState, Labels, NameSpace

from util import _parsXml


class SchematronTicket ():
    contextRegex = re.compile(r'context="(.+?")')
    asserts = {}
    let = []
    rules = []
    contextDictionary = []
    matched=None
    inProgress = ""
    def __init__(self,issue):
        self.issue = issue
        self.iid = issue.iid
        self.description = StringIO(issue.description)
        self.labels = issue.labels
         

    def _getSection(self,section:str):
        copyDescription = copy.copy(self.description)
        startSection = False
        
        for line in copyDescription:
            if not startSection and line.strip().startswith(section):
                startSection = True
            elif startSection and not line.strip().startswith(sections.HASH_SIGN.value):
                if "<sch:let" in line:
                    self.let.append(line)
                if line.strip() and line.strip() not in ["```","</sch:rule>","```xml"] and "<sch:let" not in line:
                    matchedCtx = self.contextRegex.search(line)
                    if (matchedCtx and matchedCtx.group().strip() not in self.contextDictionary):
                        self.matched = matchedCtx.group().strip()
                        self.contextDictionary.append(self.matched)
                        self.asserts[self.matched] = []
                    elif matchedCtx and matchedCtx.group() in self.contextDictionary:
                        self.matched = matchedCtx.group()
                    else:
                        self.inProgress += line
            elif startSection:
                self.asserts[self.matched].append(self.inProgress.strip())
                return

    @classmethod
    def getSchematronRules(cls,schType:str):
        rule = []
        if len(cls.contextDictionary) == 0:
            print(f"There is no implemented {schType} ")
            return
        if len(cls.contextDictionary) != 0: 
            for ctx in cls.contextDictionary:
                if len(cls.asserts[ctx]) == 0:
                    raise ValueError(f"{schType}: There are no asserts in the context of {ctx}")
                rule.append(f"<sch:rule {ctx}>")
                rule.append("".join(cls.asserts[ctx]))
                rule.append("</sch:rule>")
                cls.rules.append("".join(rule))
                rule.clear()
            cls.asserts.clear()
            cls.contextDictionary.clear()
            return cls.rules

    @classmethod
    def createSchematronDocument(cls,schTemp:str, schType:str,):
        schTypeArr = schType.split(" ")
        schType = "_".join(schTypeArr)
        if len(cls.rules):
            with open (schTemp,"r",encoding="utf-8") as f:
                schDoc = f.read().format(pattern=schType,rules="".join(cls.rules),let="".join(cls.let))
                cls.rules.clear()
                cls.let.clear()

            return _parsXml(schDoc)


        

