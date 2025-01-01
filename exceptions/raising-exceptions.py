# Raising Exceptions - raising exceptions is costly
from timeit import timeit # calculate the execution time of python code

def calculate_xfactor(age):
  if age <= 0:
    raise ValueError("Age cannot be 0 or less")
  return 10 / age

try:
  calculate_xfactor(-1)
except ValueError as error:
  print(error)

# Cost of raising exceptions: Raise exceptions if you really have to
code1 = """
def calculate_xfactor(age):
  if age <= 0:
    raise ValueError("Age cannot be 0 or less")
  return 10 / age

try:
  calculate_xfactor(-1)
except ValueError as error:
  # print(error)
  pass  # pass statement is a statement that doesn't do anything
"""

code2 = """
def calculate_xfactor(age):
  if age <= 0:
    return None
  return 10 / age

xfactor = calculate_xfactor(-1)
if xfactor == None:
  pass
"""

print(timeit("First code=", code1, number=10000)) # number is the number of times we want to execute the code 
