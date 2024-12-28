# Terminal Input
# We can ask the inser to provide input for our program
# Python has a built-in function called input() that lets Python programs read
# input from the terminal 

# Greet user by name 
print("What's your name?")
name = input()

print(f'Good morning, {name}!')

# The input function can also be used to display the prompt the user sees
name = input("What's your name? ") # Note the space after the ?
print(f'Good morning, {name}!')

# We can have input() output a new line instead of a space
name = input("What's your name?\n")
print(f'Good morning, {name}!')

# Adding Two Numbers

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = number1 + number2

print(f'The numbers {number1} and {number2} ' f'add to {sum}')
# The numbers 2 and 5 add to 23

# input() returns strings, so + performs concatenation
# We can convert (coerce) strings to numbers with the int() or float() function 
# updated code

number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
sum = float(number1) + float(number2)
print(f'The numbers {number1} and {number2} ' f'add to {sum}')

# input() still returns a string, but it is coerced to a float
