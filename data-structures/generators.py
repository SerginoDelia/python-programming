# Generators, generator objects are iterable and at each iteration in spit out a new value
# unlike lists it doesn't store all the values in memory, it generate a new value
# at each iteration, use generators when dealing with a laerget list

# get the size of an object
from sys import getsizeof

# comprehension over a tuple returns a generator object
values = (x * 2 for x in range(1000))
print("gen: ", getsizeof(values)) # the size of the generator object remains consistent

# values is a generator object
print(values)
for x in values:
  print(x)
