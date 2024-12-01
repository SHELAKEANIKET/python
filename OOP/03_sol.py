# Inheritance
#! base / parent class
class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def print_info(self):
        return f"brand:{self.brand} model:{self.model}"

#! derived / child class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

#* instance
my_electric_car = ElectricCar("Tesla","Model S", "80kWh")
print(my_electric_car.print_info())
print(my_electric_car.battery_size)