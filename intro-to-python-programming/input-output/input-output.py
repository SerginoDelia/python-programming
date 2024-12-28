# Input/Output
# Terminal Output

name = 'Jane'
print(f'Good morning, {name}!')

# In the example above, we initialize a name variable with the string 'Jane',
# then use an f-string interpolation to build and sisplay a greeting message

# print() function works with all data types, often -- but not always -- formatting the 
# output in some manner that makes it somewhat underrtandable to humans

# Multiple objects can be printed just by listing them one after the other as arguments to print

print(1, 2, 3, 'a', 'b')

print([1, 2, 3], 4, False, {5, 6, 7, 8})

# By default, multiple items are seperated by spaces, a different seperator can be used
# with the `sep` keyword argument 

print(1, 2, 3, 'a', 'b', sep=',') # 1,2,3,a,b
print('a', 'b', 'c', 'd', 'e', sep='') # abcde

# Note using empty string as the sep value causes all the values to be printed without sepration

# The end argument defines what print() prints after it prints the last argument
# By default it prints a newline ( \n ). The most common reason for using end is compatibility
# with Windows.  and for not supressing newline altogether.  Examples:

print(1, 2, 3, 'a', 'b', sep=',', end=' <-\n') # 1,2,3a,b <- 
print('a', 'b', end='', sep=','); print('c', 'd', sep=',') # a,b,c,d

# The semicolon ( ; ) an easy way to enter multiple statements on a single line, should be used 
# mostly on the REPL


# Terminal Output
#
