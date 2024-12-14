# Dictionary Comprehensions

# Set comprehension
values = {x * 2 for x in range(5)}
{1, 2, 3, 4} # Set
{1: "a", 2: "b"} # Dictionary
print(values)

# Dictionary
values = {}
for x in range(5):
  values[x] = x * 2

# shorthand version of the code above
values2 = { x: x * 2 for x in range(5)}
print(values2)

values3 = {}X: x * 3 for x in range(5)}
print(values3)
