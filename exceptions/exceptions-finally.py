# Exceptions Finally Clause - is always executed
# use when working with external resources

try:
  file = open("exceptions.py")
  age = int(input("Age: ")
  xfactor = 10 / age
except TypeError as error:
  print("You didn't enter a valid age.")
except ZeroDivisionError:
  print("Age cannot be 0.")
else:
  print("No exeptions were thrown.")
finally:
  file.close()

# We can specify multiple types of exections in the except clause

try:
  age = int(input("Age: ")
  xfactor = 10 / age
except (TypeError, ZeroDivisionError) as error:
  print("You didn't enter a valid age.")
else:
  print("No exeptions were thrown.")
