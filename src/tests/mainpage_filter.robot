
*** Settings ***
Resource		resource.robot
Suite Setup		Configure Browser And Login
Suite Teardown	Logout And Close All Browsers
Test Setup		Go To Mainpage

*** Variables ***
&{user}			username=filterer		password=salasana
&{usertip}		title=Filterer's test	url=https://filterer.example.com/filtering-test
&{anontip}		title=Anonymous' tip	url=https://anon.example.com/filtering-test

*** Test Cases *** 
Log Variables
	Log		user.username:${user}[username]
	Log		user.password:${user}[password]
	Log		tip.title:${usertip}[title]
	Log		tip.url:${usertip}[url]

User Can Hide Other Tips
	Page Should Contain		${anontip}[title]
	Click Element			ownTips
	Page Should Not Contain	${anontip}[title]

User Can View Own Tips
	Set Title				${usertip}[title]
	Set URL					${usertip}[url]
	Submit Vinkki
	Page Should Contain		${usertip}[title]
	Click Element			ownTips
	Page Should Contain		${usertip}[title]

*** Keywords ***
Configure Browser And Login
	Open And Configure Browser
	Go To Mainpage
	Set Title				${anontip}[title]
	Set URL					${anontip}[url]
	Submit Vinkki
	Go To Signuppage
	Signuppage Should Be Open
	Input Text				username	${user}[username]
	Input Text				password1	${user}[password]
	Input Text				password2	${user}[password]
	Click Button			submit
	Page Should Contain		${user}[username] kirjautuneena

Logout And Close All Browsers
	Click Link				logout
	Close All Browsers
