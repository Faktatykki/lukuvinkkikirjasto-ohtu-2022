*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Search Finds Right Result
    Searchpage Should Be Open
    Set Search  eka
    Page Should Contain  eka

User Search Is Case Insensitive
    Searchpage Should Be Open
    Set Search  Eka
    Page Should Contain  eka

User Search Searches Titles Containing Given Parameter
    Searchpage Should Be Open
    Set Search  testi
    Page Should Contain  testi
    Page Should Contain  testi2
    Page Should Contain  Testi Titteli

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae