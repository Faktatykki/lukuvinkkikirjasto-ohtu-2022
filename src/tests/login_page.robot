*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
User Can Open Login Page
    Click Link  Kirjaudu sisään
    Login Page Should Be Open

User Can Login With Correct Username
    Create User  Testaaja  Test  Test
    Click Link  Kirjaudu sisään
    Set Username  Testaaja
    Set Password  Test
    Click Button  Kirjaudu
    Mainpage Should Be Open
    Page Should Contain  Testaaja kirjautuneena

User Can Log Out
    Click Link  Kirjaudu ulos
    Main Page Should Be Open
    Page Should Contain  Luo käyttäjä
    Page Should Contain  Kirjaudu sisään

User Can Not Login With Incorrect Username Or Password
    Click Link  Kirjaudu sisään
    Set Username  Wrong
    Set Password  password
    Click Button  Kirjaudu
    Page Should Contain  Väärä käyttäjä tai salasana

*** Keywords *** 
Create User
    [Arguments]  ${username}  ${password1}  ${password2}
    Go To Signuppage
    Set Username  ${username}
    Set Password1  ${password1}
    Set Password2  ${password2}
    Click Button  submit
    Go To Main Page
    Click Link  Kirjaudu ulos

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
Set Password 
    [Arguments]  ${password}
    Input Text  password  ${password}
Set Password1 
    [Arguments]  ${password1}
    Input Text  password1  ${password1}
Set Password2 
    [Arguments]  ${password2}
    Input Text  password2  ${password2}
