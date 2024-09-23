from enum import Enum
from datetime import datetime


class CarBrand(Enum):
    ACURA = "Acura"
    ALFA_ROMEO = "Alfa Romeo"
    ASTON_MARTIN = "Aston Martin"
    AUDI = "Audi"
    BMW = "BMW"
    CHEVROLET = "Chevrolet"
    DODGE = "Dodge"
    FIAT = "Fiat"
    FORD = "Ford"
    HONDA = "Honda"
    HYUNDAI = "Hyundai"
    INFINITI = "Infiniti"
    JAGUAR = "Jaguar"
    JEEP = "Jeep"
    KIA = "Kia"
    LAMBORGHINI = "Lamborghini"
    LAND_ROVER = "Land Rover"
    LEXUS = "Lexus"
    MAZDA = "Mazda"
    MERCEDES_BENZ = "Mercedes-Benz"
    MITSUBISHI = "Mitsubishi"
    NISSAN = "Nissan"
    PEUGEOT = "Peugeot"
    PORSCHE = "Porsche"
    RENAULT = "Renault"
    SEAT = "Seat"
    SKODA = "Skoda"
    SUBARU = "Subaru"
    SUZUKI = "Suzuki"
    TOYOTA = "Toyota"
    VOLKSWAGEN = "Volkswagen"
    VOLVO = "Volvo"

class FuelType(Enum):
    PETROL = "Petrol"
    DIESEL = "Diesel"
    ELECTRIC = "Electric"
    HYBRID = "Hybrid"

class EngineType(Enum):
    I4 = "Inline 4"
    V6 = "V6"
    V8 = "V8"
    V12 = "V12"

class CarEngine:
    def __init__(self, volume: int, type: EngineType, fuel: FuelType, horse_power: int, top_speed: int):
        self.volume = volume
        self.type = type
        self.fuel = fuel
        self.horse_power = horse_power
        self.top_speed = top_speed

    def __str__(self):
        return f"{self.type.value}, {self.volume}cc, {self.horse_power}HP, {self.top_speed}KM/h, Fuel: {self.fuel.value}"

class Car:
    def __init__(self, make: CarBrand, model: str, year: int, plate_number: str, engine: CarEngine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.plate_number = plate_number
        self.parked_at = None

    def parking_duration(self):
        if self.parked_at is None:
            return 0
        else:
            return (datetime.now() - self.parked_at).total_seconds() / 3600.0


    def park(self):
        self.parked_at = datetime.now()

    def leave(self):
        duration = self.parking_duration()
        self.parked_at = None
        return duration
