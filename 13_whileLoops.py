name = input("Enter your name: ")
while name == "":
    print("You did not enetr your name")
    name = input("Enter your name: ")
print(f"Hello {name}")


food = input("Enter a food you like (press q to quit): ")
while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like (press q to quit): ")
print("Bye")
