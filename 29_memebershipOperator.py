# in
# not in

# for string
word="Apple"
letter=input("Guess a letter in the secret word: ")

if letter in word:
    print(f"There is a {letter}")

else:
    print(f"{letter} was not found")    

email="mbauntor150@gmail.com"
if "@" in email and "." in email:
    print("Valid email")

else:
    print("Invalid email")

# for set
students={"Auntor", "Rakib", "Sakib"}    
student=input("ENter the name of students: ")

if student not in students: 
    print(f"{student} not found!")
    
else:
    print(f"{student} is found")     


#for dictionary
grades={"Auntor": "A",
        "Rakib": "B", "Sakib": "C"} 
student=input("Enter the name of students: ")

if student in grades:
    print(f"{student} got {grades[student]}")

else:
    print(f"{student} not found!")