msg = "Today is a good day!"

for letter in msg:
    print(letter)

# print(msg[0])
# print(msg[1])
# print(msg[len(msg) - 1])
# print(msg[-1])

# print(len(msg))
# index = 0
# while index < len(msg):
#     print(msg[index])
#     # index = index + 1
#     index += 1

name = 'John'
print(f'Hi, {name}')

name = 'John'
print('Hi, ' + name)

print(f'What is the message of the day: {msg}')

# Functions and Methods
# functions len()
# method .upper()
print(len(msg)) #function
print(msg.upper()) # method

# for letter in msg:
#     print(letter)

def loop_through_letters(str):
    for letter in str:
        print(letter)

msg = "Today is a good day!"
loop_through_letters(msg)

msg2 = "Tommorrow will be a good day"
loop_through_letters(msg2)

lizzo = [1, 2, 3, False, True, "Day"]
loop_through_letters(lizzo)

my_list = [1, 'xyz', True, [2, 3, 4, ['yes', 'no']]]
print(my_list[3])
print(my_list[3][0])
print(my_list[3][3])
print(my_list[3][3][0])

my_tuple = (1, 2, 3, 4)
loop_through_letters(my_tuple)

for placeholder in my_tuple:
    print(placeholder)

my_range = range(10)
print(range)

my_list2 = list(my_range) # [1, 2, 3, ...]
print(my_list2)

my_tuple2 = tuple(my_range)
print(my_tuple2)

my_tuple2 = tuple(my_list2)
print(my_tuple2)

# Dictionaries

my_dict = {'dog': 'barks', 'cat': 'meows', 'pig': 'oinks'}

my_dict2 = {
    'dog': 'barks',
    'cat': 'meows',
    'pig': 'oinks',
}

print(my_dict)
print(my_dict['dog'])
print(my_dict['cat'])

print(my_dict2)
print(my_dict2['dog'])
print(my_dict2['cat'])

my_set = set("Today is a good day!")
print(my_set)

custom_list = []
msg = "Today is a good day!"

print(custom_list)
for letter in msg:
    print(f'Adding letter: >>> {letter}')
    custom_list.append(letter)

print(custom_list)

custom_set = set(custom_list)
print(custom_set)

# Mutable
my_arr = [1, 2, 3]
print(my_arr)

my_arr.append(4)
print(my_arr)

my_arr2 = my_arr
print(my_arr2)

my_arr2.pop()
print(my_arr2)
print(my_arr)

new_arr = my_arr

my_arr = ["new", "house"]
my_arr2 = my_arr

print(new_arr)
print(my_arr)
print(my_arr2)

# Slicing

msg = "Today is a good day!"
my_arr = [1, 2, 3, 4, 5]

print(msg[0:5])
print(my_arr[1:4])

# If, else, or if, elif, else --> we can have as many elif as we want

if my_arr[0] == 1:
    print('Correct')
else:
    print('Incorrect')


if my_arr[3] == "true":
    print('if is correct')
elif my_arr[3] == 4:
    print('elif is correct')
else:
    print('incorrect')

# name = input('Enter your name: ')
# print(name)

# get name from user, if the first 2 letters start wit li, reject.

name = input('Enter your name for Darian Security (No LIZZO\'s): ')

if name[0:2].lower() == 'li' or name.lower() == 'lizzo':
    print('No')
else:
    print('Wait for further inspection')
