# Variables and Variale Names
# A Variable is a label attached to a specific value stored in memory

answer = 41
print(answer)

answer = 42 # reassign the value 42 to the answer variable 
print(answer)

# Naming Convention
# names that follow these conventions are idiomatic, and those that do not are non-idiomatic 
# Use snake_case formating the names
# names may contain lowercase letters (a-z), digits (0-9), and underscores (_)
# names should begin with a letter 
# if the name have multiple words, seperate the words with a single underscore
# Names that begin or end with one or 2 underscore have special meaning under the naming conventions,
# dont use them until they are understood how they are used
# Names may only use letters and digits from the standard ASCII character set 

# Idiomatic Names
# foo
# answer_the_ultimate_question
# eighty_seven
# index_2
# index2 

# Constants names (unchanging named values)

# Use SCREAMING_SNAKE_CASE formatting for these names
# Names may contain uppercase letters (A-Z), digits (0-9), and underscores (_)
# If the name has multiple words, seperate the words with a single underscore (_)
# Names that begin or end with one or 2 underscore have special meaning under the naming conventions,
# dont use them until they are understood how they are used
# Names may only use letters and digits from the standard ASCII character set 

# Idiomatic Names
# FOO 
# ANSWER_THE_ULTIMATE_QUESTION 
# EIGHTY_SEVEN 
# INDEX_2 
# INDEX2 

# The constant naming convention is advisory only. Python has no way to ensure that contants are never changed

# Class Names
# Use PascalCase formattingfor these names. Sometimes called CamelCase
# Names may contain uppercase and lowercase letters (A-Z, a-z) and digits (0-9)
# Names should begin with an uppercases letter 
# If the names has multiple words, capitalize each word 

# Idiomatic Names
# Foo 
# UltimateQuestion 
# FourLeggedPets
# PythonVersion2Rules

# Most illegal names will raise an error, but if the illegal name looks like Python, you won't get an error
first,last = ['Mary', 'Wonder']

# Creating and Reassigning Variables
# We create (initialize) most variables by simply giving them a value 
foremane = 'Clare' # initialization (also called assignment)

foremane = 'Victor' # reassignment 

# an asignment like foo = bar can be described in 2 ways 
# 1. The variable foo is assigned the value of bar 
# 2. the value bar is assigned to the variable foo
# both phrase mean the same thing, but phrase one is prepared

foo = 'abcdefghi'


# When Python encounters this code, it will create the string 'abcdefghi' somewhere in memory
# let's assume the address is 73420, Next it creates a variable somewhere else in memory, let's suppose
# the variable is at address 10230.  It then associates address 10230 with the name foo 
# Python stores the address of the string (72420) at address 10230

foo = 'Hello'

# Python creates the new string 'Hello' somewhere in memory. We assume 'Hello' is stored at memory address
# 87160, since we already have a foo variable, Python simply replaces the value at address 10230 with 87160

# Creating Constants
PINNING_FOR = 'fjords' # initialization

# No keywords are required to create constants, but use SCREAMING_SNAKE_CASE

# Expressions and Assignment 
# Assingment and reassignmen often use expressions on the right side of the = to determine the desired value

left_side = 5
right_side = 32
total = left_side + right_side
print(total)

# A fuinction call to compute the resulting value for the assignement:

def square(number):
    return number * number 

forty_two_squared = square(42)
print(forty_two_squared)

# the expression on the right side of the = operator can be any valid expression.
# It can also be as somple or complex as needed, strive for more readable and easy to understand 
# The variable on the left side of the = operator is always the target variable for the resulting value

foo = 42 # foo is 42
foo = foo - 2 # foo is now 40
foo = foo * 3 # foo is now 120 
foo = foo + 5 # foo is now 125 
foo = foo // 25 # foo is now 5 
foo = foo / 2 # foo is now 2.5
foo = foo**3 # foo is now 15.625
print(foo)

# Augmented Assingment 
# Shorthand notation

foo = 42
foo -= 2 
foo *= 3
foo += 5
foo //= 25
foo /= 2
foo **= 3
print(foo)

# Augmented assimenet also works with string concatenation and repetition
bar = 'xyz'
bar += 'abc' # bar is now 'xyzabc'
bar *= 2 # bar is now 'xyzabcxyzabc'
print(bar)

bar = [1, 2, 3]
bar += [4, 5] # + with lists appends.  bar is now [1, 2, 3, 4, 5]
print(bar)

bar = {1, 2, 3} 
bar |= {2, 3, 4, 5} # | performs a set union, bar is now {1, 2, 3, 4, 5}
bar -= {2, 4} # - performs set difference, bar is now {1, 3, 5}
print(bar)

# Note that augmented assigment is a statement, not expression, can't be used as a 
# function argument or return value 

def foo(bar):
    print(bar)

a = 3
# foo(a *= 2) # SyntaxError: invalid syntax 

def foo():
    a = 3
    # return a *= 2 
# SyntaxError: invalid syntax

# Reassignment vs. Mutation 
# there are 2 ways to change things in Python and most other programming languages
# Change the binding of the variable by making it reference a new object know as reassignment, or change the value
# of the object assigned (bound) to the variable known as mutation 

