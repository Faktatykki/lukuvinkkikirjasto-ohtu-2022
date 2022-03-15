*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Can Search For Tip With Exact Search Term
    Go To Mainpage
    Mainpage Should Be Open
    Create Tip                  Tip-to-be-searched  https://search.example.com
    Page Should Contain         Tip-to-be-searched
    Go To Searchpage
    Searchpage Should Be Open
    Set Search                  Tip-to-be-searched
    Search
    Page Should Contain         Tip-to-be-searched

*** Keywords ***
Set Search
    [Arguments]     ${search}
    Input Text      search_param    ${search}

Search
    Click Button    searchBtn