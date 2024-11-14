# Filter function

items = [
  ("Product1", 10),
  ("Product2", 9),
  ("Product3", 12),
]

# Filter the list and only get items with price greather than or equal to 10
x = filter(lambda item: item[1] >= 10, items)
print(x)

# Filter returns a filter object, list will convert it to a list
filtered = list(filter(lambda item: item[1] >= 10, items]))
