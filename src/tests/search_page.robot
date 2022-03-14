*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

Search Finds Right Result
    Set Search  Uniikki
    Search
    Page Should Contain  www.fi

Search Is Case Insensitive
    Set Search  uniikki
    Search
    Page Should Contain  www.fi

Search Searches Titles Containing Given Parameter
    Set Search  otsikko
    Search
    Page Should Contain  Uniikki Otsikko
    Page Should Contain  Ensimmäinen Otsikko

Search Takes Special Characters
    Set Search  '
    Search
    Page Should Contain  Anonymous' tip
    Page Should Contain  Filterer's test
    Page Should Contain  Anonymous' marker tip
    
    
*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae