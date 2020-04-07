import copy
import logging
import os

import gitlab
from lxml import etree

from enums import Labels,SchLabels,EnhancementSections as sections
from project import Project
from schematronTicket import SchematronTicket
from util import save


try:
    projectID = "224" 
    milestone_title = ""
    directory = "schematron" 
    project = Project(projectID,milestone_title)
    issues = project.project.issues.list(all=True)
    schemaTemp = os.path.join("templates","schematron.sch")

    for schLbl in SchLabels.lblList():
        for i in issues:
            schTicket = SchematronTicket(i)
            if schLbl in schTicket.labels and Labels.IMPLEMENTED.value in schTicket.labels:
                schTicket._getSection(sections.SCHEMATRON_RULES.value)
        SchematronTicket._getSchematronRules()
        schematorn = SchematronTicket.createSchematronDocument(schemaTemp,schLbl)
        if (schematorn):
            parser = etree.XMLParser(remove_blank_text=True)
            schematronEle = etree.fromstring(schematorn,parser)
            prettySch = etree.tostring(schematronEle,pretty_print=True)
            save(directory,f"{schLbl}.sch",prettySch.decode("utf-8"))

except Exception as e:
    print(f"error: {e}")

