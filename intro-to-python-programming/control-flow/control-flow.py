# Control Flow 
# Conditional is a fork or multiple forks 
# The simplest conditionals use a combination of if statements with comparison
# and logical operators (<, >, <=, >=, ==, !=, and, or, and not) to direct traffic
# they use the keywords if, elif, else 

value = int(input('Enter an number: '))

if value == 3:
    print('value is 3')
else: 
    print('value is NOT 3')

# Note that else block isn't a proper statement; it's part of the if statement

# We can test if statement inside an out if: nest if statement 

value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

# Avoid using nested if statements when possible, they quickly becomes difficult to read
# If nested statements are used keep the nesting 2-3 levels deep 


if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
else:
    print('value is NOT 3 or 4')

# the code above produces the same result as the previous nested if statament 

# the if statement may contain as many lines as you want 

if value == 3:
    print('value is 3')
    print('value is an odd number')
    print('value is a prime number')
elif value == 4:
    print('value is 4')
    print('value is an even number')
    print('value is NOT a prime number')
elif value == 9:
    print('value is 9')
    print('value is an odd number')
    print('value is NOT a prime number')
else:
    print('value is something else')

# if statement blocks that does nothing must use the pass statement 

if value == 3:
    print('value is 3')
elif value == 4:
    print('value is 4')
elif value == 9:
    pass # pass we don't care about 9
else:
    print('value is something else')

# adding a comment to a pass statement is good practice so future programmers know why it is there 

# Comparison 
# comparison returns a Boolean value: True or False 
# the expression to the left and right side of an operator are its operands.
# the equlaity comparison x == y uses the == operator with two operands, x and y 

# == operator returns True 

print(5 == 5) # True 
print(5 == 4) # False

print('abc' == 'abc')
print('abc' == 'abcd') # False 

print(5 == '5') # False

print([1, 2, 3] == [1, 2, 3]) # True
print([1, 2, 3] == [3, 2, 1]) # False

# In most cases operands must have the same type and value to be equal. There are some places
# where types can be mixed. For instance, integers and floats that are mathematically equivalent are
# usually, but not always, considered equal 

print(5 == float(5)) # True

big_num = 12345678901234567
print(float(big_num) == big_num) # False

# Enormous floast lack precision at around 18 significant digits on most modern machines.
# that can lead to surprises if you happen to work with big numbers 

# string comparisons are case sensitive: str.lower and str.upper methods can be used to 
# achieve a case sensitive comparison

print('abc' == 'aBc') # False
print('abc'.lower() == 'aBc'.lower()) # True 
print('abc'.upper() == 'aBc'.upper()) # True 

# use casefold when working with non-US characters, it's best practice to 
# use casefold instead of lower or upper, especially when comaparing strings 

'straße'.casefold() == 'strasse'.casefold()

# != inequality oprator 
# the inverse of ==

print(5 != 5) # False
print(5 != 4) # True 
print('abc' != 'abc')     # False
print('abc' != 'aBc')     # True
print(5 != '5') # True

# < and <=
# less than operator ,< returns True when that value of the left operand has a value 
# that is less than the value of the right, otherwise False
# The less than or equal to operator (<=) is similar, 
# but it also returns True when the values are equal; < returns False when the operands are equal.

print(4 < 5)              # True
print(5 < 4)              # False
print(5 < 5)              # False

print(4 <= 5)             # True
print(5 <= 4)             # False
print(5 <= 5)             # True

print('4' < '5')          # True
print('5' < '4')          # False
print('5' < '5')          # False

print('42' < '402')       # False
print('42' < '420')       # True
print('420' < '42')       # False

# > and >=
# The greater than operator (>) returns True when the value of the left operand has a 
# value that is greater than the value on the right, False otherwise. 
# The greater than or equal to operator (>=) is similar, but it also returns 
# True when the values are equal; > returns False when the operands are equal.

print(4 > 5)              # False
print(5 > 4)              # True
print(5 > 5)              # False

print(4 >= 5)             # False
print(5 >= 4)             # True
print(5 >= 5)             # True

print('4' > '5')          # False
print('5' > '4')          # True
print('5' > '5')          # False

print('42' > '402')       # True
print('42' > '420')       # False
print('420' > '42')       # True

# Logical operators
# provides the ability to combine conditions:

# not - returns True when its oprand is False and returns False the when operand is True
# it negate its operand

print(not True) # False 
print(not False) # True 
print(not(4 == 4)) # False
print(not(4 != 4)) # True

# Unlike most oprators, not takes a single operand 

# and, or 
# The and operator returns True when both operands are True. 
# It returns False when either operand is False. 
# The or operator returns True when either operand is True and False when both operands are False.

print((4 == 4) and (7 == 7)) # True
print((4 == 4) and (7 == 3)) # False

print((4 == 4) or (7 == 7)) # True 
print((4 == 4) or (7 == 3)) # True
print((4 == 9) or (7 == 7)) # True 
print((4 == 9) or (7 == 3)) # False

# Short Circuits
# the and or oprators use a mechanism called short circuit evaluation to evaluate their operands 

# is_red(item) and is_portable(item)
# is_green(item) and has_wheels(item)

# the first expression returns True when an item is red and portable 
# if either condition is false, then the overall result must be false 

# The second expression retruns True when the item is either green or has wheels
# if the item is green, it doesn't have to decide whether it has wheels 
# Python short-circuits the entire expression once it knows that item is green; the expression must be True

