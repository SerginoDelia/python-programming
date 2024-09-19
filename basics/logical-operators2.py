# Python has 3 logical operators
# and
# or
# not

name = ""

# to search if name is an empty string
if not name:
    print("Name is empty")

age = 22
if age >= 18 and age <= 65:
    print("Eligible")

# chaining comparison operators (same as above)
if 18 <= age < 65:
    print("Eligible")

# ternary operator
message = "Eligible" if age >= 18 else "Not eligible"
