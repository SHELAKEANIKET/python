class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def print_info(self):
        return f"brand:{self.brand} model:{self.model}"

my_car = Car("Tata","Safari")
print(my_car.brand)
print(my_car.model)
print(my_car.print_info()) # it is method