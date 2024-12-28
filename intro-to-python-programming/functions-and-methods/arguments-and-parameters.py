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
#

