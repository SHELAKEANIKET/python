# Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "yellow"

# method 1
if fruit == "Banana":
    if color == "green":
        print("unripe")
    elif color == "yellow":
        print("ripe")
    else:
        print("overripe")

