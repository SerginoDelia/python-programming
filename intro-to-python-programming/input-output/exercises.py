# Exercises
# 1. Write a program named greeter.py. The program should ask for your name, 
# then output Hello, NAME! where NAME is the name you entered:

# $ python greeter.py
# What is your name? Sue
# Hello, Sue!

name = input('What is your name? ')
print(f'Hello, {name}!')

# 2. Modify the greeter.py program to ask for the user's first and last names separately, 
# then greet the user with their full name.

# What is your first name? Bob
# What is your last name? Roberts
# Hello, Bob Roberts!

first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print(f'Hello, {first_name} {last_name}!')

# 3. Write a program named age.py that asks the user to enter their age, 
# then calculates and reports the future age 10, 20, 30, and 40 years from now. 
# Here's the output for someone who is 27 years old.

# How old are you? 27
# You are 27 years old.
# In 10 years, you will be 37 years old.
# In 20 years, you will be 47 years old.
# In 30 years, you will be 57 years old.
# In 40 years, you will be 67 years old.

age = int(input('How old are you? '))
print(f'You are {age} years old.')

count = 10
while count <= 40:
    print(f'In {count} years, you will be {count + age} years old.')
    count += 10


