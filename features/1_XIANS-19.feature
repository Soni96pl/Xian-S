@XIANS-21
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
		    """
		    {
		        "name": "America 2016",
		        "date": {"$date": 1465146000000}
		    }
		    """
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
		When I make a authorized PATCH request to :trips/[trip_id]/name
		    """
		    "Asia 2016"
		    """
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
		    And I have a DictType result
		    And name equals "Asia 2016" in a result	

	
	@XIANS-24 @XIANS-20
	Scenario: I want to add transport to the trip
		Given I authorize as "Jakub" with password "abc"
		  And I define that departure_city is "Hong Kong"
		  And I define that arrival_city is "Chiang Mai"
		When I make a GET request to :cities/[departure_city]
		Then I have a JSON response
		    And I have a ListType result
		    And I define that departure_city_id is 0/_id from a result
		When I make a GET request to :cities/[arrival_city]
		Then I have a JSON response
		    And I have a ListType result
		    And I define that arrival_city_id is 0/_id from a result
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is 0/_id from a result
		When I make a authorized PATCH request to :trips/[trip_id]/transport
		    """
		    {
		        "carrier": {
		            "name": "DragonAir"
		        },
		        "code": "KA232",
		        "mode": "FLIGHT",
		        "departure": {
		            "station": {
		                "name": "Hong Kong International Airport",
		                "type": "AIRPORT",
		                "city": [departure_city_id]
		            },
		            "time": {"$date": 1467781200000}
		        },
		        "arrival": {
		            "station": {
		                "name": "Chiang Mai International Airport",
		                "type": "AIRPORT",
		                "city": [arrival_city_id]
		            },
		            "time": {"$date": 1467792000000}
		        }
		    }
		    """
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
		When I make a authorized PATCH request to :trips/[trip_id]/transport/0
		    """
		    {
		        "price": {
		            "value": 100.00,
		            "currency": "USD"
		        }
		    }
		    """
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
		When I make a authorized DELETE request to :trips/[trip_id]/transport/0
		Then I have a JSON response
		    And I have a DictType result
		    And success equals true in a result	

	
	@XIANS-29 @XIANS-20
	Scenario: I want to add lodging.
		Given I authorize as "Jakub" with password "abc"
		  And I define that city is "Kuala Lumpur"
		When I make a GET request to :cities/[city]
		Then I have a JSON response
		    And I have a ListType result
		    And I define that city_id is 0/_id from a result
		When I make a authorized GET request to :trips
		Then I have a JSON response
		    And I have a ListType result
		    And I define that trip_id is 0/_id from a result
		When I make a authorized PATCH request to :trips/[trip_id]/lodging
		    """
		    {
		        "city": [city_id],
		        "check_in": {"$date": 1480507200000},
		        "check_out": {"$date": 1480845600000},
		        "property": {
		            "name": "Irsia Bed and Breakfast",
		            "type": "BNB",
		            "location": {
		                "address": "Lorong 1/77a, Imbi, 55100 Kuala Lumpur, Wilayah Persekutuan Kuala Lumpur, Malaysia",
		                "coordinates": [3.141482, 101.709702],
		                "instructions": "Off Jalan Pudu (Behind Berjaya Times Square)"
		            },
		            "contact": {
		                "phone": 60333411077,
		                "email": "irsiabnb@reservations.com"
		            }
		        },
		        "room": {
		            "name": "Standard 4 Bed Mixed Dorm",
		            "type": "DORM"
		        },
		        "balance": {
		            "deposit": {
		                "value": 2.11,
		                "currency": "USD"
		            },
		            "remaining": {
		                "value": 60.72,
		                "currency": "MYR"
		            }
		        }
		    }
		    """
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