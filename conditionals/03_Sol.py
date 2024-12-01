# Grade Calculator
#Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = 165

if score >= 101:
    print("Please verify your grade again")
    exit()

#!  method 1
if score >= 90 and score <= 100:
    print("A grade")
elif score >= 80 and score < 90:
    print("B grade")
elif score >= 70 and score < 80:
    print("C grade")
elif score >= 60 and score < 70:
    print("D grade")
else:
    print("F grade")

#! method 2
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade", grade)


    