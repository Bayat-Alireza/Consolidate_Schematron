import copy
import logging
import os

from lxml import etree

from enums import Labels,SchLabels,EnhancementSections as sections
from project import Project
from schematronTicket import SchematronTicket
from util import save, formatXml
from pretty_console import color_printer as printer
from sort import sortSchematronByTagNameAndAttribute

try:
    projectID = "224" # Project Id for general-admin project
    milestone_title = ""
    directory = "schematron" # Folder in which the result will be saved
    project = Project(projectID,milestone_title)

    
    schematronLbl = project.filterSchematronLabels()
    issues = project.project.issues.list(all=True)

    # schematron template that will be used to create the schematron file 
    schemaTemp = os.path.join("templates","schematron.sch")

    for lblIdx,schLbl in enumerate(schematronLbl):
        printer.printProgressBar(0,len(issues),prefix="...") # this is just to show a progress bar
        for idx, issue in enumerate(issues):
            schTicket = SchematronTicket(issue)
            if schLbl in schTicket.labels and Labels.IMPLEMENTED.value in schTicket.labels:
                schTicket._getSection(sections.SCHEMATRON_RULES.value)
                printer.printProgressBar(idx+1,len(issues),prefix=f"{schTicket.iid}...")
        SchematronTicket.getSchematronRules(schLbl)
        schematorn = SchematronTicket.createSchematronDocument(schemaTemp,schLbl)
        if (len(schematorn)):
            sortedSchematron = sortSchematronByTagNameAndAttribute(schematorn,"rule","test")
            sortedSchematron = sortSchematronByTagNameAndAttribute(sortedSchematron,"pattern","context")
            sortedSchematron = sortSchematronByTagNameAndAttribute(sortedSchematron,"schema","id")
            save(directory,f"{schLbl}.sch",formatXml(sortedSchematron).decode("utf-8"))
        printer.printProgressBar(idx+1,len(issues),prefix=schLbl) # updateing the progress bar each round around
        
except Exception as e:
    print(f"error: {e}")

