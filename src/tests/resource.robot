*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  127.0.0.1:5000
# ${SERVER}  lit-brushlands-38911.herokuapp.com
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}/
${LOGIN URL}  http://${SERVER}/login

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Open And Configure Browser For Search
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}
    Go To Mainpage
    Go To Signuppage
    Signuppage Should Be Open
    Create User And Go To Mainpage  käyttäjä  1234  1234
    Page Should Contain  käyttäjä kirjautuneena
    Create Tip  otsikko1  url1
    Page Should Contain  otsikko1
    Create Tip  otsikko2  url2
    Page Should Contain  otsikko2

Mainpage Should Be Open
    Page Should Contain  Lukuvinkit
    Title Should Be      Lukuvinkit - Etusivu

Signuppage Should Be Open
    Page Should Contain  Luo uusi käyttäjä
    Page Should Contain  Käyttäjänimi
    Page Should Contain  Salasana
    Page Should Contain  Salasana uudestaan
    Page Should Contain  Luo käyttäjä
    
Login Page Should Be Open 
    Page Should Contain  Kirjaudu sisään
    Page Should Contain  Käyttäjänimi
    Page Should Contain  Salasana
    Page Should Contain  Kirjaudu

Lisäyslomake Should Be Open
    Page Should Contain  Lisää vinkki
    Page Should Contain  title
    Page Should Contain  url

Searchpage Should Be Open
    Page Should Contain  Hae vinkkejä
    Page Should Contain  Tulokset

Go To Mainpage
    Go To  ${HOME URL}

Go To Signuppage
    Go To  ${HOME URL}
    Click Link  id=signup

Go To Login Page
    Go To  ${LOGIN URL}

Go To Searchpage
    Go To  ${HOME URL}
    Click Link  id=searchpage

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set URL 
    [Arguments]  ${url}
    Input Text  url  ${url}

Submit Vinkki
    Click Button  Lisää

Create Tip
    [Arguments]  ${title}  ${url}
	Go To Mainpage
	Set Title			${title}
	Set URL				${url}
	Submit Vinkki

Create User And Go To Mainpage
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