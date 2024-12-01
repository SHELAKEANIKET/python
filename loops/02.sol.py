# Problem: Calculate the sum of even numbers up to a given number n.

number = 15
sum_of_even = 0

for num in range(1,number):
    if num % 2 == 0:
        sum_of_even += num

print(sum_of_even)

