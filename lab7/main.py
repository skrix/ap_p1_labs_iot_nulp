"""
Module main: Creates objects for presentation of task solution.
"""

from car import Car, CarBrand, CarEngine, EngineType, FuelType
from parking import Parking

def main():
    """Main function to create cars and manage parking."""
    print("\nСтворюємо паркінг з максимальною кількістю 3 місця і ціною за годину 20 грн")
    parking = Parking(max_capacity=3, hourly_rate=20.0)

    engine1 = CarEngine({
        'engine_type': EngineType.V6,
        'volume': 3000,
        'horse_power': 420,
        'top_speed': 280,
        'fuel': FuelType.PETROL
    })
    engine2 = CarEngine({
        'engine_type': EngineType.I4,
        'volume': 1590,
        'horse_power': 350,
        'top_speed': 210,
        'fuel': FuelType.DIESEL
    })
    engine3 = CarEngine({
        'engine_type': EngineType.V8,
        'volume': 4000,
        'horse_power': 500,
        'top_speed': 320,
        'fuel': FuelType.PETROL
    })
    engine4 = CarEngine({
        'engine_type': EngineType.I4,
        'volume': 1390,
        'horse_power': 180,
        'top_speed': 220,
        'fuel': FuelType.PETROL
    })

    print("\nСтворюємо автомобілі з двигунами")
    car1 = Car({
        'make': CarBrand.BMW,
        'model': "M3",
        'year': 2020,
        'plate_number': "AA1234BB",
        'engine': engine1
    })
    car2 = Car({
        'make': CarBrand.AUDI,
        'model': "A6",
        'year': 2018,
        'plate_number': "AA5678CC",
        'engine': engine2
    })
    car3 = Car({
        'make': CarBrand.TOYOTA,
        'model': "Camry",
        'year': 2019,
        'plate_number': "AB1122DD",
        'engine': engine3
    })
    car4 = Car({
        'make': CarBrand.FORD,
        'model': "Focus",
        'year': 2017,
        'plate_number': "AE9988FF",
        'engine': engine4
    })

    print("\nПаркуємо машини")
    parking.park_car(car1)
    parking.park_car(car2)
    parking.park_car(car3)

    print("\nСпроба запаркувати 4 машину на переповнений паркінг")
    parking.park_car(car4)

    print("\nСпроба випаркувати не запарковану машину")
    parking.leave_parking(car4)

    print("\nВиведення інформації про всі автомобілі на паркінгу")
    parking.print_cars()

    print("\nАвтомобіль залишає паркінг")
    parking.leave_parking(car1)

    print("\nСпроба запаркувати вже запарковану машину")
    parking.park_car(car3)

    print("\nВиведення інформації після виходу одного автомобіля")
    parking.print_cars()

    print("\nСортуємо машини за тривалістю стоянки")
    parking.sort_by_duration()

    print("\nВідсортовані машини за тривалістю стоянки:")
    parking.print_cars()

if __name__ == "__main__":
    main()
