# args
def fullName(*args):
    for name in args:
        print(name, end=" ")


fullName("Mutasam", "Billah", "Auntor")


# kwargs
def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print()

details(Name="Auntor", 
        Department="ETE", 
        University="RUET")




# args abd kwargs together
def aboutMe(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")        
aboutMe("Mutasam", "Billah", "Auntor",
         Upazilla="Sherpur",
         District="Bogura")