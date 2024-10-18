price1 = 3.142685
price2 = 74.3621
price3 = 420.3695

# print specific decimal number
print("2 decimal number:")
print(f"Price 1 is ${price1:.2f}")
print(f"Price 2 is ${price2:.2f}")
print(f"Price 3 is ${price3:.2f}")

print("\n\n")

# Each value take 10 spaces
print("Each value take 10 spaces")
print(f"Price 1 is ${price1:10}")
print(f"Price 2 is ${price2:10}")
print(f"Price 3 is ${price3:10}")

print("\n\n")

# Each number 0 paded and gake 1- spaces
print("Each value 0 spaces and take 10 spaces")
print(f"Price 1 is ${price1:010}")
print(f"Price 2 is ${price2:010}")
print(f"Price 3 is ${price3:010}")

print("\n\n")

# All value are left justified
print("All value are left justified and take 10 spaces in total")
print(f"Price 1 is ${price1:<10}")
print(f"Price 2 is ${price2:<10}")
print(f"Price 3 is ${price3:<10}")

print("\n\n")

# All value are center justified
print("All value are center justified and take 10 spaces in total")
print(f"Price 1 is ${price1:^15}")
print(f"Price 2 is ${price2:^15}")
print(f"Price 3 is ${price3:^15}")

print("\n\n")

thousand=145246.2152
print(f"Insert comma after thoousand: {thousand:,.2f}")
