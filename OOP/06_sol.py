# Inheritance
#! base / parent class
class Car:

    total_cars = 0

    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        Car.total_cars += 1

    def print_info(self):
        return f"brand:{self.brand} model:{self.model}"

#! derived / child class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

#* instance
my_electric_car = ElectricCar("Tesla","Model S", "80kWh")
# print(my_electric_car.print_info())
# print(my_electric_car.battery_size)

Car("Maruti Suzuki", "Swift")
Car("Toyoto", "Innova")

print(Car.total_cars)