# input always return string


name = input("WHat is your name?: ")
age = input("How old are you?: ")
print(f"Hello {name}")
print(f"You are {age} years old")
age = int(age)
print(f"Next year you will be {age+1} years old")

# calculate area
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
print(f"The area is: {area} cm²")
