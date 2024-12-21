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

# Loop over dictionairies

for key in point:
  print(key, point[key])

for key, value in point.items():
  print(key, value)

# Loop over the items and returns a tuple for each key, value pair
for x in point.items():
  print(x)

a_dic = {'lions':5, 'tigers':10, 'bears':15}

for (k,v) in a_dict.items():
  a_dict[k] = v * 5 # transforms each value


# Dictionary comprehension
a_dict = {k:v*5 for (k,v) in a_dict.items()}
