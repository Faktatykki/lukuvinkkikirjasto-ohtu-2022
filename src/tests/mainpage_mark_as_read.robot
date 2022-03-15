*** Settings ***
Resource		resource.robot
Suite Setup		Configure Browser And Login
Suite Teardown	Logout And Close All Browsers
Test Setup		Go To Mainpage

*** Variables ***
&{user}			username=marker					password=salasana
&{user_two}		username=marker_two				password=salasana2
&{usertip}		title=Marker's test				url=https://marker.example.com/filtering-test
&{anontip}		title=Anonymous' marker tip		url=https://marker-anon.example.com/filtering-test

*** Test Cases *** 
Logged User Can Mark Tip As Read
	Page Should Contain			${anontip}[title]
	Page Should Contain Link	Merkitse luetuksi
	Click Element				//a[@class="markAsRead"][1]
	Page Should Contain Link	Merkitse lukemattomaksi

Logged User Can Mark Tip As Unread
	Page Should Contain Link	Merkitse lukemattomaksi
	Click Element				//a[@class="markAsRead"][1]
	Page Should Contain Link	Merkitse luetuksi

Marking Tip As Read Doesnt Change Status For Another User
	Click Element					//a[@class="markAsRead"][1]
	Page Should Contain Link		Merkitse lukemattomaksi
	Click Link						logout
	Go To Signuppage
	Signuppage Should Be Open
	Input Text						username	${user_two}[username]
	Input Text						password1	${user_two}[password]
	Input Text						password2	${user_two}[password]
	Click Button					submit
	Page Should Contain				${user_two}[username] kirjautuneena
	Go To Mainpage
	Mainpage Should Be Open
	Page Should Not Contain Link	Merkitse lukemattomaksi

*** Keywords ***
Configure Browser And Login
	Open And Configure Browser
	Create Tip  ${anontip}[title]  ${anontip}[url]
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
