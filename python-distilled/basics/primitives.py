# primitives variables and expressions
# interest calculator

principal = 1000 # initial amount
rate = 0.05 # interest rate
numyears = 5 # number of years
year = 1

# while loop continue to run as long as the expression following the while is True
while year <= numyears:
    principal = principal * (1 + rate)
    # print(year, principal)
    print(f'${year:>3d} {principal:0.2f}') # '>3d' means a 3 digit decimal nunmber right aligned
    # '0.2f' means a floating-point number with 2 decimal places of accuracy
    year += 1

# Math operations
# Functions
# abs(x) --> absolute Value
# divmod(x, y) --> returns (x//y, x%y)
# pow(x,y [,modulo]) --> returns (x ** y) % modulo
# round(x,[n]) --> rounds to the nearest multiple of 10 to the nth power
# the round function implements bankers rounding

print(round(0.5)) # --> 0
print(round(1.5)) # --> 2

# Bit manipulation operators
# Operation
# x << y --> left shift
# x >> y --> right shift
# x & y --> Bitwise and
# x | y --> Bitwise or
# x ^ y --> Bitwise xor (exclusive or)
# ~x --> Bitwise negation

# One would commonly use these with binary integers, ex:
a = 0b11001001
mask = 0b11110000
x = (a & mask) >> 4 # x = 0b1100 (12)
print(x)

# comparison operators
# x == y
# x != y
# x < y
# x > y
# x >= y
# x <=y

# Logical operators
# x or y
# x and y
# not x --> if x is false returns True; otherwise returns False

# it is common to write an expression that updates a value, ex:
# x = x + 1 --> x += 1
# y = y * n --> y *= n
#
