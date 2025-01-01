# List Zip function

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Combine the 2 list into a tuple
# [(1, 10), (2, 20), (3, 30)]

# zip function takes multiple iterables and combine them and return a list object
print(list(zip(list1, list2)))

# We can also pass a string
print(list(zip("abc", list1, list2)))

