# fizz buzz
# if the input is divisible by 3 return "Fizz"
# if the input is divisible by 5 return "Buzz"
# if the input is divisible by both 3 and 5 it will return "FizzBuzz"
# for any other number it will return the same input

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(3))   # Fizz
print(fizz_buzz(5))   # Buzz
print(fizz_buzz(15))  # FizzBuzz
print(fizz_buzz(7))   # 7
