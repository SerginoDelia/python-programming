from tkinter import Variable
# Data Type	Class	Category	Kind	Mutable
# integers	int	numerics	Primitive	No
# floats	float	numerics	Primitive	No
# boolean	bool	booleans	Primitive	No
# strings	str	text sequences	Primitive	No
# ranges	range	sequences	Non-primitive	No
# tuples	tuple	sequences	Non-primitive	No
# lists	list	sequences	Non-primitive	Yes
# dictionaries	dict	mappings	Non-primitive	Yes
# sets	set	sets	Non-primitive	Yes
# frozen sets	frozenset	sets	Non-primitive	No
# functions	function	functions	Non-primitive	Yes
# NoneType	NoneType	nulls	--?--	No

#  class int
# whole numbers
number = 18
number = 20

# class float
# decimal numbers 3.14
my_float = 3.14

# Boolean
# class bool --> True or False

# String
# text sequence
my_string = "Today is Monday"
for text in my_string:
    print(text)

my_range = range(10)
for num in my_range:
    print(num)

# Tuples are read-only, non-primitive
my_tuple = (1, 2, 3, 4)

my_tuple2 = {1, 2, 3, 4, 5}
print(my_tuple2)

# Lists are mutable
my_list = ['Red', 'Blue', 'Yellow', 'Orange', 'Black']

# for paint in my_list:
#     print('Opening the can of ' + paint + ' paint.' )
#     print(f'Splashing the {paint} paint')
#     print(f'Pushing the {paint} paint aside')
#     print('-' * 20)

# Function starts with def keyword
# def display_output(iterable):
#     for paint in iterable:
#         print('Opening the can of ' + str(paint) + ' paint.' )
#         print(f'Splashing the {paint} paint')
#         print(f'Pushing the {paint} paint aside')
#         print('-' * 20)

# my_list = ['Red', 'Blue', 'Yellow', 'Orange', 'Black']
# my_num = [1, 2, 3, 4, 5]

# display_output(my_list)
# display_output(my_num)

# conditionals
# if, else; if, elif (can have an many elif as you want), else
# one if and one else

# smoking_age = int(input('Enter your age: '))
# '18' before the int function
# smoking_age = input("Enter your age (don't lie)")
# smoking_age = int(smoking_age)


def get_age():
    age = int(input('Enter your age: '))
    if type(age) == float:
        print('Enter a number')
        return
    if age < 18:
    # if 18 < 18: False
        print('You can\'t smoke')
    else:
        # otherwise
        print('you can smoke')

# if, else if, else JS
# constant = variable that doesn't
MY_CONSTANT = 21

# get_age()

age = 25
body_type = 'curvy'
melanin = True

if age == 25 and body_type != 'curvy':
    print('Jerard is not interested, get your weight up')
elif age >= 25 and body_type == 'curvy' and melanin != True:
    print('Jerard is not far away')
elif age >= 25 and body_type == 'curvy' and melanin == True:
    print('That\'s what Jerard is looking for')
else:
    print('Still looking, where are the chocolate girls?')

# write a  progragram that returns Fizz if a number is divisible by 3
# if the number is divisible by Buzz
# if the number is divible by 3 and 5 FizzBuzz
# Problem
#   if the number is divisble by 3 return Fizz
#   if number is divisble by 5 return Buzz
#   if number is divisble by 3 and 5 return FizzBuzz
