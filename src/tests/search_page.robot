*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open


*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  search