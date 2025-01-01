# Formatted Strings

first = "Serge"
last = "Delia"

# Concatenation
full = first + " " + last
print(full)

# Formatted strings
fullname = f"{first} {last}"
print(fullname)

# When using formatted strings, you can put any valid expression into curly braces
fmt_string = f"{len(first)} {2+2}"
print(fmt_string)

day = "Sunday"
wheather = "Sunny"

print(f"Today is {day} and it's {wheather}. The first letter of today is: {day[0:1]}")
