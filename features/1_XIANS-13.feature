@XIANS-15
@XIANS-13
Feature: Favorites
	#In order to have a list of favorite places
	#As an authorized user
	#I want to add places to the favorites
	#I want to remove places from the favorites
	#I want to list favorite

	
	@XIANS-16 @XIANS-14
	Scenario: I want to add a favorite with a given name
		Given I authorize as "Jakub" with password "abc"
		    And I define that city is "Bangkok"
		When I make a GET request to :city/[city]
		Then I have a JSON response
		    And I define that id is /0/id from a result
		When I make a authorized PUT request to :favorite/[id]
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result	

	
	@XIANS-17 @XIANS-14
	Scenario: I want to remove a favorite with a given name
		Given I authorize as "Jakub" with password "abc"
		    And I define that city is "Bangkok"
		When I make a GET request to :city/[city]
		Then I have a JSON response
		    And I define that id is /0/id from a result
		When I make a authorized DELETE request to :favorite/[id]
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result