class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("John", "20")
student2 = Student("Bob", "26")
student3 = Student("Sara", "21")
student4 = Student("Lisa", "25")

print(
    f"My graduating class of {Student.class_year} has a total of {Student.num_students} students"
)
