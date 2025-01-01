# Write a program to find the most repeated character of the sentence below
# import pretty printing
from pprint import pprint

sentence = "This is a common interview question"

# P = write a program that return the character repeated the most
# E = this is = i
# D = input: string, output: string
# A = remove white space, convert the sentence to an object key(letter) value(occurance),
#     iterate through the dictioanry and return the highest value

sentence.strip()
letters = {}
 
for char in sentence:
  if char in letters:
    letters[char] += 1
  else:
    letters[char] = 1

result = sentence[0]

for k in letters:
  if letters[k] > letters[result]:
    result = k

print(result, letters[result])
print(f"{result}, {letters[result]} times")

print("Sorted Letters")
print(sorted_letters)

# refactored
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
      char_frequency[char] = 1
#pprint(char_frequency, width=1)

# this method returns all the key, value pairs as Tuples
char_frequency_sorted = sorted(
    char_frequency.items(), 
    key=lambda kv:kv[1], 
    reverse=True)
    
print(char_frequency_sorted[0])











