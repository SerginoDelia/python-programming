# Filter - creates a list of elements for which a funtion returns true

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))

print(less_than_zero)
