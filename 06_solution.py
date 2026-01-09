num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
while True:
    operation = input("Enter a operation(+,-,*,/,%,-):")

    if operation == "+":
        result = num1 + num2
        print(f"Result:{result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result:{result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result:{result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Result:{result}")
        else:
            print("num2 should not be zero")
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
            print(f"Result:{result}")
        else:
            print("num2 should not be zero")
    elif operation == "-":
        print("Thank you for using the calculator.")
    else:
        print("Please give a valid operation")
