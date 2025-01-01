from webbrowser import Opera
# Create a simple calculator that add, substract, multiply and divide
# PEDAC
# Problem: create a basic math calculator that can add, substract, multiply and divide
# Example 1 + 1 = 2
# Data: input integers, output integers
# Algorithm: create a function that takes two inputs and an operator
# ask the use for the inputs
# if the operator is "+" return the sum of the two inputs
# if the operator is "-" return the difference of the two inputs
# if the operator is "*" return the product of the two inputs
# if the operator is "/" return the division of the two inputs
# Code:

# num1
# num2
# operator
# input("promt")
def calculator():
    # get the first number
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    operator = input("What operation would you like to do? ")
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case _:
            return num1 / num2

print(calculator())

arr = [1, 2, 3]
test = (map(lambda x: x * 2, arr))
print(arr)
