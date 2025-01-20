class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Accord", 2022)

print(car1.make)
print(car2.model)
