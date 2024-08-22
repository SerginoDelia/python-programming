# print_name function has 2 parameters
def print_name(param1, param2):
  print(f"{param1}, {param2}")

# when the function is invoke we pass arguments
print_name("John", "Wick")

def multiply(*numbers):
  total = 1
  for number in numbers:
    total *= number
  return
  
print(multiply(1, 2, 3))


