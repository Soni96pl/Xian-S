@XIANS-9
@XIANS-7
Feature: Users
	#In order to personalize the website
	#Users should be able to sign up
	#And login
	#And logout

	
	@XIANS-10 @XIANS-8
	Scenario: I want to signup
		When I make a POST request to :users
		    """
		    {
		        "name": "Jakub",
		        "password": "abc",
		        "email": "jakub@chronow.ski"
		    }
		    """
		Then I have a JSON response
		    And I have a DictType result
		    And /success equals true in a result
		    And /message equals "Document upserted successfully." in a result	

	
	@XIANS-12 @XIANS-8
	Scenario: I want to auth
		When I make a POST request to :auth
		    """
		    {
		        "name": "Jakub",
		        "password": "abc"
		    }
		    """
		Then I have a JSON response
		    And I have a DictType result
		    And "access_token" is in a result