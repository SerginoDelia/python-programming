# Unpacking Operator, similar to spread operator in JS

numbers = [1, 2, 3]
print(*numbers)

# same as above using the unpacking operator
values = [*range(5)]
print(values)

# We can unpack a string
string = [*"Hello"]

values = list(range(5))
print(values)

# Combining multiple lists
first = [1, 2]
second = [3]
values = [*first, *second]
print(values)

# Unpacking Dictionaries, use **. If there are multiple values with the same
# key the last value will be used
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second}
print(combined)
