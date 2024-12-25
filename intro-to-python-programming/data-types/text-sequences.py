# Text sequences are string of characters, such as words, dates,
# foreign text and so on 

print('Hello!')
print("He's pinning for the fjords")
print('1969-07-20')

# Text sequences can often be treated as ordinary sequences

greeting = 'hello'
for letter in greeting:
    print(letter)

# String literals and dealing with quotes
# string literals can be written in single, double, or tripple quotes

msg = 'Hello there' 
msg2 = "Monty Python's Flying Circus"
msg3 = '''King Arthur: "What is your name?"
Black Night: "None shall pass!"
'''

msg4 = """This is a 
tripple double quote
"""

# Strings that contains both double and single quotes
print("""My nickname is "Wolfy". What's yours?""")
print('My nickname is "Wolfy". What\'s yours?')
print("My nickname is \"Wolfy\". What's yours?")

# the backslash or escape charater `\` tells the computer that the next character 
# isn't syntactiv but is part of the string 

# `/` has no significance between quotes
print("C:\\Users\\Xyzzy")

# Indexing strings 
my_str = 'abc'
print(my_str[0])
print(my_str[1])
print(my_str[2])

# negative integers can be used to access character based on the distance from the end of the string
print(my_str[-1])
print(my_str[-2])

# Raw strings and f-strings 
# String literals with an `r` prefix are raws string literals
# raw string literals don't recognize escapes, `\` can be used freely
print("C:\\Users\\Xyzzy") # Each \\ produces a literal \
print(r"C:\\Users\\Xyzzy") # raw string literal

# f-strings - formatted string literals enables opration called "string interpolation"
print(f'5 plus 5 equals {5 + 5}')
my_name = 'Karl'
print(f'My name is {my_name}')

# you may use as many {epression} substrings as needed in an f-string
# if you need a literal { or } character in an f-string, you can escape them by doubling the 
# { and } characters you want to use as literal characters

foo = 'hello'
print(f'Use {{foo}} to embed a string: {foo}') # Use {foo} to embed a string: hello

# if you print a number, no matter its size, it wont be printed with underscores or even commas
# unless you use the appropriate f-string 
print(f'{12345678:_}') # 123_456_789
print(f'{123456789:,}') # 123,456,789

# None when you want nothing
# `None` is the literal whose value is the lone representative of the `NoneType` class class 

# sequences - represnts an ordered collection of objects


