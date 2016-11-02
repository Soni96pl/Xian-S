@XIANS-21
@XIANS-19
Feature: Trips
	#In order to be able to log my trips
	#As an authorized user
	#I want to create a trip
	#I want to add segments of the trip
	#And I want to chose the transportation mode
	#And I want to chose the carrier
	#And I want to chose date and time
	#And I want to enter the price


	@XIANS-22 @XIANS-20
	Scenario: I want to add a new trip
		Given I authorize as "Jakub" with password "abc"
		When I make a authorized POST request to :trips
		    | name          | date          |
		    | America 2016  | 1465146000    |
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result


	@XIANS-23 @XIANS-20
	Scenario: I want to get trip details
		Given I authorize as "Jakub" with password "abc"
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip is 0/_id from a result
		When I make a authorized GET request to :trips/[trip]
		Then I have a JSON response
		    And I have a ListType result
		    And 0/name equals "America 2016" in a result
