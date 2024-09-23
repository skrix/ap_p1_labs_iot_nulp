import pytest
from car import Car, CarBrand, CarEngine, EngineType, FuelType
from parking import Parking
from datetime import datetime, timedelta

@pytest.fixture
def parking():
    """Fixture for setting up a sample parking lot."""
    return Parking(max_capacity=2, hourly_rate=20.0)

@pytest.fixture
def car1():
    """Fixture for setting up the first car."""
    engine = CarEngine({
        'volume': 3000,
        'engine_type': EngineType.V6,
        'fuel': FuelType.PETROL,
        'horse_power': 420,
        'top_speed': 280
    })
    return Car({
        'make': CarBrand.BMW,
        'model': 'M3',
        'year': 2020,
        'plate_number': 'AA1234BB',
        'engine': engine
    })

@pytest.fixture
def car2():
    """Fixture for setting up the second car."""
    engine = CarEngine({
        'volume': 2000,
        'engine_type': EngineType.I4,
        'fuel': FuelType.DIESEL,
        'horse_power': 320,
        'top_speed': 240
    })
    return Car({
        'make': CarBrand.AUDI,
        'model': 'A4',
        'year': 2019,
        'plate_number': 'AA5678CC',
        'engine': engine
    })

def test_park_car(parking, car1):
    """Test parking a car."""
    parking.park_car(car1)
    assert len(parking.cars) == 1
    assert car1 in parking.cars

def test_park_car_over_capacity(parking, car1, car2):
    """Test trying to park when parking is full."""
    parking.park_car(car1)
    parking.park_car(car2)

    # Trying to park a third car when capacity is 2
    car3 = Car({
        'make': CarBrand.TOYOTA,
        'model': 'Camry',
        'year': 2021,
        'plate_number': 'AA9988ZZ',
        'engine': CarEngine({
            'volume': 2500,
            'engine_type': EngineType.V6,
            'fuel': FuelType.PETROL,
            'horse_power': 350,
            'top_speed': 260
        })
    })

    parking.park_car(car3)
    assert len(parking.cars) == 2  # The third car should not be parked

def test_leave_parking(parking, car1):
    """Test leaving the parking lot and calculating the price."""
    parking.park_car(car1)
    car1.parked_at = datetime.now() - timedelta(hours=3)  # Simulate 3 hours of parking

    parking.leave_parking(car1)
    assert len(parking.cars) == 0
