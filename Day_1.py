"""
Name: Sahil Ranade
Batch: AIML
Day: 1 (9th August 2026)
Assignment: 1

Description:
Introduction to Python for AI/ML, data types, indexing and slicing,
conditional statements, and loops.
"""

# Why Python for AIML?

"""
Python is widely used for Artificial Intelligence and Machine Learning
because it is easy to learn, has a simple syntax, and provides many
powerful libraries for data analysis and model development.


"""


# Datatypes in Python

num = 10
num2 = 10.5
str1 = "Hello World"

print(type(num))
print(type(num2))
print(type(str1))


# Dictionary

dict = {"x": "sahil", "y": "yug", "z": "chinmay"}

print(dict["y"])


# List

list = ["sahil", 171, 9.9, True, {1: "rome"}, 8882222]

print(list[2])


# Indexing and Slicing

var = "Hey first day at deboistech"

print(var[0:6])
print(var[2:])
print(var[9:13])


# If-Else Statement

y = int(input("Enter Number: "))

if y > 0:
    print("Positive Number")
elif y < 0:
    print("Negative Number")
else:
    print("Zero")


# For Loop

for i in range(1, 6):
    print(i)


# While Loop

i = 1

while i <= 5:
    print(i)
    i += 1