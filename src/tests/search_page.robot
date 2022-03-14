*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser And Setup For Search
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Search Finds Right Result
    Set Search  Uniikki
    Search
    Page Should Contain  www.fi

User Search Is Case Insensitive
    Set Search  uniikki
    Search
    Page Should Contain  www.fi

User Search Searches Titles Containing Given Parameter
    Set Search  otsikko
    Search
    Page Should Contain  Uniikki Otsikko
    Page Should Contain  Ensimmäinen Otsikko
    
*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae