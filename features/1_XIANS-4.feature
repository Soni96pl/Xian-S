@XIANS-2
@XIANS-4
Feature: Places
	#In order to chose places to go
	#Users should be able to search them
	#And read their descriptions
	#And browse their pictures


	@XIANS-1 @XIANS-3
	Scenario: I want to find a place by its name.
		Given I define that city is "Warsaw"
		When I make a GET request to :city/[city]
		Then I have a JSON response
				And I have 8 results
				And country is "PL" for a result
				And coordinates is [52.22977, 21.01178] for a result
