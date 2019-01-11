*** Settings ***

Resource        tests/NPSP.robot
Library           DateTime
Suite Setup     Open Test Browser
Suite Teardown  Delete Records and Close Browser

*** Test Cases ***

Select an opportunity for an account make grid changes and process it
    [tags]  unstable
    ${ns} =  Get NPSP Namespace Prefix
    &{batch} =       API Create DataImportBatch    Batch_Process_Size__c=50    Batch_Description__c=Created via API    Donation_Matching_Behavior__c=Single Match or Create    Donation_Matching_Rule__c=donation_amount__c;donation_date__c    RequireTotalMatch__c=false    Run_Opportunity_Rollups_while_Processing__c=true   GiftBatch__c=true    Active_Fields__c=[{"label":"Donation Amount","name":"${ns}Donation_Amount__c","sObjectName":"Opportunity","defaultValue":null,"required":true,"hide":false,"sortOrder":0,"type":"number","options":null},{"label":"Donation Date","name":"${ns}Donation_Date__c","sObjectName":"Opportunity","defaultValue":null,"required":false,"hide":false,"sortOrder":1,"type":"date","options":null}] 
    &{account} =     API Create Organization Account
    &{contact} =     API Create Contact
    ${date} =     Get Current Date    result_format=%Y-%m-%d
    &{opportunity1} =     API Create Opportunity   &{account}[Id]    Donation  StageName=Prospecting    Amount=100    CloseDate=${date}  
    &{opportunity2} =     API Create Opportunity   &{contact}[AccountId]    Donation  StageName=Prospecting    Amount=100    CloseDate=${date}      
    Select App Launcher Tab   Batch Gift Entry
    Click Link  &{batch}[Name]
    Select Value From BGE DD    Donor Type    Account
    Populate Address    Search Accounts    &{account}[Name]
    Click Link    &{account}[Name]
    Click Link    Review Donations
    Click BGE Button    Update this Opportunity
    Select Value From BGE DD    Donor Type    Contact
    Page Should Not Contain Link    Review Donations
    Populate Address    Search Contacts    &{contact}[FirstName] &{contact}[LastName]
    Click Link    &{contact}[FirstName] &{contact}[LastName]
    Click Link    Review Donations
    Click Link    Alternatively, create a new Opportunity.
    Fill BGE Form
    ...                       Donation Amount=20
    Select BGE Date Picker    Donation Date
    Click BGE Button    Today
    Click BGE Button       Save
    Reload Page
    Verify Row Count    1
    Page Should Not Contain Link    &{opportunity2}[Name]
    Wait For Locator    bge.edit_button    Donation Amount
    Click BGE Edit Button    Donation Amount  
    Wait For Locator    bge.edit_field   
    Populate BGE Edit Field    Donation Amount    100
    Click Managehh Add Button    Donation Date
    Page Should Not Contain Link    &{opportunity2}[Name]
    Click BGE Button       Process Batch
    Select Frame With Title    NPSP Data Import
    Click Button With Value   Begin Data Import Process
    Wait For Locator    data_imports.status    Completed
    Click Button With Value   Close
    &{existing_opp} =  Salesforce Get    Opportunity    &{opportunity2}[Id]
    Should Be Equal As Strings    &{existing_opp}[Amount]    100.0
    Should Be Equal As Strings    &{existing_opp}[CloseDate]    ${date}
    Should Be Equal As Strings    &{existing_opp}[StageName]    Prospecting 
    ${value}    Return Locator Value    bge.value    Donation
    Click Link    ${value}
    Select Window     New
    ${opp_name}    Return Locator Value    check_field    Opportunity
    Click Link    ${opp_name}
    ${newopp_id}    Get Current Record ID
    &{new_opp} =  Salesforce Get    Opportunity    ${newopp_id}
    Should Be Equal As Strings    &{new_opp}[Amount]    100.0
    Should Be Equal As Strings    &{new_opp}[CloseDate]    ${date}
    Should Be Equal As Strings    &{new_opp}[StageName]    Closed Won
    # Select Tab    Details
    # Confirm Value    Amount    $100.00    Y 
    # ${opp_date} =     Get Current Date    result_format=%-m/%-d/%Y
    # Confirm Value    Close Date    ${opp_date}    Y 
    # Confirm Value    Stage    Closed Won    Y 
    Go To Record Home    &{contact}[Id]
    Load Related List    Opportunities
    Verify Occurrence    Opportunities    2
      

    
    