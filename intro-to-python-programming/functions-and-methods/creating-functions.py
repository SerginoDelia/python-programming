# Creating Functions
# Unless a function is built-in or provided by an imported module, it must be created 

# def func_name():
#     func_body

# A function named say that prints Hi!

def say():
    print('Hi!')


print('First')
say() # function call to the say function 
print('Last')

# Python programmers often add triple-quoted strings at the beginning of a function's block
# this string is a documentation comment - a `docstring` -- that Python can access with its help()
# function and the __doc__ property.  It has no effect on the code, unless your program is interested
# in the comments (which can happen)

def say():
    """
    The say function prints "Hi!"
    """
    print('Hi!')

print('-' * 60)
print(say.__doc__)
print('-' * 60)
help(say)

# Scope
# the scope of an identifier determines where you can use it.  Python determines the scope by looking
# at where you initialize the identifier 
# In Python identifiers have function scope.  That means anything initialized inside a fuction
# is only available within the body of that fucntion and any nested function. No code outside of the 
# fuction can access that identifier 

# Consider this code:

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
# print(greeting) NameError: name is not defined
# The error occurs since the greetin variable is only available inside the 
# well_howdy function

# What happens if greeting variable is defined in the outer scope

greeting = 'Salutations'

def well_howdy(who):
    greeting = 'Howdy'
    print(f'{greeting}, {who}')

well_howdy('Angie')
print(greeting)

# This time the code will print Salutations - the outer greeting variable plays no part in the 
# in the functions body this is called 'variable shadowing'

# Let's remove greeting from the function body

greeting = 'Salutations'

def well_howdy(who):
    print(f'{greeting}, {who}')

well_howdy('Angie') # Salutations, Angie
print(greeting) # Salutations

# we're accessing the greeting variable in the outer scope 
# Without any assignment in the function body, Python looks for greeting in the 'lexical scope'
# Which means it searches the outer scope for the nearest definition of greeting.
# In this example the outer scope is the top most scope (global scope)

def scope_test():
    if True:
        foo = 'Hello'
    else:
        bar = 'Goodbye'
    print(foo)
    print(bar)

# scope_test()
# Hello
# UnboundLocalError: cannot access local variable 'bar' where it is not associated with a value 
# both names are technicalluy in scope, but since the else block never runs, bar is left unassigned
# Constants have the same scoping as variables 


