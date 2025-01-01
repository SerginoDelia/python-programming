# 1. Determine whether Python has a method to lowercase a string, 
# for example converting 'Aloha, World!' into 'aloha, world!.

greeting = 'Aloha, World!'
print(greeting.lower()) 


# 2. Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

greeting = 'hello'
print(greeting[::-1])

index = len(greeting) - 1
result = ''

while index >= 0:
    result + greeting[index]
    index -= 1

print(result)

# 3. Locate the documentation for the list built-in object in Python Documentation.

# How can we access the second element ('and') in the list ['fish', 'and', 'chips']
my_list = ['fish', 'and', 'chips']
print(my_list[1])
print(my_list[0]) # first element
print(my_list[-1])
print(my_list[len(my_list) - 1])

foo = ['a', 'b', 'c']


# Recursion
# A function that calls itself

# factorial(3) 3 * 2 * 1 = 6

def fact(num):
    # base case
    print(num)
    if (num == 1):
        return 1

    return num * fact(num - 1)

print(fact(8))
print(fact(7))

# fibonacci 
# n - 1 + n - 2
# 3
# 0, 1, 1, 2, 3, 5, 8, 13
# 5
# 0, 1, 1, 2, 3


# my_tuple = (1, 2, 3)
#
# print(my_tuple)
#
# my_tuple = list(my_tuple)
# my_tuple.append(4) 
# print(my_tuple[1])
# print(my_tuple)

