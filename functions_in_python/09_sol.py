# Problem: Write a generator function that yields even numbers up to a specified limit.

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)


#? investigation

#! The yield keyword in Python turns a regular function into a generator, which produces a sequence of values on demand instead of computing them all at once.

#* point 1:
# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         return i # just return single value

# print(even_generator(5)) # just return the first value from function

# for num in even_generator(5):
#     print(num) # 'int' object is not iterable
