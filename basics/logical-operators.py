# logical operator: or
# one of the conditions must be true
names = ["John", "Smith", "Samuel", "Nick"]

def print_names(item, index=0):
  # code will execute if one of the conditons are true
  if index == 0 or index < len(item):
    print(item[index])
  else:
    return
  
  return print_names(item, index+1)

print_names(names)

# logical operator: and
# both conditions must be true
high_income = False
good_credit = True
student = True

if good_credit and high_income:
  print("You're eligible") 
else:
  print("You're eligible")

# logical operator
# inverse of true or not equal

if (high_income or good_credit) and not student:
  print("you're eligible")
else:
  print("not eligible")




  