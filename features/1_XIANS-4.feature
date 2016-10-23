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
			And country equals "PL" somewhere in a result
			And coordinates equals [52.22977, 21.01178] somewhere in a result	

	
	@XIANS-5 @XIANS-3
	Scenario: I want to get details of a plase with a given name.
		Given I define that city is "Chiang Mai"
		When I make a GET request to :city/[city]
		Then I have a JSON response
		Then I define that id is /0/id from a result
		When I make a GET request to :city/[id]/details
		Then I have a JSON response
			And I have a ListType result
			And /0/country equals "TH" in a result
			And /0/story/content contains "Northern" in a result
		