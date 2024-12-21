# Comprehension
# Syntax: [expression for item in items]

a_list = [1, 2, 3, 4, 5]
a_list = [i * 5 for i in a_list] # iterate over the list, replacing the values

# In a real sense we are applying the mapping operation
map((lambda i: i * 5), a_list) # Apply lambda to every element in the list

items = [
  ("Product1", 10),
  ("Product1", 9),
  ("Product1", 12),
]

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items] #produces the same result as above
print(prices)

# Filetr returns a filter object, list will convert it to a list
filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item[1] for item in items if item[1] >= 10] # produces the same result as above
print(filtered)
