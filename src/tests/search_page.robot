*** Settings ***
Resource  resource.robot
Suite Setup  Suite Setup For Search
Suite Teardown  Teardown For Search
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

User Finds Title With Exact Parameter
    Set Search  mock1
    Search
    Page Should Contain  mock1

User Finds Title With Case Insensitive Parameter
    Set Search  mock1
    Search
    Page Should Contain  mock1

User Finds Titles Containing Given Parameter
    Set Search  mock    
    Search
    Page Should Contain  mock1
    Page Should Contain  mock2
    

*** Keywords ***
Set Search
    [Arguments]  ${search}
    Input Text  search_param  ${search}

Search
    Click Button  Hae

Create User
    [Arguments]  ${username}  ${password1}  ${password2}
    Go To Signuppage
    Set Username  ${username}
    Set Password1  ${password1}
    Set Password2  ${password2}
    Click Button  submit
    Go To Main Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
Set Password1 
    [Arguments]  ${password1}
    Input Text  password1  ${password1}
Set Password2 
    [Arguments]  ${password2}
    Input Text  password2  ${password2}

Suite Setup For Search
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  1 seconds
    Create User  hakutesti  testi  testi
    Page Should Contain  hakutesti
    Page Should Contain  Lisää vinkki
    Create Tip  mock1  mockurl1
    Create Tip  mock2  mockurl2

Teardown For Search
    Go To Mainpage
    Click Link  logout
    Close All Browsers

