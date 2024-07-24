*** Settings ***
Library    CLILibrary.py
Documentation     A test suite for the end to end test.

*** Test Cases ***
Testcase 1
    Build Executable
    execute    -p ./tests/testdata/end2end/testcase1_noFindings

Testcase 2
    build_executable
    Run Keyword And Expect Error    *    execute  -p ./tests/testdata/end2end/testcase1_Findings

no Requirementsfile
    build_executable
    Run Keyword And Expect Error    *    execute  -p ./tests/testdata/end2end/noRequirmentsFile

wrong config
    build_executable
    Run Keyword And Expect Error    *    execute  -p ./tests/testdata/end2end/wrongConfig