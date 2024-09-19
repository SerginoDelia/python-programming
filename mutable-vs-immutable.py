# Immutable Types
# Strings, numbers and booleans are immutable; meaning their value cannot change

# x is purely a label form that memory location
x = 1
# print the address of the memory location
print(id(x))

# when x is updated Python will allocated new memory at another location
# because we don't have a reference to the original memory, at some point
# python garbage collector will remove this memory
x = x + 1
print(id(x))


# Mutable Type

x = [1, 2, 3]
print(id(x))

# add a new number to x
x.append(4)
# the address will not change, changes are applied at the same memory location
print(id(x))
