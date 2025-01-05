# while (condition is true)
#   do this
# increment

# x = 0
# while x <= 10:
#     print(x)
#     # x = x + 1
#     x += 1

names = ['John', 'Smith', 'Anderson', 'Jim', 'Paul', 'Tom', 'Chuck']
print(len(names)) # 7
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])
# print(names[4])
# print(names[5])
# print(names[6])

index = 0
# length = len(names) - 1
# while index <= length:
while index < len(names):
    print(names[index])
    # index = index + 1
    index += 1

names = ['John', 'Smith', 'Anderson', 'Jim', 'Paul', 'Tom', 'Chuck']

for i in names:
    print(i)

print_names = [name + ' ' + 'Sunday' for name in names]
print(print_names)

update_name = []
for name in names:
    update_name.append(name + ' ' + 'Sunday')
print('Update Name')
print(update_name)

# write a program that loops through the names in names
# game: if I call a number you have to give the name in arry at number index
# if I go over the index I loose
# ['apple', 'banana', 'strawberry']
#       0,      1 ,     2
#

# index = 0
# # length = len(names) - 1
# # while index <= length:
# while index < len(names):
#     print(names[index])
#     # index = index + 1
#     index += 1

print('Walrus Operator')
x = 0
while (x := x + 1) < 10: print(x)

names = ['John', 'Smith', 'Anderson', 'Jim', 'Paul', 'Tom', 'Chuck']

index = -1
while (index := index + 1) < len(names): print(names[index])

# index = -1
# index += 1
# while index < len(names):
#     print(names[index])
#     index += 1

index = 0
while index < len(names):
    print(names[index])
    index += 1

# conver line 73-77 to a function
print('While function')

def print_names(my_list, index=0): # index=0 is a default parameter
    # index = 0
    while index < len(my_list):
        print(my_list[index])
        index += 1

lizzo = ['Lizzo', 'Music']
print_names(lizzo)
print_names(names)
print_names(names, 3)

names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []
index = 0

while index < len(names):
    # upper_name = names[index].upper()
    upper_names.append(names[index].upper())
    index += 1

print(upper_names);
# ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

# Prints 1, 2, 3, ..., 9
# The parentheses used to surround an assignment expression are always required.
# The break statement can be used to abort a loop early. It only applies to the innermost
# loop. For example:
# x = 0
# while x < 10:
# if x == 5:
# print(x)
# x += 1
# break # Stops the loop. Moves to Done below
# print('Done')
