*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser For Search
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Finds Title With Exact Parameter
    Set Search  otsikko1
    Search
    Page Should Contain  otsikko1

User Finds Title With Case Insensitive Parameter
    Set Search  oTsIkKo1
    Search
    Page Should Contain  otsikko1

User Finds Titles Containing Parameter
    Set Search  otsikko
    Search
    Page Should Contain  otsikko1
    Page Should Contain  otsikko2

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae

