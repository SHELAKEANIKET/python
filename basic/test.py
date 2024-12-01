# print("hello world")

# def printName(name):
#     print(name)

# printName("Aniket Shelake")

# x = 10
# y = x

# print(x)
# print(y)

# x = 15
# print(x)
# print(y)

# * String
# str1 = "  hello world  "
# print(str1.strip())

# chai_type = "masala"
# quantity = 2
# order = "I ordered {} cups of {} chai"
# print(order.format(quantity,chai_type)) # placeholder


#! list to string conversion
# colors = ["orange","red","pink","green","yellow"]
# colors_string = " ".join(colors)
# colors_string = ", ".join(colors)
# print(colors_string)
# print(colors)

# ! string to list conversion
# stmt = "my name is aniket"
# list_conversion = stmt.split("")
# print(list_conversion)

# ! slicing
# color = "orange"
# print(color[4])
# print(color[:])
# print(color[1:])
# print(color[:3])
# print(color[1:3])


# ! Actual Scenario
#stmt = "he said "My name is Aniket"" # ? invalid syntax
# stmt = "he said \"My name is Aniket\""
# print(stmt)

# path = "c:user\aniket\desktop" # ? doesn't give proper answer
# print(path)
# sol 1 ->
# path1 = "c:user\\aniket\\desktop"
# print(path1)

# sol 2 -> mostly used
# path2 = r"c:user\aniket\desktop\folder"
# print(path2)

# * list
# colors = ["orange","red","pink","green","yellow"]
# print(colors[1])
# print(colors[:])
# print(colors[2:])
# print(colors[:2])

# colors[1] = "purple"
# print(colors)

# print(colors[1:1]) # returna empty array

# colors[1:1] = "violet"
# print(colors)

# colors[1:1] = ["violet"]
# print(colors)

# colors[1:1] = ["violet","cyan"]
# print(colors)

# colors[1:1] = []
# print(colors)

# tea_list = ["black","white","green","lemon","ginger"]

# tea_list_copy = tea_list # direct copy (same reference) it is shallow copy 
# tea_list_copy = tea_list.copy() # direct copy (same reference) it is deep copy  

# squared_nums  = [x**2 for x in range(10)]
# print(squared_nums)

# * dictionary
# cart_items = {"shirt" : "500", "pant" : "600", "cap" : "100", "shoes" : "2000"}

# for items in cart_items:
#     print(items, cart_items[items])


# for key,value in cart_items.items():
#     print(key,value)


# cube_nums = {x:x**3 for x in range(5)}
# print("before clear", cube_nums)
# cube_nums.clear()
# print("afrer clear", cube_nums)


# ! dictionary under dictionary
# shopping = { 
#     "flipcart" : {"shirt" : "500", "pant" : "600"},
#     "amazon" : { "laptop" : "50000", "mobile" : "20000"}
# }

# print(shopping)
# print(shopping["flipcart"])
# print(shopping["flipcart"]["shirt"])

# shopping["flipcart"]["cap"] = "100" # add new item in the dictionary
# print(shopping)

