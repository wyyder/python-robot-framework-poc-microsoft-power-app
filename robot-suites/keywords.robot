*** Variables ***
${URL}
${USERNAME}
${PASSWORD}

*** Settings ***
Library     powerapp/PowerAppDemo.py

*** Keywords ***
App Specific keywords
    [Arguments]     ${URL}      ${USERNAME}     ${PASSWORD}
    open the help desk power app   ${URL}
    login to microsoft with username and password   ${USERNAME}     ${PASSWORD}
    assert help desk app home page displayed
    login as a help desk user
    assert login as a help desk user success
    logout of the help desk app
    login as a help desk admin
    assert no admin privilege error displayed
    close the app