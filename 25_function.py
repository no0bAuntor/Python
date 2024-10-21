def myAge(name, age):
    print(f"I am {name} and I'm {age} years old")


myAge("Auntor", 22)    

def fullName(firstName, lastName):
    firstName=firstName.capitalize()
    lastName=lastName.capitalize()
    return firstName + " "+ lastName

first=input("Enter your first name: ")
last=input("Enter your last name: ")

print(f"Your full name is {fullName(first, last)}")