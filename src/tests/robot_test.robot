*** Settings ***
Resource  resource.robot


*** Test Cases ***
A Test Test Case
    A Test Should Run And Pass

*** Keywords ***
A Test Should Run And Pass
    Should Be True  1 < 2