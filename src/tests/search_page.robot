*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser For Search
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Search Finds Right Result
    Set Search  Otsikko
    Search
    Page Should Contain  Otsikko

User Search Is Case Insensitive
    Set Search  otsikko
    Search
    Page Should Contain  Otsikko
    Page Should Contain  otsikkO

User Search Searches Titles Containing Given Parameter
    Set Search  ots
    Search
    Page Should Contain  Otsikko
    Page Should Contain  otsikkO

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae