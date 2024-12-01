# use of isinstance() function

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

#* instances

my_car = Car("Tata","Safari")

my_electric_car = ElectricCar("Tesla","Model S", "80kWh")


print(isinstance(my_electric_car,ElectricCar))
print(isinstance(my_electric_car,Car))
