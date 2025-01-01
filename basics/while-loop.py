# guess = 0
# answer = 5

# while answer != guess:
#     guess = int(input("Guess: "))

msg = "I'm starting to love Python"
index = 0

# print(msg[0])
# print(msg[1])
# print(msg[2])
# ...
# print(msg[26])
#
# Iterate through msg
# what do we need:
    # length of msg
    # an index
print(len(msg))

while index < len(msg):
    print(msg[index])
    # counter
    # index = index + 1
    index += 1
