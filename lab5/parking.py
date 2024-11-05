"""
Module parking: Defines a Parking class for managing car parking.
"""

from car import Car
from datetime import datetime

class Parking:
    """Represents a parking lot with a capacity and hourly rate."""

    def __init__(self, max_capacity: int, hourly_rate: float):
        self.max_capacity = max_capacity
        self.hourly_rate = hourly_rate
        self.cars_logs = []

    def park_car(self, car: Car):
        """Park a car in the parking lot."""
        if len(self.cars_logs) >= self.max_capacity:
            print("Паркінг переповнений!")
            return
        car.park()
        self.__park_car(car)
        print(f"Автомобіль {car.plate_number} припарковано.")

    def leave_parking(self, car: Car):
        """Remove a car from the parking lot and calculate the parking fee."""
        parking_log = self.__find_car(car)
        if parking_log:
            self.__unpark_car(car)
            print(f"Автомобіль {parking_log['plate_number']} залишає паркінг. "
                  f"Час на паркінгу: {parking_log['parking_time_last']:.2f} годин. Ціна: {parking_log['parking_price_last']:.2f} грн."
                  f"Загальний час на паркінгу: {parking_log['parking_time_total']:.2f} годин. Загально оплачено: {parking_log['parking_price_total']:.2f} грн.")
        else:
            print(f"Автомобіль {car.plate_number} не знайдено на паркінгу.")

    # parking_log:
    # {
    #   plate_number: string,
    #   object: car,
    #   parkings: [
    #    { parked_at: DateTime,
    #      left_at: DateTime,
    #      time: float,
    #      price: float,
    #    },
    #    { parked_at: DateTime,
    #      left_at: DateTime,
    #      time: float,
    #      price: float,
    #    },
    #    { parked_at: DateTime,
    #      left_at: DateTime,
    #      time: float,
    #      price: float,
    #    },
    #   ],
    #   parking_time_total: float,
    #   parking_price_total: float,
    #   parking_time_last: float,
    #   parking_price_last: float
    # }
    #
    def __find_car(self, car: Car):
        for parking_log in self.cars_logs:
            if parking_log['plate_number'] == car.plate_number:
                return parking_log
            else:
                return None

    def __park_car(self, car: Car):
        parking_log = self.__find_car(car)
        if parking_log:
            parking_log['parkings'].append({
              'parked_at': car.parked_at,
              'left_at': None,
              'time': 0,
              'price': 0
            })
        else:
          self.cars_logs.append({
            'plate_number': car.plate_number,
            'object': car,
            'parkings': [{
              'parked_at': car.parked_at,
              'left_at': None,
              'time': 0,
              'price': 0
            }],
            'parking_time_total': 0,
            'parking_price_total': 0,
            'parking_time_last': 0,
            'parking_price_last': 0
          })

    def __unpark_car(self, car: Car):
        last_parking_time = car.leave()
        last_parking_price = self.__calculate_price(car, last_parking_time)
        parking_log = self.__find_car(car)
        parking_entry = parking_log['parkings'][-1]
        parking_entry['left_at'] = datetime.now()
        parking_entry['time'] = last_parking_time
        parking_entry['price'] = self.__calculate_price(car, last_parking_time)
        parking_log['parking_time_total'] = self.__calculate_total_time(parking_log['parkings'])
        parking_log['parking_price_total'] = self.__calculate_total_price(parking_log['parkings'])
        parking_log['parking_time_last'] = last_parking_time
        parking_log['parking_price_last'] = last_parking_price

    def __calculate_price(self, car: Car, hours_parked):
        price = hours_parked * self.hourly_rate
        if car.engine.horse_power > 200:
            return price * 1.05
        else:
            return price

    def __calculate_total_price(self, parking_entries):
        total_price = 0
        for parking_entry in parking_entries:
            total_price += parking_entry['price']
        return total_price

    def __calculate_total_time(self, parking_entries):
        total_time = 0
        for parking_entry in parking_entries:
            total_time += parking_entry['time']
        return total_time

    def sort_by_duration(self):
        """Sort the cars by the duration they have been parked."""
        self.cars_logs.sort(key=lambda car_log: car_log['parking_time_total'], reverse=True)

    def print_cars(self):
        """Print all cars currently parked."""
        for car_log in self.cars_logs:
            print(f"{car_log['object'].plate_number} - {car_log['object'].make.value}, модель: {car_log['object'].model}, "
                  f"рік: {car_log['object'].year}, припарковано: {car_log['object'].parked_at} pure: {car_log}")
