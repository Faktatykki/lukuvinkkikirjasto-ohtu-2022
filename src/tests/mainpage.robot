*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Mainpage

*** Test Cases *** 
User Can Open Mainpage
    Main Page Should Be Open

User Can Open Lukuvinkin Lisäyslomake
    Lisäyslomake Should Be Open

User Can Submit Lukuvinkki
    Set Title  Testi Titteli 
    Set URL  testiurli.fi
    Submit Vinkki
    Page Should Contain  Testi Titteli
    Page Should Contain  testiurli.fi

*** Keywords ***
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}
Set URL 
    [Arguments]  ${url}
    Input Text  url  ${url}
Submit Vinkki
    Click Button  Lisää