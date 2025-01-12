# Ternary Expression
# A concise way to choose between 2 values based on some condition.
# They are often used as an expression on the right side of an assignment
# as function arguments, and as function return values

# value1 if condition else value2

if shape.sides() == 3:
    print("Triange")
else:
    print("Square")

print("Triangle" if shape.sides() == 3 else "Square")

value = 'Hello'

print('N/A' if value == None else value)

# Ternary expressions are recommended only when it doesn't sacrifice too much clarity
