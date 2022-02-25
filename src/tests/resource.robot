*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}/mainpage



*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Mainpage Should Be Open
    Page Should Contain  Lukuvinkit
    Page Should Contain  Title: 
    Page Should Contain  URL:

Lisäyslomake Should Be Open
    Page Should Contain  Lisää vinkki
    Page Should Contain  Otsikko: 
    Page Should Contain  URL:

Go To Mainpage
    Go To  ${HOME URL}