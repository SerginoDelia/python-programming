# Tuples
# A Tuple is basicly a read-only list, we cannot modify an existing object
point = (1, 2)

# We can also exclude the parenthesis
point = 1, 2
print(type(point))

# If you have 1 item, you shoud add a trailing comma point = 1,
# otherwise Python will think you're defining an integer

point2 = 1,
print(type(point2))

# To define an empty Tuple, you should use an empty parenthesis
# Tuples are immutable
point3 = ()
print(type(point3))

# Similar to lists, we can concatenate 2 tuples
point = (1, 2) + (3, 4)
print(point)

# We can use the multiplication operator to repeat a tuple
point = (1, 2) * 3
print(point)

# We can convert a list to a Tuple by calling the Tuple function
# The tuple function takes an iterable, we can pass any iterable
point = tuple([1, 2])
print(point)


# We can access individual items using an index, similar to lists
point = (1, 2, 3)
print(point[0])

# Or a range of items, returns a tuple
print(point[0:2]) 

# We can unpack tuples
x, y, z = point

# We can use the in operator
if 10 in point:
  print("Exists")
