*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page



*** Test Cases ***
A Not Logged In User Should Not See Filter Select 
    Page Should Not Contain  Kaikki

A Logged In User Should See Filter Select 
    Create User  Testaaja  salasana  salasana
    Page Should Contain  Kaikki

A Logged In User Can Change Filter Selection
    Page Should Contain  Kaikki
    Select From List By Label  id:readTips  Luetut
    Page Should Contain  Luetut
    Select From List By Label  id:readTips  Lukemattomat
    Page Should Contain  Lukemattomat

A Logged In User Can Filter Tips By Read Status 
    Create Tip  toka.fi  toka

    Create Tip  kolmas.fi  kolmas
    Page Should Contain  toka.fi
    Page Should Contain  toka
    Page Should Contain  kolmas.fi
    Page Should Contain  kolmas
    Click Link  //ul[@id="tipsList"]/li[1]/a[2]
    Select From List By Label  id:readTips  Luetut
    Page Should Contain  toka.fi 
    Page Should Contain  toka
    Select From List By Label  id:readTips  Lukemattomat
    Page Should Contain  kolmas.fi
    Page Should Contain  kolmas
    Select From List By Label  id:readTips  Kaikki
    Page Should Contain  kolmas.fi
    Page Should Contain  kolmas
    Page Should Contain  toka.fi 
    Page Should Contain  toka


*** Keywords *** 
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
    [Arguments]  ${password1}
    Input Text  password1  ${password1}
Set Password2 
    [Arguments]  ${password2}
    Input Text  password2  ${password2}

Create Tip 
    [Arguments]  ${url}  ${otsikko}  
    Input Text  url  ${url}
    Input Text  title  ${otsikko}
    Click Button  Lisää
