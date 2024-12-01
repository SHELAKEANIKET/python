# Problem: Write a function that takes variable number of arguments and returns their sum.

def sum_of_numbers (*args):
    return sum(args)

print(sum_of_numbers(1,2,3))
print(sum_of_numbers(1,2,3,4,5))
print(sum_of_numbers(1,2,3,4,5,6,7))



#? investigation
#* point 1: what prints args
# def sum_of_numbers (*args):
#     print(args) # print the tuple of the args (parameters)
#     return sum(args)

#* point 2: what prints *args
# def sum_of_numbers (*args):
#     print(*args) # prints the numbers
#     return sum(args)

#* point 3: as args are numbers/tuple so we can loop on it
# def sum_of_numbers (*args):
#     sum = 0
    # for i in args:
    #     sum += i
    # print("sum",sum)


