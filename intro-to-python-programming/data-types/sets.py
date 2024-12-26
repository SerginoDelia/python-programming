# Sets - represents an unordered collection of unique objects
# the objects are sometimes called the members of the set 

d1 = {} # empty dict
print(type(d1)) 

s1 = set()
print(s1)

# Createa a set from a literal
# s2 = {2, 3, 5, 7, 11, 13}
# print(s2)
#
# # Create a set from a string 
s3 = set("hello there")
print(s3)

# set literals may also use multi-line format
monty_python_cast = {
    'Eric Idle',
    'John Cleese',
    'Terry Gillian',
    'Graham Chapman',
    'Micheal Palin',
    'Terry Johns',
}

# There are 2 main types of sets: ordinary sets (calss set)
# and frozen sets (class frozenset). frozensets are immutable sets 
# They lack literal syntax, use the `frozenset` function to create one

s5 = frozenset([1, 2, 3])
print(s5)

s6 = frozenset((1, 2, 3))
print(s6)

s7 = frozenset({1, 2, 3})
print(s7)

s8 = frozenset(range(1, 4))
print(s8)

s9 = frozenset([3, 4, 5])
print(s9)

s10 = frozenset({4, 5, 6})
print(s10)

