# Problem: Reverse a string using a loop.

user_string = input("Enter your string: ")

reversed_str = ""

for char in user_string:
    # print(char + reversed_str)
    reversed_str = char + reversed_str

print(reversed_str)