"""
Module parking: Defines a Parking class for managing car parking.
"""

from car import Car, CarAlreadyParkedException, CarNotParkedException
from logger import logged, LogMode

class NoParkingLotException(Exception):
    """Exception raised when parking lot is full."""

class Parking:
    """Represents a parking lot with a capacity and hourly rate."""

    def __init__(self, max_capacity: int, hourly_rate: float):
        self.max_capacity = max_capacity
        self.hourly_rate = hourly_rate
        self.cars = []

    @logged(NoParkingLotException, LogMode.CONSOLE)
    def park_car(self, car: Car):
        """Park a car in the parking lot."""
        if len(self.cars) >= self.max_capacity:
            raise NoParkingLotException("Паркінг переповнений!")

        try:
            car.park()
        except CarAlreadyParkedException as e:
            print(f"Error parking car {car.plate_number}: {e}")
        else:
            self.cars.append(car)
            print(f"Автомобіль {car.plate_number} припарковано.")

    @logged(CarNotParkedException, LogMode.CONSOLE)
    def leave_parking(self, car: Car):
        """Remove a car from the parking lot and calculate the parking fee."""
        if car in self.cars:
            hours_parked = car.leave()
            price = hours_parked * self.hourly_rate
            print(f"Автомобіль {car.plate_number} залишає паркінг. "
                  f"Час на паркінгу: {hours_parked:.2f} годин. Ціна: {price:.2f} грн.")
            self.cars.remove(car)
        else:
            print(f"Автомобіль {car.plate_number} не знайдено на паркінгу.")

    def sort_by_duration(self):
        """Sort the cars by the duration they have been parked."""
        self.cars.sort(key=lambda car: car.parking_duration(), reverse=True)

    def print_cars(self):
        """Print all cars currently parked."""
        for car in self.cars:
            print(f"{car.plate_number} - {car.make.value}, модель: {car.model}, "
                  f"рік: {car.year}, припарковано: {car.parked_at}")
