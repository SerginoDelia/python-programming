# Swapping Variables

x = 10
y = 11

z = x
x = y
y = z

print("x = ", x)
print("y = ", y)

x = 20
y = 21
x, y = y, x # we're defining a Tuple and unpacking it, same as x, y = (21, 20) 

print("x = ", x)
print("y = ", y)
