# match_case_calculator.py

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for valid operation
while True:
    operation = input("Choose the operation (+, -, *, /): ").strip()
    if operation in ["+", "-", "*", "/"]:
        break

# Perform calculation using match-case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {int(result) if result.is_integer() else result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {int(result) if result.is_integer() else result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {int(result) if result.is_integer() else result}.")
    case "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {int(result) if result.is_integer() else result}.")
