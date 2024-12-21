# Numpy and Axes

import numpy as np

a = np.ndarray((1000))  # creates a 1000 element array
a[:] = 1 # broadcast a 1 into it
a[200:500] = 3 # from 200-499, 3
a[500:70] = 7 #from 500-699, 7
a = np.reshape(a, (10, 10, 10)) # Rehape to a 10X10X10 matrix

print(np.sum(a, axis=0)) # sum all rows (y, z)
print(np.sum(a, axis=1)) # sum all columns (x, z)
print(np.sum(a, axis=2)) # Sum all depths (x, y)

# A word on Dimentions
# Programmers tend to think of demensions as array indexes
# my_array[0][2][4]

# This is fine, but consider this notation
# (0, 2, 4) RR**3

# We can view this as coordinates of a point in 3-dimentional space

