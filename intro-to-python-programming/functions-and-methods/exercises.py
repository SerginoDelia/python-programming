# Exercises
# 1. What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()
# print(foo) returns an error because foo is not declare in the global scope
# foo is available in the function scope 
# NameError: name 'foo' is not defined

# 2. Take a look at this code snippet:

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)

# What does this program print? Why?
# print(foo) prints 'bar' because foo is in the global scope 

# Write a program that uses a multiply function to multiply two numbers 
# and returns the result. Ask the user to enter the two numbers, 
# then output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

def multiply(left, right):
    return left * right 

def get_number():
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# 4. Consider this code:
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

# Identify the following items in that code:

# Item
# function name - multiply_numbers
# function arguments - 2, 3, 4
# function definition - from def - return result 
# function body - result = num1 * num2 * num3, return result 
# function parameters - num1, num2, num3 
# function invocation - multiply_numbers(2, 3, 4)
# function return value - 24
# all identifiers - multiply_numbers, num1, num2, num3, result, product 

# 5. What does the following code print?

def scream(words):
    return words + '!!!!'

scream('Yipeee') # Yipeee!!!! 

# 6. What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')
# return terminates the function before the print function 

# 7. Without running the following code, what do you think it will do?

# def foo(bar, qux):
#     print(bar)
#     print(qux)
#
# foo('Hello') # error because there's no argument for qux 
# Error: foo() missing 1 required positional argument: 'qux'

# 8. Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

#foo(42, 3.141592, 2.718) # Error the function take 2 arguments, but 3 aruments are provided
# TypeError: foo() takes 2 positional arguments, but 3 were given

# 9. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718) # it will print the arguments one per line 
# 42
# 3.141592
# 2.718

# 10. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592) # it will print the arguments one per line, and the default argument
# 42
# 3.141592
# 2 

# 11. Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)
# 42
# 3 
# 2 

# 12. Without running the following code, what do you think it will do?

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

# foo()
# TypeError: foo() missing 1 required positional argument: 'first'

# 13. Without running the following code, what do you think it will do?

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

# foo(42)
# TypeError mising require positional argument: 'third'

# 14. Identify all of the identifiers on each line of the following code.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# multiply, left, right, get_num, prompt, float, input, first_number, second_number,
# product, print

# 15. Using the code below, classify the identifiers as global, local, or built-in. For our purposes, you may assume this code is the entire program.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# global: multiply, get_num, first_number, second_number, product
# local: left, right, prompt 
# built-in: float, input, print 

# 16. In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# function names: multiply, get_num, float, input, print 
# parameters: left, right, prompt 

# 17. Which of the identifiers in the following program are function names? Which are method names? 
# Which are built-in functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# function names: say
# method names: upper, lower 
# built-in functions: print, input, max 

# 18. The following function returns a list of the remainders of dividing the numbers in numbers by 3:

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6] 
numbers_4 = []

# 19. Not that when working with integers, a value of 0 is 'falsy'; all other integers are 'truthy'

print(any(remainders_3(numbers_1))) # True 
print(any(remainders_3(numbers_2))) # True 
print(any(remainders_3(numbers_3))) # False 
print(any(remainders_3(numbers_4))) # False 

# The following function returns a list of the remainders of dividing the numbers in numbers by 5:

def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(remainders_5(all(numbers_1))) # False 
print(remainders_5(all(numbers_2))) # True - none of the values are divisible by 5 with 0 remainder
print(remainders_5(all(numbers_3))) # False 
print(remainders_5(all(numbers_4))) # True 
