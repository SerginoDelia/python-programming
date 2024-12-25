# Integers

# data type `int()`, whole numbers
1
2
-3
234891234
131_587_465_014_410_491

# Floats 
# data type `float` represents decimals, real numbers

1.0
1.4142
-3.14159
42348.912346
131_597_565.014_410_491 # underscores are used to break up numbers

# In theory floats can represent any number, with or without a decimal point

# Python prints extremely large and small floats using scientific notation
print(3.14 * (10**20)) # 3.14e+20
print(3.14 * (10**-20)) # 3.14e-20

# You can also use scientific notation when writing float literals
print(3.14e+20 / 2.72e-15) # 1.1544117647058823e+35

print(3 * (10**20)) 

# If you want to use scientific notation to write larger Integers you must us the `int()` function
print(int(3e+20))



