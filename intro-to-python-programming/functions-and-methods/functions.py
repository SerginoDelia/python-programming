# Functions and Methods
# Blocks of code that run as seperate units

# Calling Functions
# using a function means calling, invoking, executing, or running it 

def hello():
    print('Hello')
    return True

hello() # invoking function; ignore the return value
print(hello()) # using return value in a `print` call 

# the print function returns None 
print(print()) # None

# Functions can also take one or more comma-separated arguments between the parenthesis
# Functions usually use arguments to modify the actions they take 

print('hello', 'goodbye', 'farewell')

# Built-in Functions
# functions that are always available in Python

# float, int 
# str, list, tuple
# set, frozenset
# input, print
# type 
# len 
# min, max 

# min and max fuctions can be used to determine a collection's minimum and maximum value
# the collection must have an ordering that recognizes the < and > operators for comparing any pairs
# of those objects

print(min(-10, 5, 12, 0, -20)) # -20
print(max(-10, 5, 12, 0, -20)) # 12

print(min('over', 'the', 'moon')) # 'moon'
print(max('over', 'the', 'moon')) # 'the'

# min and max can also be used with a single iterable argument, such as list, set, or tuple

my_tuple = ('i', 'tawt', 'i', 'taw', 'a',
            'puddy', 'tat')

print(min(my_tuple))
print(max(my_tuple))

# ord and chr
# given a single character, ord returns an integer that represents the Unicode poin of that character

print(ord('a')) # 97
print(ord('A')) # 65
print(ord('=')) # 61
print(ord('~')) # 126

# chr is the inverse of ord.  It converts an integer to the corresponding Unicode character

print(chr(97))
print(chr(65))
print(chr(61))
print(chr(126))

# Truthy and Falsy 
# these are not the same as True and False, but a little more general

# The Following are falsy:
# False, None 
# all numeric 0 values (integers, floats, complex)
# empty strings: ''
# empty collections: [], (), {}, frozenset(), and range(0)
# custom data types can also be define additional falsy value(s)

# All other values are said to be Truthy

# any and all 
# 2 very useful Built-in functions are the any and all
# they both operate on iterable collections, such as lists, tuples, ranges,
# dictionaries, and sets 

# The any function returns True if any element in a collection is Truthy,
# False if all of the elements are falsy 

# On the other hand all returns True if all of the elements are truthy, False otherwise

collection1 = [False, False, False]
collection2 = (False, True, False)
collection3 = {True, True, True}

print(any(collection1)) # False
print(any(collection2)) # True
print(any(collection3)) # True 
print(any([])) # False

print(all(collection1)) # False 
print(all(collection2)) # False
print(all(collection3)) # True 
print(all([])) # True 

# Notice that any returns False for an empty collection since none of the elements are truthy.
# But all returns true for the same collection since none of the elements are falsy (all the elements are thus truthy)

# Ex: assume you want to determine whether a list of numbers have any even values in it 
# you can use list comprehension to determine which values are even or odd 

numbers = [2, 5, 8, 10, 13]
print([number % 2 == 0 for number in numbers]) # [True False True True False]

# It can be taken further to determine whether any or all of the numbers are even:

numbers = [2, 5, 8, 10, 13]
print(any([number % 2 == 0 for number in numbers])) # True 
print(all([number % 2 == 0 for number in numbers])) # False 

numbers = [5, 13]
print(any([number % 2 == 0 for number in numbers])) # False
print(all([number % 2 == 0 for number in numbers])) # False

numbers = [2, 8, 10]
print(any([number % 2 == 0 for number in numbers])) # True
print(all([number % 2 == 0 for number in numbers])) # True

# The id function
# The id function returns an integer that serves as an object's identity. Every
# object has a unique identity that does not change during the object's lifetime

# In most cases, two instances of an object with the same value will always have 
# two distinct identities. This is not always true, though. For instance, 
# in a process called interning, every unique integer object from -5 through 256 has the same identity.

# Paste this code into the Python REPL
# Don't run it as a program

s = 'Hello, world!'
t = 'Hello, world!'
print(id(s) == id(t))         # False

s = 'supercalifragilisticexpialidocious'
t = 'supercalifragilisticexpialidocious'
print(id(s) == id(t))         # True

x = 5
y = 5
print(id(x) == id(y))         # True

x = 5
y = 6
print(id(x) == id(y))         # False

# Interning yields memory space savings and performance improvements.

# The dir function
# When used without arguments, the dir function returns a list of identifiers 
# in the current local scope.
# When used with an argument, dir() returns a list of the objects attributes
# (typically the objects methods and instance variables)

print(dir())

print(dir(5))

# Many of the names shown by dir begin and end with two underscores. These are names for the 
# so-called `dunder` (double-underscore) or `magic` methods and 'magic variables'

# Helpful hint: Use the sorted function with the ouput of dir:
print(sorted(dir(range(1))))

# Another helpful hint: Use pretty print to print the output in an easier to read format:

from pprint import pp 

names = sorted(dir(range(1)))
pp(names)

# Another Helpful hint: Use comprehension to limit the output to just the names that 
# don't contain __ 

names = sorted(dir(range(1)))
names = [name for name in names if '__' not in name]
print(names)

# The help Function 
# when used without arguments, the help function print some basic help on how to use help
help()

# request help more directly by placing an appropriate identifier between the parenthesis
help(ord)

# Namespaces
# in Pyhton, a namespace is defined as mapping of identifiers to objects.
# namespaces define the scopes in which Python will look for identifiers
# Python first looks for the identiier in the local namespace, that is it looks in the local scope 
# If the identiier is not in the local scope, Python next looks in any enclosing namespace, ie the outer scopes
# (but not including the global scope). Next it searches the global namespace, which is equivalent to 
# the global scope, and finally, the built-in namespace


