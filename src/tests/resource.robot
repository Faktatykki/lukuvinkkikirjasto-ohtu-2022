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
    Page Should Contain  Kotisivu
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
