age = 22
if age >= 18:
    print("Adult")
elif (age >= 13):
    print("Teenager")
else:
    print("Child")

print("All done!")


# if, elif, else
# fizz buzz
# if the input is divisible by 3 return "Fizz"
# if the input is divisible by 5 return "Buzz"
# if the input is divisible by both 3 and 5 it will return "FizzBuzz"
# for any other number it will return the same input
#
#
# PEDAC - Problem, Example, Data, Algoritym, Code
#
# Problem:
    #  write a progam that returns "Fizz" if number is divisble by 3, 5 if input
    # is divisible by 5 and "FizzBuzz" if input is divisible by 3 and 5
# Example:
    # 5 -> Buzz
    # 3 -> Fizz
    # 15 -> FizzBuzz
    # 15 if divided by 5 first we will get "Buzz"
    # 15 if divided by 3 first we will get "Fizz"
# Data: input integers, output string
# Algoritym:
    # write a helper function that takes an input (integer) if the input is
    # we need the modulo operator to check if the input is divisible by 3 or 5 %
    # if the input is divisible by both 3 and 5 return "FizzBuzz"
    # divisible by 3 return "Fizz", if the input is divisible by 5 return "Buzz"
    # else the input is not divisible by 3 or 5 return the input

def fizz_buzz(input):
    if (input % 3 == 0):
        return "Fizz"
    elif (input % 5 == 0 and input % 3 == 0):
        return "FizzBuzz"
    elif (input % 5 == 0):
        return "Buzz"
    else:
        return "Input is not divisible by 3 or 5"

print(fizz_buzz(3))   # Fizz
print(fizz_buzz(5))   # Buzz
print(fizz_buzz(15))  # FizzBuzz
