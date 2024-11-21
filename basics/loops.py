# For Loops
# dynamically typed
names = ['John', 'Wick', 'Trump', 'Kamala', 'Joe', 'Smith']
new_names = names
# new_names.pop()
# new_names.append('Samuel')

for name in names:
  print(name)
  
print("Print the names with their index\n")

for name in enumerate(names):
  print(name)

print("while loop --------------\n")

# print the items at a given index
for name in enumerate(names):
  print(name[0], name[1])

index = 0
# # while true
# while index < len(names):
#   print(names[index]) # names[4]
#   index += 1 # (same) index = index + 1

# while True:
#   print(index)
#   index

# print(names[0])
# print(names[4])

people = {
  'Donald': 'Trump', 
  'Kamala': 'Harris', 
  'JD': 'Vance', 
  'Year': 2024
  }
candidates = people
candidates["Joe"] = "Biden"


for first_name, last_name in people.items():
  print(first_name, last_name)

for first_name in people.keys():
  print(first_name)

for last_name in people.values():
  print(last_name)

# Recursion (similar to loops)
def print_names(names):
  if len(names) == 0:
    return
  print(names[0])
  print_names(names[1:])

print("")
print("Recursion\n")
print("")
print_names(names)

# Recursion (similar to loops)
print("")
print("Print print_names2 funcion\n")

names = ['musty', 'dusty', 'sloppy', 5]
# A recursive function is a function that calls itself
# my list take an array, or a string, index is set to 0
def print_names2(my_list, index=0):
    # Starting the resursive function loop will be printed only once
    if index == 0:
        print("Starting the recursive function loop")

    # the length of the list is the base case
    # last element of the list will always be len(my_list) - 1
    if index >= len(my_list):
        print("end of list")
        return
    
    # print the element of the list at the index
    print(my_list[index])

    # call the function again with the same list and the next index
    return print_names2(my_list, index + 1)

# Example usage
print_names2(names)
print_names2("Sergino Delia")