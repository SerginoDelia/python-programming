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
