order_size = "large"
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with the extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)