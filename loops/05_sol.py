string = "radar"

for char in string:
    if string.count(char) == 1: # check if count is 1
        print("first non-repeating character is:", char)
        break
