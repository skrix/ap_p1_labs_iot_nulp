import pytest
from car import Car, CarBrand, CarEngine, EngineType, FuelType
from datetime import datetime, timedelta

@pytest.fixture
def car_engine():
    """Fixture for setting up a sample car engine."""
    return CarEngine({
        'volume': 3000,
        'engine_type': EngineType.V6,
        'fuel': FuelType.PETROL,
        'horse_power': 420,
        'top_speed': 280
    })

@pytest.fixture
def car(car_engine):
    """Fixture for setting up a sample car."""
    return Car({
        'make': CarBrand.BMW,
        'model': 'M3',
        'year': 2020,
        'plate_number': 'AA1234BB',
        'engine': car_engine
    })

def test_engine_str(car_engine):
    """Test the string representation of the car engine."""
    assert str(car_engine) == "V6, 3000cc, 420HP, 280KM/h, Fuel: Petrol"

def test_car_initial_state(car):
    """Test that a car is initialized with correct values."""
    assert car.make == CarBrand.BMW
    assert car.model == 'M3'
    assert car.year == 2020
    assert car.parked_at is None

def test_car_park_and_duration(car):
    """Test car parking and the parking duration."""
    car.park()
    assert car.parked_at is not None

    car.parked_at = datetime.now() - timedelta(hours=2)
    duration = car.parking_duration()

    assert duration == pytest.approx(2, rel=1e-2)

def test_car_leave(car):
    """Test that leaving the parking lot resets the parked_at and returns the correct duration."""
    car.park()

    car.parked_at = datetime.now() - timedelta(hours=3)
    duration = car.leave()

    assert car.parked_at is None
    assert duration == pytest.approx(3, rel=1e-2)
