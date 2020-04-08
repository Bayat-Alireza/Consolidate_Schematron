from enum import Enum

class NameSpace(Enum):
    NAME_SPACE = ' xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:lx="lixi.org.au/schema/appinfo_elements" xmlns:li="lixi.org.au/schema/appinfo_instructions"'
class Standards(Enum):
    CAL = 'CAL'
    VAL = 'VAL'
    SVC = 'SVC'
    CNZ = 'CNZ'
    CDA = 'CDA'
    DAS = 'DAS'
    ACC = 'ACC'
    LMI = 'LMI'

    @classmethod
    def stdList(cls):
        return [enum.value for enum in cls]


class EnhancementSections (Enum):
    ADD_ITEM = "Add Items:"
    PROBLEM = "# Problem / Requirement Statement"
    SOLUTION = "# Solution"
    OVERVIEW = "## Overview"
    DETAIL = "## Detail"
    DEFINITION = "## Definitions"
    DATA_DICTIONARY = "## Data Dictionary"
    MASTER_SNIPPET = "## Master Schema Snippet"
    RELATED_LINKS = "# Related Links"
    SCHEMATRON_RULES = "# Schematron Rule"
    HASH_SIGN = "#"

    @classmethod
    def sectionList(cls):
        return [enum.value for enum in cls] 

class Labels(Enum):
    SCHEMATRON_RULE = "SchematronRule"
    IMPLEMENTED = "Implemented"

    @classmethod
    def lblList(cls):
        return [enum.value for enum in cls]

class SchLabels(Enum):
    MANDATORY_ITEM = "MandatoryItem Rule"
    POLICY_RULE = "Policy Rule"
    STRUCTURAL_RULE = "Structural Rule"
    
    @classmethod
    def lblList(cls):
        return [enum.value for enum in cls]
        
class IssueState(Enum):
    CLOSED = "closed"
    OPENED = "opened"
    TOTAL = "Total"

    @classmethod
    def statList(cls):
        return[enum.value for enum in cls]