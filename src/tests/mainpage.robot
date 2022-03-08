*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close All Browsers
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

User Can Not Submit Duplicate Title
    Set Title  Uniikki Otsikko 
    Set URL  www.fi
    Submit Vinkki
    Page Should Contain  Uniikki Otsikko
    Page Should Contain  www.fi
    Set Title  Uniikki Otsikko 
    Set URL  www.tämäneipitäisinäkyä.org
    Submit Vinkki
    Page Should Not Contain  www.tämäneipitäisinäkyä.org

User Can Not Submit Duplicate Url
    Set Title  Ensimmäinen Otsikko 
    Set URL  www.uniikkilinkki.fi
    Submit Vinkki
    Page Should Contain  Ensimmäinen Otsikko
    Page Should Contain  www.uniikkilinkki.fi
    Set Title  Toinen Otsikko 
    Set URL  www.uniikkilinkki.fi
    Submit Vinkki
    Page Should Not Contain  Toinen Otsikko

User Can Not Submit Empty Title
    Set URL  www.tämänkääneipitäisinäkyä.org
    Submit Vinkki
    Page Should Not Contain  www.tämänkääneipitäisinäkyä.org

User Can Not Submit Empty url
    Set Title  Otsikko Joka Ei Näy 
    Submit Vinkki
    Page Should Not Contain  Otsikko Joka Ei Näy

*** Keywords ***
Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}
Set URL 
    [Arguments]  ${url}
    Input Text  url  ${url}
Submit Vinkki
    Click Button  Lisää