course = "  Python Programming "

# convert to uppercase
print(course.upper())

# convert to lowercase
print(course.lower())

# conver to title case
print(course.title())

# trimming whitespace from the beginning and end
print(course.strip())

# left strip for removing the whitespace from the beginning
print(course.lstrip())

# right strip for removing the whitespace from the end
print(course.rstrip())

# find the index of a character
print(course.find("Pro"))

# replace characters, (replacing all P with -)
print(course.replace("P", "-"))

# check for a character or sequence of characters in a string return true or false
print("Programming" in course)

# we can also use the not operator, returns true or false
print("Programming" not in course)
