@XIANS-19
Feature: Trips
	#In order to be able to log my trips
	#As an authorized user
	#I want to create a trip
	#I want to add transport to the trip
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
		    And I define that trip_id is /0/_id from a result
		When I make a authorized GET request to :trips/[trip_id]
		Then I have a JSON response
		    And I have a ListType result
		    And 0/name equals "America 2016" in a result	

	
	@XIANS-24 @XIANS-20
	Scenario: I want to add transport to the trip
		Given I authorize as "Jakub" with password "abc"
		  And I define that origin is "Hong Kong"
		  And I define that destination is "Chiang Mai"
		When I make a GET request to :cities/[origin]
		Then I have a JSON response
		    And I have a ListType result
		    And I define that origin_id is 0/_id from a result
		When I make a GET request to :cities/[destination]
		Then I have a JSON response
		    And I have a ListType result
		    And I define that destination_id is 0/_id from a result
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is 0/_id from a result
		When I make a authorized POST request to :trips/[trip_id]/transport
		  | origin_id   | destination_id    | departure   | arrival    |
		  | [origin_id] | [destination_id]  | 1467781200  | 1467792000 |
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result	

	
	@XIANS-25 @XIANS-20
	Scenario: I want to update transport of a trip
		Given I authorize as "Jakub" with password "abc"
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is 0/_id from a result
		    And I define that transport_id is 0/transport/0/_id from a result
		    And I define that origin_id is 0/transport/0/origin_id from a result
		    And I define that destination_id is 0/transport/0/destination_id from a result
		    And I define that departure is 0/transport/0/departure from a result
		    And I define that arrival is 0/transport/0/arrival from a result
		    And I convert departure to timestamp
		    And I convert arrival to timestamp
		When I make a authorized POST request to :trips/[trip_id]/transport/[transport_id]
		  | origin_id   | destination_id    | departure   | arrival     | price |
		  | [origin_id] | [destination_id]  | [departure] | [arrival]   | 10    |
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result
			

	
	@XIANS-26 @XIANS-20
	Scenario: I want to remove transport from a trip
		Given I authorize as "Jakub" with password "abc"
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is 0/_id from a result
		    And I define that transport_id is 0/transport/0/_id from a result
		When I make a authorized DELETE request to :trips/[trip_id]/transport/[transport_id]
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result	

	
	@XIANS-27 @XIANS-20
	Scenario: I want to update a trip
		Given I authorize as "Jakub" with password "abc"
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is /0/_id from a result
		When I make a authorized POST request to :trips/[trip_id]
		    | name      | date          |
		    | Asia 2016 | 1465146000    |
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result	

	
	@XIANS-28 @XIANS-20
	Scenario: I want to remove a trip
		Given I authorize as "Jakub" with password "abc"
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is /0/_id from a result
		When I make a authorized DELETE request to :trips/[trip_id]
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result