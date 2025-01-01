# Arguments and Parameters

print('hello')
print('hi')
print('how do you do')
print('Quite all right')

def say(text):
    print(text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

# Arguments let you pass data from outside the function's scope into the function so
# it can access that data.  Arguments are not needed when the fuction doesn't need access
# tp outside data 

# The names between parenthesis in the function definition are called parameters, think of 
# parameters as placeholders for potential arguments, while arguments are the values assigned
# to those placeholders

# Function names and parametersare both considered variables in Python, parameters are local variables
# parameters cannot be referenced outside the function body

def add(left, right):
    sum = left + right 
    return sum 

sum = add(3, 6)

# in the above code, left and right are parameters, however they are local variables that 
# contains the argument values passed to add

# functions gives us the ability to make changes in one location, suppose we wanted to 
# add a ==> to the beginning of every line that say outputs, all we have to do is change one
# line of code -- we con't have to chage the function invocations:

def say(text):
    print('==> ' + text)

say('hello')
say('hi')
say('how are you')
say("I'm fine")

# Return Values 
# functions can perform an operation and return a result to the caller for later use 
# that can be done with a return statement 
# All Python function calls evaluate to a value, by default the value is None;
# this is the implicit return value of most Python functions 
# use return to return a specific value outside the function

def add(a, b):
    return a + b 

add(2, 3) # returns 5

# When Python encounters a return statement, it evaluate the expression, terminates the function 
# then returns the expression's value 

two_and_three = add(2, 3)
print(two_and_three)

# Functions that always return a Boolean value, i.e. True or False are called predicates
# predicate example:

def is_digit(char):
    if char >= '0' and char <= '9':
        return True 

    return False

# Default Parameters
# functions can be invoked without some of its arguments, by providing default values 
# for the function's parameters 

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy
say() # hello!

# default parameters can be provided for all of the function's parameters, but once one
# default parameter is provide all parameters after must have default values

# def say(msg1, msg2, msg3='dummy message', msg4):
#     pass

# SyntaxError: non-default argument follows default argument

# you cant accept the default value for a parameter and provide an explicit value for the 
# subsequent parameter 

def say(msg1, msg2, msg3='dummy message',
                    msg4='omitted message'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)

say('a', 'b', 'c', 'd')
say('a', 'b', 'c')
say('a', 'b')
# say('a', 'b', , 'd')
# a
# b 
# d # oops - expecting 'dummy message'
# omitted message # oops - expected 'd'

# Functions vs Methods
# Thus far, all function calls have used the function_name(obj, ...) syntax.

# Method invocation occur when you prepend an object followed by a period to a function invocation
# e.g. 'xyzzy'.upper(), such function invocation are called method calls 
# methods provides the same benefits as functions, however methods work with specific object
# all methods are functions but not vice versa 
# Every method belongs to a class and requires an object of that class to call it 

my_str = 'abc-123-def'
print(my_str.upper())

# Writting custom methods requires classes, which is how custom data types are created in Python 
# Some function invocations look like method invocation 

import math

print(math.sqrt(5))

# Since math references an object, math.sqrt() must be a method call, it is not.
# math is technically a reference to a module object, it is not being used to perform
# operations on that object, the sole purpose of the math object is to tell Python where 
# to look for those functions 

# Mutating the Caller 
# sometimes a method mutates the object used to invoke the method: it mutates the caller.

odd_numbers = [1, 3, 5, 7, 9]
odd_numbers.pop()
print(odd_numbers)

# We can also talk about whether functions mutate their arguments:

def add_new_number(my_list):
    my_list.append(9)

numbers = [1, 2, 3, 4, 5]
add_new_number(number)
print(numbers) # [1, 2, 3, 4, 5, 9]

# The code above uses the list.append method to add a new member to the list my_list, thus 
# list.append mutates the caller 

# mutating the caller is acceptable practice; many built-in functions and methods do just that.
# However, avoid mutating arguments since such functions can be tough to debug and is considered bad practice

# Returning a new object
def add_new_number(my_list):
    return my_list + [9]

numbers = [1, 2, 3, 4, 5]
new_numbers = add_new_number(numbers)
print(new_numbers)
print(numbers)
