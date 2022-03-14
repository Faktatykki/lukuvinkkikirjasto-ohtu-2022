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

Open And Configure Browser And Setup For Search
    Open And Configure Browser
    Create User  testi  testi  testi
    Create Tip  Testi Titteli  testiurli.fi
    Create Tip  Uniikki Otsikko  www.fi
    Create Tip  Ensimmäinen Otsikko  wwww.uniikkilinkki.fi

Create User
    [Arguments]  ${username}  ${password1}  ${password2}
    Go To Signuppage
    Set Username  ${username}
    Set Password1  ${password1}
    Set Password2  ${password2}
    Click Button  submit

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password1 
    [Arguments]  ${password}
    Input Text  password1  ${password}

Set Password2 
    [Arguments]  ${password}
    Input Text  password2  ${password}

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
