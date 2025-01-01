# Equality Comparison
# dtermine whether 2 values are identical or different
print(42 == 42) # True 
print(42 == 43) # False 
print('foo' == 'foo') # True
print('FOO' == 'foo') # False

# inequality 
print(42 != 42) # False
print(42 != 43) # True 

# Comparison Operators
print(42 < 41)
print(42 <= 42)
print('abcdf' < 'abcef') # strings are compared lexicographically
print(42 > 42)
print(42 >= 42)

# Like string Comparisons, list and tuple comparison goes element by element
# Sets
print({3, 2, 1} < {2, 4, 3, 1}) # True 

# Tuples 
print([1, 2, 3] < [1, 2, 3, 4]) # True 

# String Concatenation
# It uses `+` and `*` operators to join strings 
print('foo' + 'bar')
print('1' + '2')
print('abc' * 3) # 'abcabcabc'
print(3 * 'abc') # 'abcabcbac'

# Coercion
# change from one type to another

# String to Numbers
print(int('5'))
print(float('3.141592'))

# Numbers to Strings 
# numbers can be coerced to strings using `str` function
print(str(5))
print(str(3.141592))

# Implicit Coercion
# only occurs when mixing numbers with different types in expressions
# int and float = float
# int and Decimal = Decimal
# int and Fraction = Fraction
# float and Decimal = --error--
# float and Fraction = float
# Decimal and Fraction = --error--

print(True + True + True) # 3
print(True + 1 + 1.0) # 3.0
print(False * 5000) # 0

# Determining types
# the type function can be called on any object
print(type(1))
print(type(3.14))
print(type(True))
print(type([1, 2, 3]))
print(type(None)) # <class 'NoneType'>

# The return value of the type function include more information than what's needed.
# access the class name __name__ property from the result
print(type('abc').__name__) # str 
print(type(False).__name__) # bool

# type with the `is` operator
print(type('abc') is str) # True
print(type(False) is bool) # True
print(type([]) is set) # False

# The `isinstance` function determines whether an object is an instance of a particular type 
print(isinstance('abc', str)) # True
print(isinstance([], set)) # False 

class A:
    pass 

class B(A):
    pass

b = B()

print(type(b).__name__) # B 
print(type(b) is B) # True
print(type(b) is A) # False
print(isinstance(b, B)) # True 
print(isinstance(b, A)) # True (b is instance of A and B)

# String Representations
# the `repr` function is a bit lower-level than the str function, it returns a string
# that can in theory , use to create a new insance of the object
my_str = 'abc'
print(my_str) # abc
print(str(my_str)) # abc
print(repr(my_str)) # 'abc'

# Collection and String Lengths
# all built-in collection types (strings, sequences, mappings and sets) have length Lengths
print(len('Launch School'))
print(len(range(5, 15)))
print(len({'foo': 42, 'bar': 7})) # 2

# Indexing and Key Access 
# Strings, lists, and tuples all support indexed access to individual elements in the collection
my_str = "abc"
print(my_str[0])
print(my_str[1])

my_range = range(5, 8)
print(my_range[0])
print(mu_range[2])

my_list = [4, 5, 6]
print(my_list[0])
print(my_lsit[1])
print(my_list[2])

tup = (8, 9, 10)
print(tup[0])
print(tup[1])
print(tup[2])


# Dictionaries use keys that are similar to indexes 
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])
print(my_dict['b'])
print(my_dict['c'])

# Using [] to Update Elements 
# Since the are mutable lists and dictionaries let you use [] operator to replace collection elements
# Note: Strings, frozensets, ranges, tuples are immutable they do not support [] for updates

my_list = [1, 2, 3, 4]
my_list[2] = 6
print(my_list)
my_list[4] = 10

my_dict = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks'
}

my_dict['pig'] = 'snorts'
print(my_dict)

my_dict['fish'] = 'glub glub'

# Expression and Statements
# Expression - combines values, variables, operators, and calls to functions to produce a new object
# Expressions must be evaluated to determine the expression's value 
# Examples:
# Literals: 5, 'Karl', 3.14, True, None 
# variable References: foo or name
# math operations: x + y or a * b - 5
# Comparison operations: 'x' == 'x' or 'x' < 'y'
# String oprations: print('Hello') or len('Python')

# Think of expressions as something that produces a value that can be assigned to a variable
# passed to a function or method, or returned by a function or a method 

# Statement - is an instruction that tells Python to perform an action of some kind 
# unlike expressions statements don't return values 
# Examples:
# Assignment: x = 5
# Control Flow: if, else, while, for and so on 
# function and class definitions: def or class 
# Return statements: like return x, which tells a function to return a value
# return itself doesnt return a value; it informs the function what value it should return
# Import statements: such as import math

# Expressions return a value, statements do not 
# some stand-alone expressions
3 + 4 # simple expression
print('Hello') # function call; returns None 
my_list.sort() # method call; returns None 

# Expression Evaluation 
# by default python evaluates most expressions from left to right
# This is fime if all the oprators are the same operator 
1 + 2 + 3 + 4 + 5

# don't rely on -precedence rules, use parentheses to tell Python explicitly how you
# want to evalue the expression
print(((4 * 5) -1) + (2 * 3))

# Output and return values 
# When we invoke the print function, we're telling Python to write some output to the display
print('abc') # simply print the string 'abc' it doesn't return a useful value, only purpose is to print something

# In mamy cases, a function or expression doen't print anything, but simply returns a value
# that gets assigned to a variable, evalueate as a condition, or passed to another function
list(range(3))
