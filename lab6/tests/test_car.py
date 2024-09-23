"""
Test cases for the Car and CarEngine classes.
"""

from datetime import datetime, timedelta
import pytest
from car import CarBrand, EngineType, FuelType

def test_engine_str(create_engine):
    """Test the string representation of the car engine."""
    engine = create_engine(3000, EngineType.V6, FuelType.PETROL, 420, 280)
    assert str(engine) == "V6, 3000cc, 420HP, 280KM/h, Fuel: Petrol"

def test_car_initial_state(car1):
    """Test that a car is initialized with correct values."""
    assert car1.make == CarBrand.BMW
    assert car1.model == 'M3'
    assert car1.year == 2020
    assert car1.parked_at is None

def test_car_park_and_duration(car1):
    """Test car parking and the parking duration."""
    car1.park()
    assert car1.parked_at is not None

    # Simulate a time duration for testing
    car1.parked_at = datetime.now() - timedelta(hours=2)
    duration = car1.parking_duration()

    # The duration should be approximately 2 hours
    assert duration == pytest.approx(2, rel=1e-2)

def test_car_leave(car1):
    """Test that leaving the parking lot resets the parked_at and returns the correct duration."""
    car1.park()

    # Simulate parking for 3 hours
    car1.parked_at = datetime.now() - timedelta(hours=3)
    duration = car1.leave()

    assert car1.parked_at is None
    assert duration == pytest.approx(3, rel=1e-2)
