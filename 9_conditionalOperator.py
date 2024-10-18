num = int(input("Enter an integer: "))
result = "Even" if num % 2 == 0 else "Odd"
print(result)


num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))
max_num=num1 if num1>num2 else num2
min_num=num1 if num1<num2 else num2
print(f"Maximum number between {num1} & {num2} is {max_num}")
print(f"Minimmum number between {num1} & {num2} is {min_num}")