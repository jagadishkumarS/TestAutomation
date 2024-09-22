*** Settings ***
Library     SeleniumLibrary
Library     customResult.py
Library     CustomListener.py


*** Variables ***


*** Test Cases ***
Test 1
    [Teardown]  Run Keyword    AggFunction             ${TEST_NAME}    Test1234   ${TEST_STATUS}   Test
    Log to Console          message




Test 2
    [Teardown]   Run Keyword    AggFunction             ${TEST_NAME}    Test125442   ${TEST_STATUS}   Test message 2
    Log to Console

Test 3
    [Teardown]   Run Keyword    AggFunction    ${TEST_NAME}    Test125442   ${TEST_STATUS}   Test message 3
    Log To Console    message 3
