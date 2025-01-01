# 1. Concatenate two strings, one with your first name and one with your last, 
# to create a new string with your full name as its value. For example, 
# if your name is John Doe, you should combine 'John' and 'Doe' to get 'John Doe'.
print('John' + ' ' + 'Doe')

# 2. This question may be a little challenging if your math skills are rusty. 
# Don't be afraid to take advantage of the hints. Try your best to solve the problem, 
# but don't feel compelled to complete it if you become frustrated.
# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

number = 4936
print(number % 10) # 6

number = number // 10 # 493
tens = number % 10 
print(tens) # 3

number = number // 10
print(number) # 49

hundreds = number % 10
print(hundreds) # 9

thousands = number // 10
print(thousands) # 4

# 3. What does the following code do? Why?
print('5' + '10')
# Concatenate '5' and '10' and returns '510'

# 4. Refactor the code from the previous exercise to use coercion to print 15 inste
print(int('5') + int('10'))

# 5. Will an error occur if you try to access a list element with an index greater 
# than or equal to the list's length? For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error? yes 'list index out of range' IndexError

# 6. To what value does the following expression evaluate?
'foo' == 'Foo' # False

# 7. What will the following code do? Why?
int('3.1415') # it raises a ValueError since the string value of 3.1415 is not a valid integer

# 8. To what value does the following expression evaluate?

print('12' < '9') # True, on the first comparison, it determines that '1' < '9', so '12' must be less than '9'


