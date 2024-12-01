# use of property decorator 

#! base / parent class
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
    
    # setter method
    def set_brand(self):
        return self.__brand + "!"

    def print_info(self):
        return f"brand:{self.__brand} model:{self.__model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_deacription():
        return "this is general description of a car"
    
    @property
    def access_model(self):
        return self.__model

#! derived / child class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

#* instances

my_car = Car("Tata","Safari")

# print(my_car.__model) # doesn't work
my_car.__model = "Nano"

print(my_car.access_model) # propert decoder allows to call the method like a attribute and it is read only.


#* note - use the property decoder so that object of that class can not access it directly
