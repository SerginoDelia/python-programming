course = "Python Programming"

# return the number of characters in the String course
len(course)

# bracket notation
course[0]  # get the first character
print(course[0])

# return first character from the end or (the last character of the string)
course[-1]

course[-2]  # return the second character from the end

# Slicing a string
# [start_index:end_index] - doesn't return the character at the end_index
course[0:3]

# same as above, Python will pass 0 as the start index
course[:3]

# if the end index is excluded, Pyhton will pass the length of the string
course[0:]

# if the start_index and end_index is excluded, Python will return the string
course[:]

print(id(course))
print(id(course[0]))
