def multiply(a, b):
    return a * b


print(multiply(3, 5))

# if we pass an * asterisk python will see that parameter as a tuple
# a tuple is like a list


def multiply_two(*list):  # passing an arbitratory number of arguments
    total = 1
    for num in list:
        total *= num
    return total


print(multiply_two(2, 3, 4, 5))


def save_user(**user):
    print(user)
    print(user['id'])
    print(user['name'])


save_user(id=1, name="admin")  # returns a dictionary
# {'id': 1, 'name': 'admin'}
# 1
# admin
