# Introduction to Python Programming

## Basic Syntax and Data Types

# This is a comment in Python - it starts with a # symbol
print("Hello World!")  # This prints text to the console

# Variables and Basic Data Types
name = "Alice"        # String - text enclosed in quotes
age = 25             # Integer - whole number
height = 5.7         # Float - decimal number
is_student = True    # Boolean - True or False

# Basic Operations
x = 10
y = 3

print(x + y)    # Addition: 13
print(x - y)    # Subtraction: 7
print(x * y)    # Multiplication: 30
print(x / y)    # Division: 3.3333...
print(x // y)   # Floor division: 3
print(x % y)    # Modulus (remainder): 1
print(x ** y)   # Exponentiation: 1000

# String Operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # String concatenation
print(full_name)  # Output: John Doe

# String methods
message = "hello, world!"
print(message.upper())      # HELLO, WORLD!
print(message.capitalize()) # Hello, world!
print(len(message))        # 13 (length of string)

# Lists - ordered, mutable collections
fruits = ["apple", "banana", "orange"]
print(fruits[0])       # First item: apple
fruits.append("grape") # Add item to end
print(fruits)         # ['apple', 'banana', 'orange', 'grape']

# Basic Input
user_input = input("Enter your name: ")  # Gets input from user
print("Hello, " + user_input + "!")

# Simple if statement
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Basic loop
for i in range(5):  # Prints numbers 0 to 4
    print(i)

# While loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1


