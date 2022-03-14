*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Set Up Database  hakutesti  hakutesti  hakutesti

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

Search Finds Right Tip With Exact Parameter
    Set Search  Mock Tip 1
    Search
    Page Should Contain  Mock Tip 1

Search Is Not Casesensitive
    Set Search  mock tip 1
    Search
    Page Should Contain  Mock Tip 1

Search Finds Right Results When Target Contains Parameter
    Set Search  Mock
    Search
    Page Should Contain  Mock Tip 1
    Page Should Contain  Mock Tip 2

*** Keywords ***
Set Up Database
    [Arguments]  ${username}  ${password1}  ${password2}
    resource.Create User  username  password1  Password1
    resource.Create Tip  Mock Tip 1  mockurl1
    resource.Create Tip  Mock Tip 2  mockurl2
    Go To Searchpage

Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae