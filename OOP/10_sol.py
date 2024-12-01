# Multiple Inheritance - python supports multiple inheritance

#! base / parent class
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    
    # setter method
    def set_brand(self):
        return self.__brand + "!"

    def print_info(self):
        return f"brand:{self.__brand} model:{self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_deacription():
        return "this is general description of a car"

#! derived / child class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"



class Battery:
    def battery_info(self):
        return "this is battery info"

class Engine:
    def engine_info(self):
        return "This is engine info"


class NewElectricCar(Battery, Engine, Car):
    pass

#* instance

my_tesla_car = NewElectricCar("Tesla","Model X")

print(my_tesla_car.battery_info())
print(my_tesla_car.engine_info())