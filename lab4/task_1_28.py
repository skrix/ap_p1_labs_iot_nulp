import textwrap

class WaterPump:
  def __init__(self, brand=None, watt=None, capacity=None, model=None, serial=None, manufacture_year=None):
    self.__brand = brand
    self.__watt = watt
    self.__capacity = capacity
    self.model = model
    self.serial = serial
    self.manufacture_year = manufacture_year

  def get_brand(self):
    return self.__brand

  def get_watt(self):
    return self.__watt

  def get_capacity(self):
    return self.__capacity

  def __str__(self):
    return f'WaterPump: {self.__brand}, {self.__watt} Watt power, {self.__capacity} l/h capacity'

  def __repr__(self):
    return textwrap.dedent(f'''
    Record: WaterPump
    Brand: {self.__brand}
    Model: {self.model}
    Serial: {self.serial}
    Year: {self.manufacture_year}
    Power: {self.__watt} watt
    Capacity: {self.__capacity} l/h
    ''')

  def __del__(self):
    print(f"{self.__str__()} deleted.")


def main():
  obj1 = WaterPump()
  obj2 = WaterPump('Bosch', 48, 996, 'Bosch Water Pump 16.6l / Minute 12V', 'BO-EWP004', 2024)
  obj3 = WaterPump('BGA', model='Water Pump Fiat Combo/Doblo/Ducato 1.6/2.0D/CDTi 10-', serial='CP2660', manufacture_year=2024)
  print(obj1.__repr__())
  print(obj2.__repr__())
  print(obj3.__repr__())

main()
