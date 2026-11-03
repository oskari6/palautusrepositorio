*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Register Page

*** Test Cases ***
Register With Matching Password And Confirmation
    Set Username  maija
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Welcome Page Should Be Open

Register With Matching Password Containing Special Character
    Set Username  maija
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Welcome Page Should Be Open

Register With Password Containing Only Lowercase Letters
    Set Username  maija
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or a special character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  maija
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain a number or a special character

Register With Different Password And Confirmation
    Set Username  maija
    Set Password  kalle123
    Set Password Confirmation  kalle124
    Click  button >> text=Register
    Register Should Fail With Message  Passwords do not match

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Username That Is Already In Use
    Create User  kalle  kalle123
    Set Username  kalle
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  short
    Set Password Confirmation  short
    Click  button >> text=Register
    Register Should Fail With Message  Password must be at least 8 characters long

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Welcome Page Should Be Open
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Reset Application And Go To Register Page
    Reset Application
    Go To  ${REGISTER_URL}
