*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser For Search
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

Search Finds Right Tip With Exact Parameter
    Set Search  Mock Tip 1
    Search
    Page Should Contain  mockurl1

Search Is Not Casesensitive
    Set Search  mock tip 1
    Search
    Page Should Contain  mockurl1

Search Finds Right Results When Target Contains Parameter
    Set Search  Mock
    Search
    Page Should Contain  mockurl1
    Page Should Contain  mockurl2

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae