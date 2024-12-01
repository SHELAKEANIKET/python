class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

my_car = Car("Tata","Safari")
print(my_car.brand)
print(my_car.model)

#? note - this __init__ is nothing but the 'constructor' and this self is nothing but 'this'