# Triple-quoted strings capture all the text until the terminating triple quote

print('''Content-type: text/html
<h1>Hello World</h1>
Click <a href="http://python.org">here</a>.
''')

# f-strings

base_year = 2025
principal = 1000

print(f'{base_year} {principal}')

# the format() method and a % operator are used sometimes to format strings as an
# alternative to f-string

print('Year {0} and principal: {1}'.format(base_year, principal))

# Strings are stored as sequences of Unicode characters indexed by integers
# starting at 0

a = 'Hello World'
print(a[0])
print(len(a))

# strings have a variety of methods

g = a.replace('Hello', 'Hello Cruel')
print(g)

print(g.split())

# Common string Methods
# s.endswith(prefix [,start [,end]]) - checks whether a string ends with prefix
# s.find(sub [, start [,end]]) - find the first occurnece of the specified substring or -1 if not found
# s.lower() - converts to lowercase
# s.replace(old, new [,maxreplace]) - replaces a substring
# s.split([sep [,maxsplit]]) - splits a string using the seperateor as a delimiter, maxsplit is the maximum number of splits to perform
# s.startwwith(prefix [, start [,end]]) checks whether a string starts with a prefix
# s.strip([chars]) - removes leading and trailing whitespace or characters supplied in chrs
# s.upper() converts string to uppercase

x = '37'
y = '42'
z = x + y # z = 3742 (string concatenation)
z = int(x) + int(y) # converted strings x and y to integers

# Non-sting values can be converted into a string representation by using the str(), repr() or format() functions
s = 'The value of x is ' + str(x)
print(s)

# repr() creates a string that you type into a program to exactly represent the value of an object
s = 'The value of x is ' + repr(x)
print(s)
s = 'The value of x is ' + format(int(x), '4d')
print(s)

# When debugging, use repr(s) to produce output because it shows you more information about a value and its type

# The format() function is used to convert a single value to a string with a specific formatting applied

x = 12.34567
print(format(x, '0.2f'))

# the fomat code given to format() is the same code you would use with f-strings when producing formatted output

print(f'{x:0.2f}') #same as formt() above
