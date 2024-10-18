name = "mutasam billah auntor"
phone_numb= "14-85-6-45"
result = len(name)  # length of string
result = name.find("a")  # find index "a" of string
result = name.rfind("a")  # find last string index "a" of string
result=name.capitalize() #1st letter capital
result=name.upper() #all letter upper case
result=name.lower() #all letter lower case
result=name.isdigit() #check if all letter digit or not
result=phone_numb.isalpha() #check if all letter alphanetical or not -> space, digit is not alphabetical
result=phone_numb.count("-")
result=phone_numb.replace("-", " ")
print(result)



username=input("Enter your username: ")
if len(username)>12:
    print("Your username must be less than 12 characters")
elif not username.find(" ")==-1:
    print("Username can't contain spaces")    
elif not username.isalpha():
    print("Username can't contain numbers")    
else:
    print(f"Welcome {username}")    