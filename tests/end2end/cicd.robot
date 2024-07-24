*** Settings ***
Library    GitHubCICDActionsLibrary.py
Documentation     A test suite for the end to end test which tests the ci cd pipeline.

*** Test Cases ***
Failure Job
    Trigger_Workflow    testFailure.yml
    Run Keyword And Expect Error    Workflow failed    Check_Status

Positve Job
    Trigger_Workflow    testSuccess.yml