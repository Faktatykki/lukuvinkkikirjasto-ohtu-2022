*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser For Search
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Search Finds Right Result
    Searchpage Should Be Open
    Set Search  otsikko2
    Search
    Page Should Contain  otsikko2

User Search Is Case Insensitive
    Searchpage Should Be Open
    Set Search  Otsikko2
    Search
    Page Should Contain  otsikko2

User Search Searches Titles Containing Given Parameter
    Searchpage Should Be Open
    Set Search  otsikko
    Search
    Page Should Contain  Otsikko
    Page Should Contain  otsikko2

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae