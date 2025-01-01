# Mappings represent an unordered collection of objects that are stored as key-value pairs.
# The dictionary (class dict) is the most common mapping in Python 

my_dict = {
    'dog': 'bark',
    'cat': 'meow',
    'pig': 'oink'
}

# Dictionary literals also uses a multi-line format
my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
        'Michael Palin',
        'Terry Jones',   
    ],
    'first_season': 1969,
    'last_season': 1974,
    'reboot_season': 'None',
}

my_dict = {
    'dog': 'bark',
    'cat': 'meow',
    'pig': 'oink'
}

print(my_dict['cat'])

my_dict['cat'] = 'purrs'
print(my_dict)
