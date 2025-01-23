# While, if and else statements are used for looping and
# conditional code execution

a = 10
b = 12

if a < b:
    print('Computer says Yes')
else:
    print('Computer says No')

# the bodies of the if, else clause are denoted by indentation,
# the else clause is optional

if a < b:
    pass # do nothing
else:
    print('Computer says No')

# use the elif to handle multiple-test cases

suffix = '.htm'
content = ''

if suffix == '.htm':
    content = 'text/html'
elif suffix == '.jpg':
    content = 'image/jpeg'
elif suffix == '.png':
    content = 'image/png'
else:
    raise RuntimeError(f'Unknown content type {suffix!r}')

# if you are assigning a value in combination with a test, use a conditonal expression:

# maxval = a if a > b else b
# this is the same as
# if a > b:
    # maxval = a
# else:
    # maxval = b

a = 10
b = 6

maxval = a if a > b else b
print(maxval) #10

a = 10
b = 60
maxval = a if a > b else b
print(maxval) #60

# Walrus operator: :=
# assignment of a variable and a conditional combined using the := operator

x = 0
while (x := x + 1) < 10: # prints 1, 2, 3, ..., 9
    print(x)

# The parenthesis used to surround the assignment expression are always required
# the break statement can be used to abort the loop early, it only applies to the
# innermost loop

x = 0
while x < 10:
    if x == 5:
        break # stops the loop, moves to Done below
    print(x)
    x += 1

print('Done')

# The continue statement skips the rest of the loop body and goes back tot eh top
# of the loop

x = 0
while x < 10:
    x += 1
    if x == 5:
        continue # skips the print(x), goes back to the start of the loop
    print(x)

print('Done')
