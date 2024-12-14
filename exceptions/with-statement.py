# With Statement - works with certain kind of objects
# If the object has __enter__ and __exit__ magic methods, we can enter context management protocol
# we can use that object with the with statement

try:
  # file = open("exceptions.py")
  # returns a file object, python will automatically call file.close() whether
  # we have it or not
  with open("exceptions.py") as file:
    print("FIle opened")
  age = int(input("Age: ")
  xfactor = 10 / age
except TypeError as error:
  print("You didn't enter a valid age.")
except ZeroDivisionError:
  print("Age cannot be 0.")
else:
  print("No exeptions were thrown.")

# We can specify multiple types of exections in the except clause

try:
  age = int(input("Age: ")
  xfactor = 10 / age
except (TypeError, ZeroDivisionError) as error:
  print("You didn't enter a valid age.")
else:
  print("No exeptions were thrown.")
