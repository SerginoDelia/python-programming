# List literals use square brackets [] surrounding a comma-delimited list of values,
# while tuples use parentheses ()

my_list = [1, 'xyz', True, [2, 3, 4]]
print(my_list)

tup = ('xyz', [2, 3, 4], 1, True)
print(tup)

# List and tuple literals may also use a multi-line format, which is useful for nested collections
# Items in the list can be accessed using bracker notation
# The values between the brackets must be an integer between 0 and the length -1
# Lists are mutable and tuples are immutable (read-only)

my_tuple = (1)
print(type(my_tuple)) # <class 'int'>
# in the case above the parentheses cause Python to treat the expression as a parenthesized 
# expression, not as a tuple
my_tuple = (1,)
print(type(my_tuple)) # <class 'tuple'>

# Ranges 
#a sequence of integers between 2 endpoints
# most commnly used to iterate over an increasing or decreasing range of integers
# Python optimizes ranges to save memory

# with one argument the range start at 0 
my_tuple = tuple(range(5)) 
print(my_tuple) # (1, 2, 3, 4)

# with 2 arguments, the first argument is the starting poing, second argument is one
# past the last number
my_tuple = tuple(range(5,10))
print(my_tuple) # (5, 6, 7, 8, 9)

# With 3 arguments the 3rd argument is the step value 
my_list = list(range(0, -5, -1))
print(my_list) # [0, -1, -2, -3, -4]

# Like strings, lists, and tuples, indexing can be used to access specific numbers in the range object
my_range = range(5, 10)
print(my_range[3]) # 8
