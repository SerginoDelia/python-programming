# Control Flow
# FizzBuzz

# num = int(input('Enter a number: '))

# if num % 3 == 0 and num % 5 == 0:
#     print('FizzBuzz')
# elif num % 3 == 0:
#     print('Fizz')
# elif num % 5 == 0:
#     print('Buzz')
# else:
#     print('Number is not divisible by 3 or 5')

# num = int(input('Enter a number: '))

# # match/case statements

# match num:
#     case 1 | 2 | 3 | 4 | 5:
#         print('Num is 1, 2, 3, 4, or 5')
#     case 6:
#         print('Num is 6')
#     case _:
#         print('Num is neither 5 nor 6')

# 0 - no permission
# 1 - execute
# 2 - write
# 3 - execute and write
# 4 - read
# 5 -execute and read
# 6 - read and write
# 7 - read, write, and execute
# chmod user,group,other

# Ternary Expression
# value1 if conditon else value2

num = 5
num2 = 10

print(num if num == 5 else num2)
print(num if num == 2 else num2)

# Collections
# lists [1, 2, 3, 'four'] ordered collection - mutable
# dictionaries {'name': 'Serge', 'day': 'Sunday'} - key value pairs - dictionaries
# sets {'a', 1, 2, 3} unordered collection of unique value - mutable
# frozenset frozenset({1, 2, 3, 4}) immutable
# tuples (1, 2, 3, 'four', true) - read only ordered pairs - immutable - read only
# range range(0,5) - immutable

# List Syntax
# lists are 0 indexed - meaning it starts at 0
# [element1, element2, element3, ...]
# We can put anything in the list
# ['day', 12, true, false, '', 3.14]

names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]

names.append('Tom')
print(names)

first_two_names = names[0:2]
print(first_two_names)

minus_first_two_names = names[2:]
print(minus_first_two_names)

names_lenth = len(names)
minus_first_two_names = names[2:names_lenth]
print(minus_first_two_names)

# insert syntax --> insert(index, value)
names.insert(1, 'Eve')
print(names)

names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]

# iterate through the list
for name in names:
    print(name)

# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

index = 0
while index < len(names):
    print(names[index])
    index += 1

#  returns a tuple (index, element)
for name in enumerate(names):
    print(name)

# our own tuple
print('My tuple')

index = 0
while index < len(names):
    my_tuple = (index, names[index])
    print(my_tuple)
    index += 1

# Creata a list of tuples --> [(index, element), (index+1, element), ...]
names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]

# using enumerate
names_tuple = []

for name in enumerate(names):
    names_tuple.append(name)

print(names_tuple)

names = [ 'Dave', 'Paula', 'Thomas', 'Lewis' ]
names_tuple_2 = []
index = 0

while index < len(names):
    custom_tuple = (index, names[index])
    names_tuple_2.append(custom_tuple)
    index += 1

print(names_tuple_2)
