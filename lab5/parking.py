from car import Car

class Parking:
    def __init__(self, max_capacity: int, hourly_rate: float):
        self.max_capacity = max_capacity
        self.hourly_rate = hourly_rate
        self.cars = []

    def park_car(self, car: Car):
        if len(self.cars) >= self.max_capacity:
            print("Паркінг переповнений!")
            return
        car.park()
        self.cars.append(car)
        print(f"Автомобіль {car.plate_number} припарковано.")

    def leave_parking(self, car: Car):
        if car in self.cars:
            hours_parked = car.leave()
            price = hours_parked * self.hourly_rate
            print(f"Автомобіль {car.plate_number} залишає паркінг. Час на паркінгу: {hours_parked:.2f} годин. Ціна: {price:.2f} грн.")
            self.cars.remove(car)
        else:
            print(f"Автомобіль {car.plate_number} не знайдено на паркінгу.")

    def sort_by_duration(self):
        self.cars.sort(key=lambda car: car.parking_duration(), reverse=True)

    def print_cars(self):
        for car in self.cars:
            print(f"{car.plate_number} - {car.make.value}, модель: {car.model}, рік: {car.year}, припарковано: {car.parked_at}")
