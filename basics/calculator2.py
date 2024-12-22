# create a calculator that can add, subtract, multiply and divide
# PEDAC
# Problem:
    # create a calculator that can add, subtract, multiply and divide
# Example:
    # 12 + 4 = 16
# Data:
    # Input: integers, floats, operator(string). Output: interger, floats
# Algorithm:
    # input num1, operator, num2
    # return the value: num1 (operator) num2
    # if operator == + (add)
    # if operator == - (substact)
    # if operator == * (multiply)
    # if operator == / (divide)

def calculator():
    # text = input("prompt")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter the operator: ")
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2

print(calculator())
