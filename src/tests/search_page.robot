*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Can Search Title With Exact Parameter
    Create Tip  otsikko  urli
    Go To Searchpage
    Set Search  otsikko
    Search
    Page Should Contain  otsikko

User Can Search Title With Case Insensitive Paramter
    Set Search  Otsikko
    Search
    Page Should Contain  otsikko

User Can Search Multiple Titles With Containing Parameter
    Create Tip  otsikko2  urli2
    Go To Searchpage
    Set Search  otsikko
    Search
    Page Should Contain  otsikko
    Page Should Contain  otsikko2

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae