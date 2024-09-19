# for loops
# 3 iterate over any object that is iterable

for x in "Pyhton":
    print(x)

for x in ['a', 'b', 'c']:
    print(x)

# print 0 through 4
for x in range(5):
    print(x)
# we can also use step (start, end, step)
# the range function does not return a list
for x in range(0, 10, 2):
    print(x)
# range is an object, range object takes a small amount of memory
print(type(range(5)))  # <class 'range'>

# for loop with conditionals
names = ["John", "Mary"]

for name in names:
    if name.startswith("J"):
        print("Found")
        break
else:
    print("Not found")
