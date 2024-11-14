# Comprehension
# Syntax: [expression for item in items]

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
