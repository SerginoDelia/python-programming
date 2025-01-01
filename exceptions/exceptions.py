# Exceptions - Terminates the execution of a program
# Handling Exceptions, if exceptions are not handled properluy
# the program will crash.  try: except clause

numbers = [1, 2]
try:  
  print(numbers[3])
except IndexError:
  print("enter a valid index")

# get input from the user
try:
  age = int(input("Age: "))
except ValueError as error: # variable error will include the details of the exception
  # this code will execute if we have an exception
  print("You didn't enter a valid age.")
  print(error)
  print(type(error))
else:
  print("No execptions were thrown")
