# Encapsulation
#! base / parent class
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    def set_brand(self):
        return self.__brand + "!"

    def print_info(self):
        return f"brand:{self.__brand} model:{self.model}"

#! derived / child class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

#* instance
my_electric_car = ElectricCar("Tesla","Model S", "80kWh")
# print(my_electric_car.__brand) #? not directly accesible
print(my_electric_car.set_brand())
# print(my_electric_car.print_info())
# print(my_electric_car.battery_size)