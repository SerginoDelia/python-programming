# For Loops
# dynamically typed
names = ['black', 'musty', 'dusty', 'sloppy', 5]
lizzo = names
lizzo.pop()
lizzo.append('flat booty')

# print(yomomma)

# for placeholder in yomomma:
#   print(placeholder)

print("while loop --------------")

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

# write a recursive function that prints all the names in the list
def print_names(names):
  if len(names) == 0:
    return
  print(names[0])
  print_names(names[1:])

print("")
print("Recursion")
print("")
print_names(names)