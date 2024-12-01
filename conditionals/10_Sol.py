# Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

species = "Cat"
age = 2

if species == "Cat":
    if age<2:
        print("babbie cat food")
    else:
        print("senior cat food")

elif species == "Dog":
    if age<2:
        print("puppy food")
    else:
        print("senior Dog food")