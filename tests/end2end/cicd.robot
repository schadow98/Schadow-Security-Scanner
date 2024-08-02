*** Settings ***
Library    GitHubCICDActionsLibrary.py
Documentation     A test suite for the end to end test which tests the ci cd pipeline.
...               The class GitHubCICDActionsLibrary defines the necessary methods
...               The workflow gets triggered via the REST-API
...               The other method checks the status via the same REST-API
...               if the run ends positively, nothing happens
...               íf the run end negatively, the method raises an error called "Workflow failed"

*** Test Cases ***
Failure Job
    [Documentation]    Test if the workflow/ pipeline failes when there are vulnerabilites and the further build-Process gets stopped
    Trigger_Workflow    testFailure.yml
    Run Keyword And Expect Error    Workflow failed    Check_Status

Positve Job
    [Documentation]    Test if the workflow/ pipeline success when no vulnerabilites are in the repository
    Trigger_Workflow    testSuccess.yml