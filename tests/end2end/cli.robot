*** Settings ***
Library    Process
Documentation     A test suite for the end to end test.

*** Test Cases ***
Testcase 1
    Run Process ./dist/SecurityScannerSchadow.exe 

no Requirementsfile
    [Tags]    negative
    Connect to Server
    Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123
    Verify Unauthorised Access