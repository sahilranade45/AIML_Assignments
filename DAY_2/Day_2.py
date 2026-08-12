"""
Name: Sahil Ranade
Batch: AIML
Day: 2 (10th August 2026)
Assignment: 2

Description:
Python operators, variables, comments, input/output, type conversion,
built-in functions, and comparison operators.
"""


# Arithmetic Operators

a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

print("Exponent:", a ** b)
print("Modulus:", a % b)
print("Floor Division:", a // b)
print("Division:", a / b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)


# String Concatenation

a = "sahil"
b = "rohan"
c = " "

d = a + c + b

print(d)


# String Repetition

a = "happy"

b = a * 2

print(b)


# Variables

"""
Variable rules:

- A variable cannot start with a number.
- A variable can contain letters, numbers and underscores.
- Python keywords cannot be used as variable names.
"""

var1 = 3.14
print(var1)

var2 = "alice"
print(var2)


# Comments

# This is a single-line comment


# Input and Print

name = input("Enter your name: ")

print("Hello", name)


# Length

a = len("heyyyy")

print(a)


# Type Conversion

# str() - converts to string
# int() - converts to integer
# float() - converts to float

print("My" + " " + str(1000) + "s" + " " + "of assignments are pending.")

a = "100"
num = int(a)

print(num)

b = "10.5"
deci = float(b)

print(deci)


# Round Function

print(round(2233.7))
print(round(30.2456))


# Absolute Function

print(abs(-176))

a = int(input("Enter num: "))

print(abs(a))


# Comparison Operators

a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

if a == b:
    print("Numbers are equal")

elif a != b:
    print("Numbers are not equal")

elif a < b:
    print(a, "is less than", b)

elif a > b:
    print(a, "is greater than", b)

elif a <= b:
    print(a, "is less than or equal to", b)

elif a >= b:
    print(a, "is greater than or equal to", b)