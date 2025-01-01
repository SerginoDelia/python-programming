# Looping Over Lists

letters = ["a", "b", "c"]

for letter in letters:
  print(letter)

# enumerate built-in function will return the index of each item in the list
# in each iteration we will get a tuple (0, 'a')
# Tuples are similar to a list, but it's read only
for letter on enumerate(letters):
  print(letter)

# unpacking the items list
for index, letter in enumerate(letters):
  print(index, letter)

