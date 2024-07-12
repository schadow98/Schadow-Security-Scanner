*** Settings ***
Documentation     A test suite for the end to end test.
...
...               Keywords are imported from the resource file
Default Tags      positive

*** Test Cases ***
Found No Vulnaribilities
    Connect to Server
    Login User            ironman    1234567890
    Verify Valid Login    Tony Stark


Denied Login with Wrong Password
    [Tags]    negative
    Connect to Server
    Run Keyword And Expect Error    *Invalid Password    Login User    ironman    123
    Verify Unauthorised Access