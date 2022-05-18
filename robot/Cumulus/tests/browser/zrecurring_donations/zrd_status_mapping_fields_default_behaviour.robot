*** Settings ***

Resource        robot/Cumulus/resources/NPSP.robot
Library         cumulusci.robotframework.PageObjects
...             robot/Cumulus/resources/NPSPSettingsPageObject.py
Suite Setup     Run keywords
...             Enable RD2
...             Open Test Browser
Suite Teardown  Capture Screenshot and Delete Records and Close Browser


*** Test Cases ***

User on a RD2 enbaled Org should See Status Mappings Option along with default mapped values
    [Documentation]               On an org with rd2 enabled, a user
     ...                          Should see the option Status to state mapping option
     ...                          When clicked on the sublink status to state mappings
     ...                          A table with default mapped values get populated


    [tags]                       W-8211315  feature:RD2   unstable    deprecated  unit
    Open NPSP Settings           Recurring Donations               Status to State Mapping
    Verify Status To State Mappings
    ...                          Active=Active
    ...                          Lapsed=Lapsed
    ...                          Closed=Closed
    ...                          Paused=Active

