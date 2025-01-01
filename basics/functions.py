def increment(number, by):
    return (number, number + by)


print(increment(2, 3))

# we can also prefix the second argument
print(increment(2, by=3))

# we can also anotate (-> returning a tuple)


def increment_two(number: int, by: int) -> tuple:
    return (number, number + 3)


print(increment_two(2, 3))

# print_name function has 2 parameters


def print_name(param1, param2):
    print(f"{param1}, {param2}")


# when the function is invoke we pass arguments
print_name("John", "Wick")


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return


print(multiply(1, 2, 3))
