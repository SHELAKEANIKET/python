# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key:value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")


print_kwargs(name="Aniket", country="India")
print_kwargs(name="Aniket")
print_kwargs(name="Aniket", country="India", age = 20)