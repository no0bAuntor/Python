# 1
double =[]
for x in range(1,11):
    double.append(x*2)

print (double)

# 2
doubles=[x*2 for x in range(1,11)]
print (doubles)

# 3 (string)
fruits=["apple", "orange", "banana","grape"]
fruits=[fruit.upper() for fruit in fruits]
print (fruits)
fruitChar=[fruit[0] for fruit in fruits]
print(fruitChar)


# 4 condition
numbers=[1, -2, 3, -4, 5, -6]
positiveNum=[num for num in numbers if num > 0]
negativeNum=[num for num in numbers if num < 0]

print(positiveNum)
print(negativeNum)