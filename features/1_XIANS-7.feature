@XIANS-9
@XIANS-7
Feature: Users
	#In order to personalize the website
	#Users should be able to sign up
	#And login
	#And logout

	
	@XIANS-10 @XIANS-8
	Scenario: I want to signup
		Given I define that name is "Jakub"
		    And I define that password is "abc"
		    And I define that email is "jakub@chronow.ski"
		When I make a POST request to :signup
		    | name  | password  | email             |
		    | Jakub | abc       | jakub@chronow.ski |
		Then I have a JSON response
		    And I have a DictType result
		    And /status equals "success"
		    And /message equals "Signed up successfully"