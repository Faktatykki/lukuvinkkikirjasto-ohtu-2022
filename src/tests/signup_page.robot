*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Signup Teardown
Test Setup  Go To Signuppage

*** Test Cases *** 
User Can Open Signuppage
    Signuppage Should Be Open

User Can Not Submit Too Short Username
    Set Username  a
    Set Password1  abcde
    Set Password2  abcde
    Create User
    Page Should Contain  Käyttäjänimen tulee olla 2-20 merkkiä pitkä
    Page Should Contain  Back
    Go Back
    Signuppage Should Be Open

User Can Not Submit Too Short Password
    Set Username  abcde
    Set Password1  a
    Set Password2  a
    Create User
    Page Should Contain  Salasanan tulee olla 2-20 merkkiä pitkä
    Page Should Contain  Back
    Go Back
    Signuppage Should Be Open


User Can Not Submit Non-matching Passwords
    Set Username  abcde
    Set Password1  abc
    Set Password2  acb
    Create User
    Page Should Contain  Salasanat eivät täsmää.
    Page Should Contain  Back
    Go Back
    Signuppage Should Be Open


User Can Signup
    Set Username  testi
    Set Password1  testi
    Set Password2  testi
    Create User
    Page Should Contain  testi kirjautuneena


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}
Set Password1 
    [Arguments]  ${password}
    Input Text  password1  ${password}
Set Password2 
    [Arguments]  ${password}
    Input Text  password2  ${password}
Create User
    Click Button  submit
Go Back
    Click Button  back
Signup Teardown
    Click Link  logout
    Close All Browsers