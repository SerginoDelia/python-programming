# Sorting Lists
# sort() method, sorts the list
numbers = [3, 51, 2, 8, 6]

numbers.sort()
print(numbers)

# sort in descending order
numbers.sort(reverse=True)

# sorted() returns a new list sorted, it will not mutate the original list
sorted(numbers)

# sorted() in descending order
sorted(numbers, reverse=True)

# List of tuples

items = [
  ("Product1", 10),
  ("Product2", 9),
  ("Product3", 12)
]

# Sort items based on their price, use a helper function that returns the price

def sort_item(item):
  return item[1]

# pass a reference to the function, but not calling the function, when Python call the sort
# function, it will pass each item to the helper function
items.sort(key=sort_item)

# Lambdas (anonymous function)
# Lambdas syntax: items.sort(key=lambda parameters:expression)

items.sort(key=lambda item:item[1])
print(items)







