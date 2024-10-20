fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(groceries[1][2])

for collection in groceries:
    for item in collection:
        print(item, end=" ")
    print()        
