# Simple Calculator
def calculator():
    print("Select an operation:")
    print("Addition (+)")
    print("Subtraction (-)")
    print("Multiplication (*)")
    print("Division (/)")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    choice=input("Choose the Operator:")
    if choice == '+':
        result = num1 + num2
    elif choice == '-':
        result = num1 - num2
    elif choice == '*':
        result = num1 * num2
    elif choice == '/':
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
            return
        result = num1 / num2

    print(f"The result of {num1} {choice} {num2} is: {result}")

calculator()
