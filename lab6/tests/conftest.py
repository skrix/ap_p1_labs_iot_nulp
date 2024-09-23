"""
Shared fixtures for the test suite.
"""
import pytest
from car import Car, CarBrand, CarEngine, EngineType, FuelType
from parking import Parking

@pytest.fixture(name="create_engine")
def fixture_create_engine():
    """Helper fixture to create a car engine."""
    def _create_engine(volume, engine_type, fuel, horse_power, top_speed):
        return CarEngine({
            'volume': volume,
            'engine_type': engine_type,
            'fuel': fuel,
            'horse_power': horse_power,
            'top_speed': top_speed
        })
    return _create_engine

@pytest.fixture
def car1(create_engine):
    """Fixture for setting up the first car."""
    engine_instance = create_engine(3000, EngineType.V6, FuelType.PETROL, 420, 280)
    return Car({
        'make': CarBrand.BMW,
        'model': 'M3',
        'year': 2020,
        'plate_number': 'AA1234BB',
        'engine': engine_instance
    })

@pytest.fixture
def car2(create_engine):
    """Fixture for setting up the second car."""
    engine_instance = create_engine(2000, EngineType.I4, FuelType.DIESEL, 320, 240)
    return Car({
        'make': CarBrand.AUDI,
        'model': 'A4',
        'year': 2019,
        'plate_number': 'AA5678CC',
        'engine': engine_instance
    })

@pytest.fixture
def parking():
    """Fixture for setting up a sample parking lot."""
    return Parking(max_capacity=2, hourly_rate=20.0)
