# Dictionaries - collection of key,value pairs, Object in JavaScripts

point = {"x": 1, "y": 2}

# we can also use the dict() function
point2 = dict(x=1, y=2)

print(point["x"])

# change the value of "x" to a new value
point["x"] = 10
# we can add new keys and value
point["z"] = 20
print(point)

# When reading the value if we use an invalid key we get an error
if "a" in point:
  print(point["a"])
else:
  print("a is not a key")

# Other solution is the get() method, if the key doesn't exist it returns None
print(point.get("a"))

# Or we can pass a default value as a second argument, if the first argument doesn't
# exist returnt the second argument
print(point.get("a", 0))

# Delete an item
del point["x"]
print(point)

# Loop over dictionairies

for key in point:
  print(key, point[key])

for key, value in point.items():
  print(key, value)

# Loop over the items and returns a tuple for each key, value pair
for x in point.items():
  print(x)
