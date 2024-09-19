# list
letters = ["a", "b", "c", "d"]

# matrix - a 2-demensional list
matrix = [[0, 1], [2, 3]]

# a list of 5 0's
zeros = [0] * 5  # the * repeat the items in the list
print(zeros)

# we can concatenate lists
combined = zeros + letters
print(combined)

# list function (takes an iterable), we can pass any iteratble and convert it to a list
numbers = list(range(20))  # create a list of numbers from 0 - 19;
# 20 is not included
print(numbers)

chars = list("Hello World")
print(chars)
print(len(chars))

print(letters[0])  # "a"
print(letters[-1])  # "d"

# change an element
letters[0] = "A"
print(letters)  # ["A", "b", "c", "d"]

# slice [start_index:end_index]
print(letters[0:3])  # ["A", "b", "c"]

# slice with a step, returns every second element of the list
print(letters[::2])

numbers = list(range(20))
print(numbers)
print(numbers[::2])  # return every second element in the list

# return every item in the list, in reverse order
print(numbers[::-1])
