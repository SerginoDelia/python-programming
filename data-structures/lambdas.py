# Lambdas

# Lambdas are one line functions, also know as anonymous functions in other
# programming languages. Use Lambdas when you don't want to use a function twice
# 3 in a program, they are just like normal functions and behave like them

# Syntax
# lambda argument: manipulate(argument)

# Example
add = lambda x, y: x + y

print(add(3, 5))

arr = [1, 2, 3]
print(list(map(lambda x: x * 2, arr)))

test = lambda x: x * 2
print(list(map(test, [2, 3, 5, 8])))

print(sum(map(test, arr)))

# Output 8

# Few useful cases for lambdas

# List Sorting
a = [(1, 2), (4, 1), (9,10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
# Output [(13, -30, (4, 1), (1, 2), (9, 10)]

# Parallel sorting of lists
# data = zip(list1, list2)
# data = sorted(data)
# list1, list2 = map(lambda t: list(t), zip(*data))
