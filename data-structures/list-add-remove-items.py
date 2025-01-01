# Adding and Removing Items

letters2 = ["a", "b", "c"]

# Add at the end of the list use append() method
letters2.append("d")

# Add items at a specific position, use insert() method
letters2.insert(0, "-") # insert item at the beginning of the list

# Removing Items
# Remove items at the end of the list, use pop() method
letters2.pop()

# pass an index to remove items at a specific index
letters2.pop(0)

# use remove an item that you don't know the index of
letters2.remove("b")  # this will remove the first occurence of the letter "b"

# delete an item by its index or a range of items
del letters2[0:3]

# delete all the items in the list, use clear() method
letters.clear()
