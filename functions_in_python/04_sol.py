# Problem: Create a function that returns both the area and circumference of a circle given its radius.

import math


def circle_values (radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius

    return area,circumference

area,circumference = circle_values(3)

print("Area:",round(area,2), "Circumference:",round(circumference,2))
