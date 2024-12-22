# for loops
# 3 iterate over any object that is iterable

for x in "Pyhton":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

# print 0 through 4
for x in range(5):
    print(x)
# we can also use step (start, end, step)
# the range function does not return a list
for x in range(0, 10, 2):
    print(x)
# range is an object, range object takes a small amount of memory
print(type(range(5)))  # <class 'range'>

# for loop with conditionals
names = ["John", "Mary"]

for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")

# For Loops
# for placeholder in iterable:

msg = "Python Programming"
print(msg[0:5])

# Recursion - a function that calls itself

# PEDAC - Problem, Example, Data, Algoritym, Code
# Problem: Create our own loop that can loop through an iterable
# Example: [1, 2, 3]
# 1
# 2
# 3
# Data: iterable, can be a list, string, tuple (1, 2, 3), slice method
# Algorithm:
#     iterate over the iterable
#     get one item at a time [0:1] --> Python = ython = thon = hon = on = n
#     [1, 2, 3] = [2, 3] = [3] = []
#     if the iterable is empty return (stop the loop)
#     if the iterable is not empty print the first item, take it out and call the function again
# Code:
def my_for(iterable):
    # base
    if len(iterable) == 0:
        return iterable
    print(iterable[0])
    my_for(iterable[1:])

def factorial(n):
    # base case
    if n == 1:
        return 1
    return n * factorial(n - 1)
    # return 4 * factorial(4 - 1 = 3)
    # return 3 * factorial(3 - 1 = 2)
    # return 2 * factorial(2 - 1 = 1)
    # return 1

# 4 * 3 * 2 * 1 = 24
