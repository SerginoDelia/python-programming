# Sets a collection with no duplicates, an unordered collection of items
# The items inthe list are not in sequence (ordered like lists)
numbers = [1, 1, 2, 3, 4]

# convert list to set to remove duplicates
first = set(numbers)
print(first) # {1, 2, 3, 4}

# Sets are defined using curly braces
second = {1, 5}

# add and remove items from the list
second.add(6)
second.remove(6)

# len function to get the number of items from the Set
len(second)

# union of 2 sets using the |, returns all the items that are either in the 
# first or second set
print(first | second)

# Get the intersection of 2 sets
print(first & second) # print the number that exist in both sets

# Get the difference between the 2 sets
print(first - second)

# Symmetic Difference - Returns items that are either in the first or second set, but not both
print(first ^ second)

if 1 in first:
  print("yes")
