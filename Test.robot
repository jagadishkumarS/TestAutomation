*** Settings ***
Library    SeleniumLibrary
Library    Screenshot

*** Test Cases ***
Open Application
    [Tags]    Test    Add
    open browser    https://www.amazon.co.in    chrome
    take screenshot