# A variable name referes to a specific object at a place in memory. Reassignment makes that name
# refer to a different object somewhere else in memory
# Mutation on the other hand does not change which object the variable refers to instead it changes the
# object itself.  After mutating an object assigned to a specific variable, the variable continues to 
# refer to the same object 

# One subtle but important distinction is the difference between reassigning a variable and reassigning
# an element in a list, dict, or other mutable collection.  Reassigning an element of a mutable collection
# doesn't reassign the variable; it mutates the collection

num = 3 # assingment (initialization)
my_list = [1, 2, 3] # assingment (initialization)
my_dict = { # assingment (initialization)
    'a': 1,
    'b': 2,
}

num = 42 # reassignment
my_list[1] = 42 # reassignment of element, my_list is mutated 
my_dict['b'] = 3 # reassignment of dict pair, my_dict is mutated 

# The variables can still be reassigned 
my_list = [2, 3, 4] # reassignment
my_dict = { 'x': 0 } # reassignment

# Exercises
# 1. Classify the following potential non-constant variable names as idiomatic, 
# non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
# Name
# index - idiomatic
# CatName - non-idiomatic
# lazy_dog - idiomatic
# quick_Fox - non-idiomatic
# 1stCharacter - illegal
# operand2 - idiomatic
# BIG_NUMBER - non-idiomatic
# π - non-idiomatic

# 2. Classify the following potential function names as idiomatic, 
# non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
# Name
# index - idiomatic
# CatName - non-idiomatic
# lazy_dog - idiomatic
# quick_Fox - non-idiomatic
# 1stCharacter - illegal
# operand2 - idiomatic
# BIG_NUMBER - non-idiomatic
# π - non-idiomatic

# 3. Classify the following potential constant names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.
# Name
# index - non-idiomatic
# CatName - non-idiomatic
# snake_case - non-idiomatic
# LAZY_DOG3 - idiomatic
# 1ST - illegal
# operand2 - non-idiomatic
# BIG_NUMBER - idiomatic
# Π - non-idiomatic

# 4. Classify the following potential class names as idiomatic, non-idiomatic, or illegal. 
# For the non-idiomatic and illegal names, explain your choice.
# Name
# index - non-idiomatic
# CatName - idiomatic
# Lazy_Dog - non-idiomatic
# 1ST - illegal
# operand2 - non-idiomatic
# BigNumber3 - idiomatic
# Πi - non-idiomatic

# 5. Write a program named greeter.py that greets 'Victor' three times. 
# Your program should use a variable and not hard code the string value 'Victor' in each greeting. 
# Here's an example run of the program:
#$ python greeter.py
# Good Morning, Victor.
# Good Afternoon, Victor.
# Good Evening, Victor.

name = 'Victor'

print(f'Good Morning, {name}')
print(f'Goog Afternoon {name}')
print(f'Good Evening, {name}')

count = 0
time_of_day = ['Morning', 'Afternoon', 'Evening']
while count < 3:
    print(f'Good {time_of_day[count]}, {name}')
    count += 1

# 6. Write a program named age.py that includes someone's age and then calculates 
# and reports the future age 10, 20, 30, and 40 years from now. Here's the output 
# for someone who is 22 years old.

age = 22 
print(f'You are {age} old')
print(f'In 10 years, you will be {age + 10} years old')
print(f'In 20 years, you will be {age + 20} years old')
print(f'In 30 years, you will be {age + 30} years old')
print(f'In 40 years, you will be {age + 40} years old')

count = 10

while count <= 40:
    print(f'In {count} years, you will be {age + count} years old')
    count += 10

# 7. What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# the value of the constant NAME will change (reassignment), because it's a Python convention,
# Python has no way to prevent constants, because Python doesn't have real constants 
# the program will greet Victor 3 times and greet Nina 3 times

# 8. Challenge: This program uses a bit of math. Don't let that scare you away -- try it anyway.

# Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% 
# (this is a wish-fulfillment fantasy) compounded interest every year. After one year, you will have 
# $1,050 ($1,000 times 1.05). After two years, you will have $1,050 times 1.05, or $1102.50. 
# Create a variable named balance that contains the amount of money you will have after 5 years, 
# then print the result. Use a single expression if you can to set balance to the correct value.

balance = (1000.0 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(balance)

# 9. Repeat the previous question but, this time, use augmented assignment to compute the final result, 
# one year at a time.

balance = 1000.0
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)

# 10. Assume that obj already has a value of 42 when the code below starts running. 
# Which of the subsequent statements reassign the variable? Which statements mutate 
# the value of the object that obj references? Which statements do neither? If necessary, 
# you can read the documentation.

obj = 'ABcd' # Reassingment
obj.upper() # neither 
print(obj)
obj = obj.lower() # reassignment
print(obj)
print(len(obj)) # neither
obj = list(obj) # reassignment
obj.pop() # mutation
obj[2] = 'X' # mutation 
obj.sort() # mutation 
set(obj) # neither
obj = tuple(obj) # reassignment
