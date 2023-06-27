from enum import Enum


class DocType(Enum):
    AN = "Analytical Data"
    CO = "Compliance"
    CI = "Correspondence-Internal"
    CR = "Correspondence-Received"
    CS = "Correspondence-Sent"
    FI = "Financial"
    FO = "Forms"
    LE = "Legal"
    PE = "Permits"
    PL = "Plans"
    RE = "Reports"
    OT = "Other"

    @classmethod
    def has_value(cls, value):
        return value in iter(cls)


class DocSubType(Enum):
    AD = "ADVF"
    AG = "Agreement/Contract"
    AI = "Air"
    AN = "Annual"
    AP = "Application"
    AS = "Assessment/Investigation"
    BE = "Below Reportable Quantity Event"
    CE = "Certificate/License/Registration"
    CR = "Confidentiality Request"
    CA = "Corrective Action"
    DM = "DMR"
    DR = "Draft Permit"
    FE = "Fee Collection"
    FP = "Final Permit"
    FA = "Financial Assurance"
    GR = "Green Cards"
    HE = "Hearing Request"
    ID = "ID-Generator Notification"
    IC = "Incident"
    IS = "Inspection"
    IN = "Invoice"
    JU = "Judgment/Decision/Order"
    MA = "Manifest"
    ME = "Meeting"
    MD = "Modifications"
    MO = "Monitoring"
    NA = "Name/Owner Change"
    NE = "NetDMR Subscriber Agreement"
    NC = "Noncompliance"
    NM = "Note/Memo"
    NO = "Notice"
    NF = "Notifications"
    OR = "Order"
    PE = "Penalty"
    PU = "Public Notice"
    QU = "Quarterly"
    RF = "Reference Materials"
    RT = "Returned Mail"
    SM = "Semi-Annual"
    ST = "Settlement"
    TE = "Testing"
    TR = "Trust Fund"
    VA = "Variances/Exemptions"
    WA = "Warning Letters"
    OT = "Other"

    @classmethod
    def has_value(cls, value):
        return value in iter(cls)


class Media(Enum):
    AC = "Accident Prevention"
    AI = "Air Quality"
    AS = "Asbestos"
    BI = "Biosolids"
    GR = "Ground Water"
    HA = "Hazardous Waste"
    IN = "Inactive & Abandoned Sites"
    LE = "Lead"
    MU = "Multi-Media"
    NO = "Non-Applicable"
    RA = "Radiation"
    SO = "Solid Waste"
    SU = "Surface Water"
    UN = "Underground Storage Tanks"
    WA = "Waste Tire"
    OT = "Other"

    @classmethod
    def has_value(cls, value):
        return value in iter(cls)


class DocFunction(Enum):
    AG = "Agency Governance"
    AE = "Air Emissions Inventory"
    AM = "Air Modeling"
    AA = "Air Monitoring and Analysis"
    AP = "Air Planning"
    AS = "Air Stack and Tank Testing"
    CH = "Chemical Accident Prevention"
    EN = "Enforcement"
    FI = "Financial"
    IE = "Incidents - Emergency"
    IN = "Incidents - Non-Emergency"
    IF = "Information Services"
    IS = "Inspections"
    LE = "Legal"
    OF = "Office of the Secretary (OSEC)"
    OU = "Outreach"
    PS = "Permit Support Services"
    PE = "Permits"
    RA = "Radiological Services"
    RE = "Remediation Services"
    SI = "Single Point of Contact (SPOC)"
    UN = "Unassigned"
    US = "Underground Storage Tanks"
    WA = "Water Quality Standards and Assessment"
    OT = "Other"

    @classmethod
    def has_value(cls, value):
        return value in iter(cls)
