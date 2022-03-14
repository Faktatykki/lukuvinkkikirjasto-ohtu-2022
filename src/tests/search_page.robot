*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

Search Finds Right Tip With Exact Parameter
    Create User  user  pass  pass
    Create Tip  title  url
    Go To Searchpage
    Set Search  title
    Search
    Page Should Contain  title

Search Is Not Casesensitive
    Create Tip  title  url
    Go To Searchpage
    Set Search  Title
    Search
    Page Should Contain  title

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae