*** Settings ***
Library    CLILibrary.py
Documentation     A test suite for the end to end test which tests the cli version.
...               The class CLILibrary defines the necessary methods
...               The class triggers the processing via entering the command in a shell
...               First there is a check if the build exists
...                    otherwise the software gets build -> checks if the build process works
...               if the run ends positively, nothing happens
...               íf the run end negatively, the programm ends with an exception
*** Test Cases ***
Testcase 1
    [Documentation]    Testcase where no vulnerabilites get found - the programm ends positively
    Build Executable
    execute    -p ./tests/testdata/end2end/testcase1_noFindings

Testcase 2
    [Documentation]    Testcase where vulnerabilites get found - the programm ends negatively
    build_executable
    Run Keyword And Expect Error    *    execute  -p ./tests/testdata/end2end/testcase1_Findings

no Requirementsfile
    [Documentation]    Testcase where a wrong config gets entered - no Requirementsfile is defined or exists in project - the programm ends negatively
    build_executable
    Run Keyword And Expect Error    *    execute  -p ./tests/testdata/end2end/noRequirmentsFile

wrong config
    [Documentation]    Testcase where a wrong config gets entered - a wrong config is entered as input - the programm ends negatively
    build_executable
    Run Keyword And Expect Error    *    execute  -p ./tests/testdata/end2end/wrongConfig