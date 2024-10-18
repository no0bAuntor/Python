name = "Auntor"
age = 25
gpa = 5.00
is_student = True
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

# float to int
gpa = int(gpa)
print(f"{gpa} type of {type(gpa)}")

# int to float
age = float(age)
print(f"{age} type of {type(age)}")

# int to string
age = str(age)
print(f"{age} type of {type(age)}")
# age = age + 1  -> error
# age = age + "1" -> correct

# string to bool
name=bool(name)
print(name)
