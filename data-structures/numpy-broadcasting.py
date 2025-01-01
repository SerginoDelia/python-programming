#! /usr/local/bin/python3

# Numpy Broadcasting
# Calculating an average 2 ways

import numpy as np

grades = [[60, 70, 80, 90, 100, 77], 
           [57, 75, 70, 80, 79, 80],
           [77, 88, 99, 67, 84, 99]]

print([sum(row)/len(row) for row in grades]) # calculate the avg for each row
numpy_grades = np.array(grades) # convert to Numpy 2d array
print(np.average(numpy_grades, axis=1)) # caluclate the average for each row
print(np.average(numpy_grades, axis=0)) # calculate the average for each column(!)
