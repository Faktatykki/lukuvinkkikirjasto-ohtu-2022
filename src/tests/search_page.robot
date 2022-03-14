*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Searchpage

*** Test Cases ***
User Can Open Searchpage
    Searchpage Should Be Open

Search Finds Right Result
    Create User  Testi  Testi  Testi
    Set Title  Uniikki Otsikko 
    Set URL  www.fi
    Submit Vinkki
    Go To Searchpage
    Set Search  Uniikki
    Search
    Page Should Contain  www.fi

Search Is Case Insensitive
    Go To Mainpage
    Set Title  Uniikki Otsikko 
    Set URL  www.fi
    Submit Vinkki
    Go To Searchpage
    Set Search  uniikki
    Search
    Page Should Contain  www.fi

Search Searches Titles Containing Given Parameter
    Go To Mainpage
    Set Title  Uniikki Otsikko 
    Set URL  www.fi
    Submit Vinkki
    Set Title  Ensimmäinen Otsikko 
    Set URL  www.uniikkilinkki.fi
    Submit Vinkki
    Go To Searchpage
    Set Search  otsikko
    Search
    Page Should Contain  Uniikki Otsikko
    Page Should Contain  Ensimmäinen Otsikko
    

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
Set Password 
    [Arguments]  ${password}
    Input Text  password  ${password}
Set Password1 
    [Arguments]  ${password1}
    Input Text  password1  ${password1}
Set Password2 
    [Arguments]  ${password2}
    Input Text  password2  ${password2}