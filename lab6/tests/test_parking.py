"""
Test cases for the Parking class and its methods.
"""

from datetime import datetime, timedelta

def test_park_car(parking, car1):
    """Test parking a car."""
    parking.park_car(car1)
    assert len(parking.cars) == 1
    assert car1 in parking.cars

def test_park_car_over_capacity(parking, car1, car2):
    """Test trying to park when parking is full."""
    parking.park_car(car1)
    parking.park_car(car2)

    car3 = car1
    car3.plate_number = "AA9988ZZ"

    parking.park_car(car3)
    assert len(parking.cars) == 2  # The third car should not be parked

def test_leave_parking(parking, car1):
    """Test leaving the parking lot and calculating the price."""
    parking.park_car(car1)
    car1.parked_at = datetime.now() - timedelta(hours=3)  # Simulate 3 hours of parking

    parking.leave_parking(car1)
    assert len(parking.cars) == 0
