*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser For Search
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

Testi
    Go To Mainpage
    Page Should Contain  Mock



*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  hae

