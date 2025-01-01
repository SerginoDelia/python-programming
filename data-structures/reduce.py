# Reduce - useful function for performing some computation on a 
# list and returning the result. It applies a rolling computation
# to sequential pairs of value in the list

from functools import reduce

product = 1
my_list = [1, 2, 3, 4]

for num in my_list:
  product = product * num
  # product = 24

# With reduce
product = reduce(lambda x, y: x * y, my_list)
print(product)
