# list=[] ordered and changeable, duplicate ok

fruits=["apple", "orange", "mango"] 

print(fruits[1])
print(fruits[:3])
print(fruits[1:3])
print(fruits[::2])  # step 1
print(fruits[::-1]) # reversed
print("coconut" in fruits)
print(fruits.index("orange")) # search element index
print(fruits.count("orange")) # count specific element 


fruits[0]="coconut"
fruits.append("banana") # add element
for fruit in fruits:
    print(fruit, end=" ")
print("\n")    
fruits.remove("banana") # remove element
for fruit in fruits:
    print(fruit, end=" ")

print("\n")    
fruits.insert(0,"pineapple") # insert element at specific index
for fruit in fruits:
    print(fruit, end=" ")


print("\n")    
fruits.sort() # sort elements (in alphabetical order)
for fruit in fruits:
    print(fruit, end=" ") 

# for reverse element in alphabetical order need to 1st sort function and then reverse function

print("\n")    
fruits.clear() # clear all elements
for fruit in fruits:
    print(fruit, end=" ") 
