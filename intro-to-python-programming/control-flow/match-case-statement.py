# match/case Statement
# A match statement in it's most basic for is similar to an if statement
# It compares a single value against multiple values

value = 5

match value:
    case 5:
        print('value is 5')
    case 6:
        print('value is 6')
    case _:
        print('value is neither 5 nor 6')

# the example above is identical to the following if/else statement

value = 5

if value == 5:
    print('value is 6')
elif value == 6:
    print('value is 6')
else:
    print('value is neither 5 nor 6')

# to match multiple values in a case, use the | character to seperate item values

value = 5

match value:
    case 1 | 2| 3| 4:
        print('value is less than 5')
    case 5 | 6:
        print('value is 5 or 6')
    case _:
        print('value is not 1, 2, 3, 4, 5, or 6')
