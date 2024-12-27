# Addition

print(38 + 4)
print(38.4 + 41.9)
print(38 + 41.5)

# Subtraction
print(38 - 4)
print(38.4 - 41.9)

# Multiplication
print(38 * 4)
print(38 * 41.5)

# Division
print(12 / 4)
print(16 / 2.5)

# Integer division with `//` 
# returns the largest whole number less than or equal to the floating point
# it rounds the result down to the nearest whole number 
print(16 // 3) # 5
print(16 // -3) # -6
print(16 // 2.3) # 6
print(-16 // 2.3) # 7

# Exponents
print(16**3)

# Modullo
# % returns the remainder

print(15 % 3) # 0
print(16 % 3) # 1
print(17 % -7) # 3
print(-17 % 7) # -3


# Floating Point Imprecison
# Floating point numbers have some precision issues to be aware of 
print(0.1 + 0.2 == 0.3) # False

import math 
math.isclose(0.1 + 0.2, 0.3) # True 

# decimal.Decimal can be used to make precise computations
# decimal.Decimal should always use strings
from decimal import Decimal 
Decimal('0.1') + Decimal('0.2') == Decimal(0.3) # True 


