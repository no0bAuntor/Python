operator = input(
    "Which operation you want to perform? \n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication(*)\n4. Division(/)\n "
)

if operator == "+":
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    print(f"Addition of {x} and {y} is {round(x+y,3)}")

elif operator == "-":
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    print(f"Subtraction of {x} and {y} is {round(x-y,3)}")

elif operator == "*":
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    print(f"Multiplication of {x} and {y} is {round(x*y,3)}")

elif operator == "/":
    x = float(input("Enter 1st number: "))
    y = float(input("Enter 2nd number: "))
    print(f"Division of {x} and {y} is {round(x/y,3)}")
