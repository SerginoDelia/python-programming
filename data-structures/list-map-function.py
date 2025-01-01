# Map function

items = [
  ("product1", 10),
  ("Product2", 9),
  ("Product3", 12)
]

# Transform the list of Tuples into a list of numbers

prices = []

for item in items:
  prices.append(item[1])

print(prices)

# using the map function:
# the map function will iterate over the iterable(items) and call the lambda function 
# on each item of this iterable

x = map(lambda item: item[1], items)

for item in x:
  print(item)

# we can convert the map object into a list object
# we can pass the list function to any iterable to create a new list

x = list(map(lambda item: item[1], items))
  print(x)
