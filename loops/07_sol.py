# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("okkk")
        break
    else:
        print("Invalid number, try again")