*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  127.0.0.1:5000
# ${SERVER}  lit-brushlands-38911.herokuapp.com
${BROWSER}  Chrome
${DELAY}  0.1 seconds
${HOME URL}  http://${SERVER}/


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
    
Lisäyslomake Should Be Open
    Page Should Contain  Lisää vinkki
    Page Should Contain  title
    Page Should Contain  url

Go To Mainpage
    Go To  ${HOME URL}

Go To Signuppage
    Go To  ${HOME URL}
    Click Link  id=signup