import copy
import re
from io import StringIO

from lxml import etree

from enums import EnhancementSections as sections
from enums import IssueState, Labels, NameSpace


class SchematronTicket ():
    contextRegex = re.compile(r'context="(.+?")')
    asserts = {}
    let = []
    rules = []
    contextDictionary = []
    matched=None
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
                        self.asserts[self.matched].append(line)
            elif startSection:
                return

    @classmethod
    def _getSchematronRules(cls):
        rule = []
        if len(cls.contextDictionary):
            cls.contextDictionary.sort()
            for key in cls.contextDictionary:
                rule.append(f"<sch:rule {key}>")
                rule.append("".join(cls.asserts[key]))
                rule.append("</sch:rule>")
                cls.rules.append("".join(rule))
                rule.clear()
        cls.asserts.clear()
        cls.contextDictionary.clear()

    @classmethod
    def createSchematronDocument(cls,schTemp:str, schType:str,):
        if len(cls.rules):
            with open (schTemp,"r",encoding="utf-8") as f:
                schDoc = f.read().format(pattern=schType,rules="".join(cls.rules),let="".join(cls.let))
                cls.rules.clear()
                cls.let.clear()

            return schDoc

