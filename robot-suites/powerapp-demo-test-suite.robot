*** Variables ***
${URL}          
${USERNAME}
${PASSWORD}

*** Settings ***
Library     powerapp/PowerAppDemo.py

*** Test Case ***
Access the published Help desk Power App in Web browser
    [Tags]  UAT     Positive
    open the help desk power app    ${URL}
    login to microsoft with username and password  ${USERNAME}  ${PASSWORD}
    assert help desk app home page displayed
    close the app


Login as a Help desk user and validate successful login
    [Tags]  UAT     Positive
    open help desk app  ${URL}  ${USERNAME}  ${PASSWORD}
    login as a help desk user
    assert login as a help desk user success
    close the app


Logout of Help desk App and validate successful logout
    [Tags]  UAT     Positive
    open help desk app  ${URL}  ${USERNAME}  ${PASSWORD}
    login as a help desk user
    logout of the help desk app
    assert help desk app home page displayed
    close the app


# Negative Use case
Being a low previliged user Attempt to Login as a Help desk Admin should display error
    [Tags]  Negative
    open help desk app  ${URL}  ${USERNAME}  ${PASSWORD}
    login as a help desk admin
    assert no admin privilege error displayed
    close the app


*** Keywords ***
Open help desk app
    [Arguments]     ${URL}      ${USERNAME}     ${PASSWORD}
    open the help desk power app   ${URL}
    login to microsoft with username and password   ${USERNAME}     ${PASSWORD}
    assert help desk app home page displayed
