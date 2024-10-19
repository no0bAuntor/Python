# set={} unordered and immutable, but add/remove ok. No duplicate

fruits = {"apple", "orange", "banana", "coconut"}


fruits.add("pineapple")
print(fruits)
fruits.remove("apple")
print(fruits)

fruits.clear()
print(fruits)