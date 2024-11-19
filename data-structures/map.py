# Map - applies a function to all items in an input_list

# Syntax
# map(function_to_apply, list_of_inputs)

# Ex - most of the time we want to pass all the list elements to
# a function one-by-one and then collect the output

items = [1, 2, 3, 4]
squared = []
for i in items:
  squared.append(i ** 2)

# Map allows a much simpler implementation

items = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, items))

# We can even have a list of functions

def multiply(x):
  return (x*x)

def add(x):
  return (x+x)

funcs = [multiply, add]

for i in range(5):
  value = list(map(lambda x: x(i), funcs))
  print(value)
