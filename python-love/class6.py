# For loops

my_list = [1, 2, 3, True, 'Hello', 'Smith', 'John', 'Anna', 'Lauren']

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])

for placeholder in my_list:
    print(placeholder)

msg = 'Today is Monday'

for letter in msg:
    print(letter)

# While loop
# While the expression is true, the loop will run

my_list = [1, 2, 3, True, 'Hello', 'Smith', 'John', 'Anna', 'Lauren']
print(len(my_list))
index = 0

print('#' * 20)
while index < len(my_list):
    print(my_list[index])
    # index = index + 1
    index += 1

# Functions

def say_hello():
    print('Hello')

say_hello() # calling/invoked say_hello function

print(f'{'#' * 20} Fuctions {'#' * 20}')
def print_elements(my_arr):
    for element in my_arr:
        print(element)

my_list = [1, 2, 3, True, 'Hello', 'Smith', 'John', 'Anna', 'Lauren']

print_elements(my_list)

# Conditionals: if, elif, else
# We can only one and one else, but can have multiple elif

num1 = 7
num2 = 10

if num1 < num2:
    print('num1 is smaller than num2')
else:
    print('num1 is not smaller than num2')

if num1 != num2:
    print('num1 is not equal to num2')

if num1 > num2:
    print('num1 is greater')
elif num1 == num2:
    print('num2 is greater')
else:
    print('num1 and num2 are not equal')

num1 = 7
num2 = 10
# a if a > b else b

# (conditon) ? this if true : else
# vpc_id = endswith(each.key, 'public') ? aws_vpc.main.id : aws_vpc.private.id

# if num1 < num2:
#     print('num1 is smaller')
# else:
#     print('num1 is greater')

print('num1 is smaller') if num1 < num2 else print('num1 is greater')

my_list = [1, 2, 3, True, 'Hello', 'Smith', 'John', 'Anna', 'Lauren']

# list slicing
# ge the first 3 elements
print(my_list[0:3])
print(my_list[2:3])
print(my_list[4:])

print(len(my_list))

my_set = set(my_list)
print(my_set)
