# variables

#  decalaring a variable called name and initializing it with a the string "John Smith"
#  Primitives
# In function they are passed by value
name = "John Smith"
num = 12
floating_point = 12.0  # Float
booleans = True  # True or False
12 == 12  # True
12 == 13  # False
12 > 6  # True
12 < 6  # False
12 >= 6  # True
12 <= 6  # False

# Mutable types
# In functions they are passed by reference
my_arrays = ["John", "Smith", "Samuel", "Nick"]
my_dictioanry = {"name": "Serge", "age": 30, "city": "New York"}
my_array2 = my_arrays

print(my_dictioanry["name"])
print(my_arrays)
print(my_array2)

my_arrays.append("Jane")
print(my_arrays)
print(my_array2)

#  Strings
name = "John Smith"
len(name)
# print(name[2])
# print(name[-2])
# print(len(name))

# Slicing
print(name[:])  # Jo

# Escape characters
# \"
print("John \"Smith\"")
print('John "Smith"')
print("John \tSmith")
